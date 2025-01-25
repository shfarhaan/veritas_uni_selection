import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# University details dictionary (Add the full dictionary from your previous data)
UK_University_details = [
    {
        "name": "Ulster University",
        "country": "UK",
        "city": "Coleraine",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": "£14,000 to £20,000 per year",
        "distance_from_city_center": 2.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Engineering", "Psychology", "Business Studies"],
            "Master's": ["Data Science", "Cybersecurity", "MBA"],
            "PhD": ["Artificial Intelligence", "Medicine", "Law"]
        },
        "intake": ["September", "January"],
        "additional_information": "Known for its strong focus on employability and partnerships with industries."
    },
    {
        "name": "University of East London",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,200 to £1,800 per month",
        "tuition_fee": "£14,000 to £18,000 per year",
        "distance_from_city_center": 6.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Computer Science", "Nursing", "Architecture"],
            "Master's": ["Sustainability", "Creative Writing", "Data Science"],
            "PhD": ["Environmental Studies", "Public Health", "Urban Design"]
        },
        "intake": ["September", "January"],
        "additional_information": "A modern university focused on career readiness and diverse programs."
    },
    {
        "name": "Middlesex University",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,200 to £1,800 per month",
        "tuition_fee": "£14,000 to £18,000 per year",
        "distance_from_city_center": 7.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Law", "Marketing", "Health and Social Care"],
            "Master's": ["Digital Marketing", "Human Resources", "Artificial Intelligence"],
            "PhD": ["Law and Policy", "Social Sciences", "Cybersecurity"]
        },
        "intake": ["September", "January"],
        "additional_information": "Offers strong support for international students and work placement opportunities."
    },
    {
        "name": "The University of the West of Scotland",
        "country": "UK",
        "city": "Paisley",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": "£12,000 to £16,000 per year",
        "distance_from_city_center": 1.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Engineering", "Nursing", "Education"],
            "Master's": ["Big Data", "Renewable Energy", "Creative Industries"],
            "PhD": ["Computer Science", "Health Sciences", "Climate Change"]
        },
        "intake": ["September", "January"],
        "additional_information": "Known for its practical approach to learning and industry connections."
    },
    {
        "name": "Heriot-Watt University",
        "country": "UK",
        "city": "Edinburgh",
        "living_cost": "£1,000 to £1,500 per month",
        "tuition_fee": "£12,000 to £20,000 per year",
        "distance_from_city_center": 5.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Mechanical Engineering", "Business", "Architecture"],
            "Master's": ["Artificial Intelligence", "Energy Engineering", "International Business"],
            "PhD": ["Robotics", "Sustainable Engineering", "Economics"]
        },
        "intake": ["September", "January"],
        "additional_information": "Internationally recognized for innovation and research-led teaching."
    },
    {
        "name": "University of Wales Trinity Saint David",
        "country": "UK",
        "city": "Swansea",
        "living_cost": "£900 to £1,400 per month",
        "tuition_fee": "£11,000 to £15,000 per year",
        "distance_from_city_center": 2.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["History", "Design", "Psychology"],
            "Master's": ["Cybersecurity", "Digital Marketing", "Education Management"],
            "PhD": ["Health Sciences", "Culture Studies", "Social Work"]
        },
        "intake": ["September", "January"],
        "additional_information": "Offers a strong support system for students and focuses on creative industries."
    },
    {
        "name": "Queen Mary University of London",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,200 to £1,800 per month",
        "tuition_fee": "£15,000 to £22,000 per year",
        "distance_from_city_center": 3.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Law", "Engineering", "Business"],
            "Master's": ["Computer Science", "International Relations", "Data Science"],
            "PhD": ["Law", "Philosophy", "Public Health"]
        },
        "intake": ["September", "January"],
        "additional_information": "Renowned for its legal, medical, and engineering programs."
    },
    {
        "name": "BPP University",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,300 to £1,900 per month",
        "tuition_fee": "£12,000 to £16,000 per year",
        "distance_from_city_center": 2.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Law", "Accounting", "Finance"],
            "Master's": ["Law", "Business Management", "Finance"],
            "PhD": ["Legal Studies", "Business"]
        },
        "intake": ["September", "January"],
        "additional_information": "Specializes in professional qualifications and postgraduate law courses."
    },
    {
        "name": "University of Kent",
        "country": "UK",
        "city": "Canterbury",
        "living_cost": "£900 to £1,400 per month",
        "tuition_fee": "£13,000 to £18,000 per year",
        "distance_from_city_center": 1.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Biology", "History", "Law"],
            "Master's": ["Political Science", "Environmental Studies", "Human Rights"],
            "PhD": ["Sociology", "Law", "Environmental Science"]
        },
        "intake": ["September", "January"],
        "additional_information": "Known for its research in social sciences and humanities."
    },
    {
        "name": "University of Greenwich",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,100 to £1,700 per month",
        "tuition_fee": "£12,000 to £17,000 per year",
        "distance_from_city_center": 8.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Engineering", "Computer Science", "Accounting"],
            "Master's": ["Financial Management", "Mechanical Engineering", "Environmental Studies"],
            "PhD": ["Business Management", "Engineering", "Health Sciences"]
        },
        "intake": ["September", "January"],
        "additional_information": "A historical university with a focus on professional qualifications."
    },
    {
        "name": "Ravensbourne University",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,200 to £1,800 per month",
        "tuition_fee": "£14,000 to £18,000 per year",
        "distance_from_city_center": 6.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Digital Media", "Fashion", "Graphic Design"],
            "Master's": ["Media Production", "Data Science", "Digital Marketing"],
            "PhD": ["Media Studies", "Fashion Design", "Graphic Design"]
        },
        "intake": ["September", "January"],
        "additional_information": "Focused on creative industries, design, and technology."
    },
    {
        "name": "Bolton University - University of Greater Manchester",
        "country": "UK",
        "city": "Bolton",
        "living_cost": "£700 to £1,200 per month",
        "tuition_fee": "£12,000 to £16,000 per year",
        "distance_from_city_center": 10.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Business", "Engineering", "Nursing"],
            "Master's": ["Engineering Management", "Nursing", "Cybersecurity"],
            "PhD": ["Business Studies", "Engineering", "Nursing"]
        },
        "intake": ["September", "January"],
        "additional_information": "Offers a variety of courses with a focus on employability and local partnerships."
    }
]


# Streamlit app layout
st.title("University Search")

# User Input Widgets
country_choice = st.selectbox("Select Country", ["UK", "USA", "South Korea", "Japan", "EU", "UAE", "Kyrgyzstan"])
city_choice = st.selectbox("Select City", ["London", "Edinburgh", "Canterbury", "Swansea", "Coleraine", "Paisley", "Bolton"])
subject_choice = st.selectbox("Select Subject", ["Engineering", "Law", "Business", "Computer Science", "Health", "Design", "Marketing", "Data Science"])
intake_choice = st.selectbox("Select Intake", ["September", "January"])
email_input = st.text_input("Enter Student Email", placeholder="example@studentemail.com")

# Function to filter universities based on user preferences
def filter_universities(country, city, subject, intake):
    filtered_universities = []
    for university in UK_University_details:
        if university["country"] == country and university["city"] == city:
            for level, courses in university["notable_courses"].items():
                if subject in courses and intake in university["intake"]:
                    filtered_universities.append(university)
    return filtered_universities

# # Function to send email
# def send_email(to_email, filtered_universities):
#     sender_email = "farhaan@csmeta.pro"  # Replace with your email
#     sender_password = "FARhaan101&"  # Replace with your email password

#     # Email Content
#     subject = "University Search Results"
#     body = "Here are the universities that match your preferences:\n\n"

#     for university in filtered_universities:
#         body += f"University Name: {university['name']}\n"
#         body += f"City: {university['city']}\n"
#         body += f"Living Cost: {university['living_cost']}\n"
#         body += f"Tuition Fee: {university['tuition_fee']}\n"
#         body += f"Intake: {', '.join(university['intake'])}\n"
#         body += f"Notable Courses: {', '.join([course for courses in university['notable_courses'].values() for course in courses])}\n"
#         body += "---\n\n"

#     # Email Setup
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = to_email
#     msg["Subject"] = subject
#     msg.attach(MIMEText(body, "plain"))

#     try:
#         # Connect to the email server and send the email
#         with smtplib.SMTP("send.one.com", 465) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.sendmail(sender_email, to_email, msg.as_string())
#         return "Email sent successfully!"
#     except Exception as e:
#         return f"Error sending email: {str(e)}"

# # Filter universities based on user preferences
# filtered_data = filter_universities(country_choice, city_choice, subject_choice, intake_choice)

# # Display filtered results
# if filtered_data:
#     st.subheader("Filtered Universities:")
#     for university in filtered_data:
#         st.write(f"**University Name**: {university['name']}")
#         st.write(f"**City**: {university['city']}")
#         st.write(f"**Living Cost**: {university['living_cost']}")
#         st.write(f"**Tuition Fee**: {university['tuition_fee']}")
#         st.write(f"**Intake**: {', '.join(university['intake'])}")
#         st.write(f"**Notable Courses**: {', '.join([course for courses in university['notable_courses'].values() for course in courses])}")
#         st.write("---")
    
#     # Email Button
#     if email_input:
#         if st.button("Send Results to Email"):
#             response = send_email(email_input, filtered_data)
#             st.success(response)
# else:
#     st.write("No universities found for the selected preferences.")

def send_email(to_email, filtered_universities):
    sender_email = "farhaan@csmeta.pro"  # Replace with your email
    sender_password = "FARhaan101&"  # Replace with your email password

    # Email Content
    subject = "University Search Results"
    body = "Here are the universities that match your preferences:\n\n"
    for university in filtered_universities:
        body += f"University Name: {university['name']}\n"
        body += f"City: {university['city']}\n"
        body += "---\n\n"

    # Email Setup
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

  
    try:
        # Connect to the SMTP server using SSL
        with smtplib.SMTP_SSL("send.one.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending email: {str(e)}"

# Filter universities based on user preferences
filtered_data = filter_universities(country_choice, city_choice, subject_choice, intake_choice)

# Display filtered results
if filtered_data:
    st.subheader("Filtered Universities:")
    for university in filtered_data:
        st.write(f"**University Name**: {university['name']}")
        st.write(f"**City**: {university['city']}")
        st.write(f"**Living Cost**: {university['living_cost']}")
        st.write(f"**Tuition Fee**: {university['tuition_fee']}")
        st.write(f"**Intake**: {', '.join(university['intake'])}")
        st.write(f"**Notable Courses**: {', '.join([course for courses in university['notable_courses'].values() for course in courses])}")
        st.write("---")
    
    # Email Button
    if email_input:
        if st.button("Send Results to Email"):
            response = send_email(email_input, filtered_data)
            st.success(response)
else:
    st.write("No universities found for the selected preferences.")
