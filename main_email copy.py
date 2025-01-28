import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


# def display_cover_image(image_path: str, overlay_text: str = None):
#     # Display the cover image
#     st.markdown(
#         """
#         <style>
#             .cover-container {
#                 position: relative;
#                 text-align: center;
#                 margin-bottom: 20px;
#             }
#             .cover-image {
#                 width: 100%;
#                 border-radius: 15px;
#                 box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
#             }
#             .overlay-text {
#                 position: absolute;
#                 top: 50%;
#                 left: 50%;
#                 transform: translate(-50%, -50%);
#                 background-color: rgba(0, 0, 0, 0.6);
#                 color: white;
#                 padding: 10px 20px;
#                 font-size: 24px;
#                 font-weight: bold;
#                 border-radius: 5px;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
    
#     if overlay_text:
#         # Use HTML to layer the image and text
#         st.markdown(
#             f"""
#             <div class="cover-container">
#                 <img src="{image_path}" alt="Cover Image" class="cover-image">
#                 <div class="overlay-text">{overlay_text}</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#     else:
#         # Fallback to using Streamlit's st.image for simpler rendering
#         st.image(image_path, use_column_width=True, caption="Cover Image")

# # Example usage:
# image_path = os.path.abspath("assets\cover_photo.png")

# # image_path = "cover_image.jpg"  # Use this if the image is stored locally in your project folder
# overlay_text = "Welcome to Our Application"

# # Call the function to display the cover image
# display_cover_image(image_path, overlay_text)



# University details dictionary (Add the full dictionary from your previous data)
UK_universities = [
    {
        "name": "Ulster University",
        "country": "UK",
        "city": "Coleraine",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": {
            "Bachelor's": "£14,000 to £18,000 per year",
            "Master's": "£15,000 to £20,000 per year",
            "PhD": "£16,000 to £20,000 per year",
        },
        "distance_from_city_center": 2.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Engineering", "Psychology", "Business Studies", "Biotechnology", "Media Studies"],
            "Master's": ["Data Science", "Cybersecurity", "MBA", "Public Health", "Architecture"],
            "PhD": ["Artificial Intelligence", "Medicine", "Law", "Sustainable Development"],
        },
        "english_proficiency_requirement": {
            "Bachelor's": "IELTS 6.0 or equivalent",
            "Master's": "IELTS 6.5 or equivalent",
            "PhD": "IELTS 7.0 or equivalent",
        },
        "intake": ["September", "January"],
        "additional_information": "Known for its strong focus on employability and partnerships with industries.",
    },
    {
        "name": "University of East London",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,200 to £1,800 per month",
        "tuition_fee": {
            "Bachelor's": "£14,000 to £16,000 per year",
            "Master's": "£15,000 to £18,000 per year",
            "PhD": "£16,000 to £18,000 per year",
        },
        "distance_from_city_center": 6.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Computer Science", "Nursing", "Architecture", "Sports Science", "Media Studies"],
            "Master's": ["Sustainability", "Creative Writing", "Data Science", "Finance", "Public Health"],
            "PhD": ["Environmental Studies", "Public Health", "Urban Design", "Digital Economy"],
        },
        "english_proficiency_requirement": {
            "Bachelor's": "IELTS 6.0 or equivalent",
            "Master's": "IELTS 6.5 or equivalent",
            "PhD": "IELTS 7.0 or equivalent",
        },
        "intake": ["September", "January"],
        "additional_information": "A modern university focused on career readiness and diverse programs.",
    },
    {
        "name": "Middlesex University",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,200 to £1,800 per month",
        "tuition_fee": {
            "Bachelor's": "£14,000 to £17,000 per year",
            "Master's": "£15,000 to £18,000 per year",
            "PhD": "£16,000 to £19,000 per year",
        },
        "distance_from_city_center": 7.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Law", "Marketing", "Health and Social Care", "Film Production", "Education"],
            "Master's": ["Digital Marketing", "Human Resources", "Artificial Intelligence", "Clinical Psychology"],
            "PhD": ["Law and Policy", "Social Sciences", "Cybersecurity", "Education Studies"],
        },
        "english_proficiency_requirement": {
            "Bachelor's": "IELTS 6.0 or equivalent",
            "Master's": "IELTS 6.5 or equivalent",
            "PhD": "IELTS 7.0 or equivalent",
        },
        "intake": ["September", "January"],
        "additional_information": "Offers strong support for international students and work placement opportunities.",
    },
    
    {
        "name": "University of Hertfordshire",
        "country": "UK",
        "city": "Hatfield",
        "living_cost": "£1,000 to £1,500 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£13,000 to £15,000 per year",
                "examples": {
                    "Computer Science": "£14,000 per year",
                    "Pharmacy": "£15,000 per year",
                    "Engineering": "£14,500 per year",
                    "Business Administration": "£13,800 per year",
                    "Psychology": "£13,500 per year"
                }
            },
            "Master's": {
                "range": "£15,000 to £17,000 per year",
                "examples": {
                    "Artificial Intelligence": "£16,500 per year",
                    "Cybersecurity": "£16,000 per year",
                    "MBA": "£17,000 per year",
                    "Health Informatics": "£15,800 per year",
                    "Data Science": "£16,200 per year"
                }
            },
            "PhD": {
                "range": "£13,000 to £16,000 per year",
                "examples": {
                    "Machine Learning": "£14,500 per year",
                    "Healthcare Research": "£13,500 per year",
                    "Climate Science": "£14,000 per year",
                    "Engineering Innovation": "£15,000 per year",
                    "Digital Economics": "£16,000 per year"
                }
            }
        },
        "distance_from_city_center": 2.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Computer Science", "Pharmacy", "Engineering", "Business Administration", "Psychology"],
            "Master's": ["Artificial Intelligence", "Cybersecurity", "MBA", "Health Informatics", "Data Science"],
            "PhD": ["Machine Learning", "Healthcare Research", "Climate Science", "Engineering Innovation", "Digital Economics"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.0 overall (no band less than 5.5)",
            "TOEFL": "80 overall (minimum of 18 in each section)"
        },
        "intake": ["September", "January"],
        "additional_information": "Renowned for its strong industry connections and modern campus facilities."
    },
    
    
    {
        "name": "The University of the West of Scotland",
        "country": "UK",
        "city": "Paisley",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£13,000 to £15,000 per year",
                "examples": {
                    "Business Studies": "£13,500 per year",
                    "Nursing": "£14,000 per year",
                    "Computer Science": "£13,800 per year",
                    "Film Production": "£14,200 per year",
                    "Engineering": "£15,000 per year"
                }
            },
            "Master's": {
                "range": "£14,000 to £16,000 per year",
                "examples": {
                    "Data Science": "£15,000 per year",
                    "Advanced Nursing": "£14,500 per year",
                    "MBA": "£16,000 per year",
                    "Health and Social Care": "£14,800 per year",
                    "Engineering Management": "£15,800 per year"
                }
            },
            "PhD": {
                "range": "£13,500 to £15,500 per year",
                "examples": {
                    "Health Sciences": "£14,000 per year",
                    "Artificial Intelligence": "£13,800 per year",
                    "Engineering": "£15,000 per year",
                    "Environmental Studies": "£14,200 per year",
                    "Social Sciences": "£13,500 per year"
                }
            }
        },
        "distance_from_city_center": 1.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Business Studies", "Nursing", "Computer Science", "Film Production", "Engineering"],
            "Master's": ["Data Science", "Advanced Nursing", "MBA", "Health and Social Care", "Engineering Management"],
            "PhD": ["Health Sciences", "Artificial Intelligence", "Engineering", "Environmental Studies", "Social Sciences"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.0 overall (no band less than 5.5)",
            "TOEFL": "78 overall (minimum of 18 in reading, 17 in writing, 17 in listening, and 20 in speaking)"
        },
        "intake": ["September", "January"],
        "additional_information": "Recognized for strong industry links and practical-focused education."
    },
    {
        "name": "Heriot-Watt University",
        "country": "UK",
        "city": "Edinburgh",
        "living_cost": "£1,000 to £1,500 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£15,000 to £18,000 per year",
                "examples": {
                    "Engineering": "£17,500 per year",
                    "Computer Science": "£16,000 per year",
                    "Economics": "£15,800 per year",
                    "Psychology": "£16,500 per year",
                    "Business Management": "£18,000 per year"
                }
            },
            "Master's": {
                "range": "£16,000 to £20,000 per year",
                "examples": {
                    "Renewable Energy Engineering": "£18,000 per year",
                    "Data Science": "£16,800 per year",
                    "MBA": "£20,000 per year",
                    "International Finance": "£17,200 per year",
                    "Artificial Intelligence": "£17,500 per year"
                }
            },
            "PhD": {
                "range": "£15,000 to £18,000 per year",
                "examples": {
                    "Robotics": "£16,000 per year",
                    "Climate Science": "£15,500 per year",
                    "Engineering": "£17,000 per year",
                    "Business Analytics": "£15,800 per year",
                    "Cognitive Science": "£16,200 per year"
                }
            }
        },
        "distance_from_city_center": 6.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Engineering", "Computer Science", "Economics", "Psychology", "Business Management"],
            "Master's": ["Renewable Energy Engineering", "Data Science", "MBA", "International Finance", "Artificial Intelligence"],
            "PhD": ["Robotics", "Climate Science", "Engineering", "Business Analytics", "Cognitive Science"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.5 overall (no band less than 6.0)",
            "TOEFL": "90 overall (minimum of 20 in each section)"
        },
        "intake": ["September", "January"],
        "additional_information": "Renowned for its strong engineering and business programs, with a global campus network."
    },
    {
        "name": "University of Wales Trinity Saint David",
        "country": "UK",
        "city": "Swansea",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£11,000 to £13,500 per year",
                "examples": {
                    "Business Management": "£12,000 per year",
                    "Creative Arts": "£13,000 per year",
                    "Computer Science": "£12,500 per year",
                    "Psychology": "£11,800 per year",
                    "Education Studies": "£11,500 per year"
                }
            },
            "Master's": {
                "range": "£12,000 to £14,000 per year",
                "examples": {
                    "Education Leadership": "£12,500 per year",
                    "Digital Marketing": "£13,000 per year",
                    "Heritage Studies": "£12,800 per year",
                    "Data Science": "£13,500 per year",
                    "Public Health": "£12,200 per year"
                }
            },
            "PhD": {
                "range": "£13,000 to £14,500 per year",
                "examples": {
                    "Sustainability Studies": "£13,500 per year",
                    "Psychology": "£14,000 per year",
                    "Cultural Studies": "£13,200 per year",
                    "Artificial Intelligence": "£13,800 per year",
                    "Education Policy": "£13,500 per year"
                }
            }
        },
        "distance_from_city_center": 1.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Business Management", "Creative Arts", "Computer Science", "Psychology", "Education Studies"],
            "Master's": ["Education Leadership", "Digital Marketing", "Heritage Studies", "Data Science", "Public Health"],
            "PhD": ["Sustainability Studies", "Psychology", "Cultural Studies", "Artificial Intelligence", "Education Policy"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.0 overall (no band less than 5.5)",
            "TOEFL": "78 overall (minimum of 18 in reading, 17 in writing, 17 in listening, and 20 in speaking)"
        },
        "intake": ["September", "January"],
        "additional_information": "A student-focused university offering personalized support and diverse programs."
    },
    {
        "name": "Queen Mary University of London",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,300 to £1,800 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£18,000 to £22,000 per year",
                "examples": {
                    "Medicine": "£42,000 per year",
                    "Law": "£19,500 per year",
                    "Computer Science": "£20,000 per year",
                    "Business Management": "£21,000 per year",
                    "Engineering": "£22,000 per year"
                }
            },
            "Master's": {
                "range": "£19,000 to £24,000 per year",
                "examples": {
                    "Data Science": "£21,500 per year",
                    "International Relations": "£19,000 per year",
                    "MBA": "£24,000 per year",
                    "Public Health": "£20,500 per year",
                    "Artificial Intelligence": "£21,000 per year"
                }
            },
            "PhD": {
                "range": "£18,000 to £22,000 per year",
                "examples": {
                    "Law": "£20,000 per year",
                    "Bioinformatics": "£19,500 per year",
                    "Engineering": "£22,000 per year",
                    "Public Policy": "£19,000 per year",
                    "Neuroscience": "£21,000 per year"
                }
            }
        },
        "distance_from_city_center": 3.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Medicine", "Law", "Computer Science", "Business Management", "Engineering"],
            "Master's": ["Data Science", "International Relations", "MBA", "Public Health", "Artificial Intelligence"],
            "PhD": ["Law", "Bioinformatics", "Engineering", "Public Policy", "Neuroscience"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.5 overall (no band less than 6.0)",
            "TOEFL": "92 overall (minimum of 23 in writing, 20 in speaking, 18 in reading, and 17 in listening)"
        },
        "intake": ["September", "January"],
        "additional_information": "Part of the Russell Group, recognized globally for high-impact research and diverse programs."
    },
    {
        "name": "BPP University",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,300 to £1,800 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£12,000 to £14,000 per year",
                "examples": {
                    "Business Management": "£13,000 per year",
                    "Law": "£14,000 per year",
                    "Health Sciences": "£13,500 per year"
                }
            },
            "Master's": {
                "range": "£13,000 to £16,000 per year",
                "examples": {
                    "Legal Practice": "£15,000 per year",
                    "Financial Technology": "£14,500 per year",
                    "Healthcare Management": "£14,000 per year"
                }
            },
            "PhD": {
                "range": "£14,000 to £17,000 per year",
                "examples": {
                    "Legal Studies": "£16,000 per year",
                    "Business Analytics": "£14,500 per year"
                }
            }
        },
        "distance_from_city_center": 2.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Business Management", "Law", "Health Sciences"],
            "Master's": ["Legal Practice", "Financial Technology", "Healthcare Management"],
            "PhD": ["Legal Studies", "Business Analytics"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.0 overall (no band less than 5.5)",
            "TOEFL": "78 overall (minimum of 18 in reading, 17 in writing, 17 in listening, and 20 in speaking)"
        },
        "intake": ["September", "January"],
        "additional_information": "Known for specialized professional programs, especially in law and business."
    },
    {
        "name": "University of Kent",
        "country": "UK",
        "city": "Canterbury",
        "living_cost": "£900 to £1,200 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£15,000 to £18,000 per year",
                "examples": {
                    "International Business": "£16,500 per year",
                    "Law": "£17,000 per year",
                    "Engineering": "£15,800 per year",
                    "Psychology": "£16,000 per year",
                    "Art History": "£15,500 per year"
                }
            },
            "Master's": {
                "range": "£16,000 to £20,000 per year",
                "examples": {
                    "MBA": "£20,000 per year",
                    "Cybersecurity": "£18,000 per year",
                    "Data Science": "£17,500 per year",
                    "International Relations": "£16,200 per year",
                    "Creative Writing": "£16,500 per year"
                }
            },
            "PhD": {
                "range": "£16,000 to £20,000 per year",
                "examples": {
                    "Cybersecurity": "£17,000 per year",
                    "International Business": "£18,000 per year",
                    "Creative Writing": "£16,500 per year"
                }
            }
        },
        "distance_from_city_center": 1.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["International Business", "Law", "Engineering", "Psychology", "Art History"],
            "Master's": ["MBA", "Cybersecurity", "Data Science", "International Relations", "Creative Writing"],
            "PhD": ["Cybersecurity", "International Business", "Creative Writing"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.5 overall (no band less than 6.0)",
            "TOEFL": "90 overall (minimum of 20 in each section)"
        },
        "intake": ["September", "January"],
        "additional_information": "The University of Kent is a research-intensive university with strong global partnerships."
    },
    {
        "name": "University of Greenwich",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,200 to £1,500 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£14,000 to £17,000 per year",
                "examples": {
                    "Business Management": "£15,000 per year",
                    "Computer Science": "£16,000 per year",
                    "Engineering": "£17,000 per year",
                    "Architecture": "£16,500 per year",
                    "Psychology": "£14,800 per year"
                }
            },
            "Master's": {
                "range": "£15,000 to £18,000 per year",
                "examples": {
                    "MBA": "£18,000 per year",
                    "Data Science": "£16,500 per year",
                    "Engineering Management": "£17,500 per year",
                    "Public Health": "£15,200 per year",
                    "Creative Writing": "£15,800 per year"
                }
            },
            "PhD": {
                "range": "£15,000 to £18,000 per year",
                "examples": {
                    "Sustainability Studies": "£16,000 per year",
                    "Artificial Intelligence": "£15,800 per year"
                }
            }
        },
        "distance_from_city_center": 5.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Business Management", "Computer Science", "Engineering", "Architecture", "Psychology"],
            "Master's": ["MBA", "Data Science", "Engineering Management", "Public Health", "Creative Writing"],
            "PhD": ["Sustainability Studies", "Artificial Intelligence"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.5 overall (no band less than 6.0)",
            "TOEFL": "90 overall (minimum of 20 in each section)"
        },
        "intake": ["September", "January"],
        "additional_information": "Offers a scenic campus in Greenwich with a strong focus on employability."
    },
    {
        "name": "Ravensbourne University",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,200 to £1,500 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£16,500 to £18,000 per year",
                "examples": {
                    "Animation": "£17,500 per year",
                    "Fashion Design": "£18,000 per year",
                    "Graphic Design": "£16,800 per year",
                    "Architecture": "£17,000 per year",
                    "Digital Media": "£16,500 per year"
                }
            },
            "Master's": {
                "range": "£17,000 to £19,000 per year",
                "examples": {
                    "Digital Media Management": "£18,000 per year",
                    "Interactive Digital Design": "£17,800 per year",
                    "Architecture": "£18,500 per year",
                    "UX/UI Design": "£17,500 per year",
                    "Creative Direction": "£19,000 per year"
                }
            },
            "PhD": {
                "range": "£18,000 to £21,000 per year",
                "examples": {
                    "Digital Arts": "£20,000 per year",
                    "Fashion Innovation": "£18,500 per year"
                }
            }
        },
        "distance_from_city_center": 2.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Animation", "Fashion Design", "Graphic Design", "Architecture", "Digital Media"],
            "Master's": ["Digital Media Management", "Interactive Digital Design", "Architecture", "UX/UI Design", "Creative Direction"],
            "PhD": ["Digital Arts", "Fashion Innovation"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.0 overall (no band less than 5.5)",
            "TOEFL": "80 overall (minimum of 18 in reading, 17 in writing, 17 in listening, and 20 in speaking)"
        },
        "intake": ["September", "January"],
        "additional_information": "Ravensbourne is known for its emphasis on creative disciplines and close industry connections."
    },
    {
        "name": "Bolton University (University of Greater Manchester)",
        "country": "UK",
        "city": "Bolton",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": {
            "Bachelor's": {
                "range": "£12,500 to £14,000 per year",
                "examples": {
                    "Business Management": "£13,000 per year",
                    "Nursing": "£14,000 per year",
                    "Engineering": "£13,500 per year",
                    "Psychology": "£12,800 per year",
                    "Sports Science": "£13,200 per year"
                }
            },
            "Master's": {
                "range": "£13,500 to £15,000 per year",
                "examples": {
                    "MBA": "£15,000 per year",
                    "Artificial Intelligence": "£14,500 per year",
                    "Advanced Engineering": "£13,800 per year",
                    "Public Health": "£13,700 per year",
                    "Education Leadership": "£14,000 per year"
                }
            },
            "PhD": {
                "range": "£14,000 to £16,000 per year",
                "examples": {
                    "Engineering": "£15,500 per year",
                    "Health Sciences": "£14,800 per year",
                    "Psychology": "£14,000 per year"
                }
            }
        },
        "distance_from_city_center": 10.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Business Management", "Nursing", "Engineering", "Psychology", "Sports Science"],
            "Master's": ["MBA", "Artificial Intelligence", "Advanced Engineering", "Public Health", "Education Leadership"],
            "PhD": ["Engineering", "Health Sciences", "Psychology"]
        },
        "english_proficiency_requirement": {
            "IELTS": "6.0 overall (no band less than 5.5)",
            "TOEFL": "80 overall (minimum of 18 in reading, 17 in writing, 17 in listening, and 20 in speaking)"
        },
        "intake": ["September", "January"],
        "additional_information": "Offers an affordable cost of living and is known for its strong student support system."
    }
]


# Function to filter universities
def filter_universities(country, city, program, test, intake):
    filtered = []
    for uni in UK_universities:
        if (
            uni["country"] == country and
            uni["city"] == city and
            program in uni["tuition_fee"] and
            test in uni["english_proficiency_requirement"] and
            intake in uni["intake"]
        ):
            filtered.append(uni)
    return filtered

# Function to send email
def send_email(to_email, filtered_universities):
    sender_email = "farhaan@csmeta.pro"  # Replace with your email
    sender_password = "FARhaan101&"  # Replace with your email password

    # Email Content
    subject = "University Search Results"
    body = "Here are the universities that match your preferences:\n\n"
    
    for university in filtered_universities:
        body += f"University Name: {university['name']}\n"
        body += f"City: {university['city']}\n"
        body += f"Living Cost: {university['living_cost']}\n"
        body += f"Tuition Fee: {university['tuition_fee']}\n"
        body += f"Intake: {', '.join(university['intake'])}\n"
        body += f"Notable Courses: {', '.join([course for courses in university['notable_courses'].values() for course in courses])}\n"
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

# Streamlit app
st.title("University Finder")

# User input selections
st.sidebar.header("Search Filters")
country_choice = st.sidebar.selectbox("Select Country", sorted(set([uni["country"] for uni in UK_universities])))
city_choice = st.sidebar.selectbox("Select City", sorted(set([uni["city"] for uni in UK_universities if uni["country"] == country_choice])))
program_choice = st.sidebar.selectbox("Select Program", ["Bachelor's", "Master's", "PhD"])
test_choice = st.sidebar.selectbox("Select English Proficiency Test", ["IELTS", "TOEFL"])
intake_choice = st.sidebar.selectbox("Select Intake", ["September", "January"])

email_input = st.sidebar.text_input("Enter Your Email (optional)")

# Filter universities
filtered_data = filter_universities(country_choice, city_choice, program_choice, test_choice, intake_choice)

# Display filtered results
if filtered_data:
    st.subheader("Filtered Universities:")
    for university in filtered_data:
        st.write(f"**University Name**: {university['name']}")
        st.write(f"**City**: {university['city']}")
        st.write(f"**Living Cost**: {university['living_cost']}")
        st.write(f"**Tuition Fee**: {university['tuition_fee'][program_choice]['range']}")
        st.write(f"**Intake**: {', '.join(university['intake'])}")
        st.write(f"**Notable Courses**: {', '.join(university['notable_courses'][program_choice])}")
        st.write("---")
    
    # Email Button
    if email_input:
        if st.button("Send Results to Email"):
            response = send_email(email_input, filtered_data)
            st.success(response)
else:
    st.write("No universities found for the selected preferences.")