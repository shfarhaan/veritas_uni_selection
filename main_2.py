import streamlit as st

# Data for universities
universities = [
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
        "additional_information": "Offers a variety of courses with a focus on employability and local partnerships."
    }
]

# Streamlit app
st.title("University Finder")
st.markdown("Find universities based on your preferences!")

# User inputs
st.sidebar.header("Filter Options")
country = st.sidebar.selectbox("Select Country", sorted(set([u["country"] for u in universities])))
city = st.sidebar.selectbox("Select City", sorted(set([u["city"] for u in universities if u["country"] == country])))
distance = st.sidebar.slider("Distance from City Center (miles)", 0.0, 5.0, 2.0)
subject_level = st.sidebar.radio("Select Subject Level", ["Bachelor's", "Master's", "PhD"])
subject = st.sidebar.text_input("Enter Subject (Optional)")
intake = st.sidebar.text_input("Enter Intake (e.g., Fall 2024)")

# Search for matching universities
filtered_universities = []
for uni in universities:
    if (
        uni["country"] == country
        and uni["city"] == city
        and uni["distance_from_city_center"] <= distance
    ):
        if subject:
            courses = uni["notable_courses"].get(subject_level, [])
            if any(subject.lower() in course.lower() for course in courses):
                filtered_universities.append(uni)
        else:
            filtered_universities.append(uni)

# Display results
if filtered_universities:
    st.subheader("Matching Universities:")
    for uni in filtered_universities:
        st.markdown(f"### {uni['name']}")
        st.write(f"**Country:** {uni['country']}")
        st.write(f"**City:** {uni['city']}")
        st.write(f"**Living Cost:** {uni['living_cost']}")
        st.write(f"**Tuition Fee:** {uni['tuition_fee']}")
        st.write(f"**Distance from City Center:** {uni['distance_from_city_center']} miles")
        st.write(f"**Notable Courses ({subject_level}):** {', '.join(uni['notable_courses'][subject_level])}")
        st.write(f"**Additional Information:** {uni['additional_information']}")
        st.write("---")
else:
    st.warning("No universities match your criteria. Try adjusting your filters!")
