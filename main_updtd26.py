import streamlit as st
import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pydeck as pdk

# Sample university data with added fee and living expense info
universities = [
    {
        "name": "Ulster University",
        "country": "UK",
        "city": "Belfast",
        "latitude": 54.5843,
        "longitude": -5.9329,
        "programs": ["Engineering", "Law", "Business"],
        "intakes": ["January", "May", "September"],
        "english_tests": ["IELTS", "TOEFL"],
        "tuition_fee": 12000,
        "living_expense": 8000,
    },
    {
        "name": "University of East London",
        "country": "UK",
        "city": "London",
        "latitude": 51.5074,
        "longitude": -0.1278,
        "programs": ["Engineering", "Arts"],
        "intakes": ["February", "June", "October"],
        "english_tests": ["IELTS", "TOEFL"],
        "tuition_fee": 14000,
        "living_expense": 10000,
    },
    {
        "name": "Middlesex University",
        "country": "UK",
        "city": "London",
        "latitude": 51.5908,
        "longitude": -0.2284,
        "programs": ["Business", "Arts"],
        "intakes": ["January", "September"],
        "english_tests": ["IELTS"],
        "tuition_fee": 13000,
        "living_expense": 9000,
    },
    {
        "name": "Heriot-Watt University",
        "country": "UK",
        "city": "Edinburgh",
        "latitude": 55.9304,
        "longitude": -3.2097,
        "programs": ["Engineering", "Law"],
        "intakes": ["April", "September"],
        "english_tests": ["IELTS", "TOEFL", "PTE"],
        "tuition_fee": 15000,
        "living_expense": 12000,
    },
    {
        "name": "The University of the West of Scotland",
        "country": "UK",
        "city": "Paisley",
        "latitude": 55.8472,
        "longitude": -4.4234,
        "programs": ["Business", "Law"],
        "intakes": ["January", "September"],
        "english_tests": ["None"],
        "tuition_fee": 11000,
        "living_expense": 7000,
    },
]

# Convert to DataFrame
df_universities = pd.DataFrame(universities)

# Streamlit App
st.title("University Finder with Map")

# Step 1: Select Preferred City
st.subheader("Select City")
city = st.selectbox("Choose your preferred city:", sorted(df_universities["city"].unique()))

# Filter universities by city
filtered_df = df_universities[df_universities["city"] == city]

# Display map with universities in the selected city
st.subheader("Universities in Selected City")
if not filtered_df.empty:
    # Prepare map data
    map_data = filtered_df[["name", "latitude", "longitude"]]
    map_data["tooltip"] = map_data["name"]
    
    # Show map with markers
    st.map(map_data[["latitude", "longitude"]])

    # Display universities
    st.write("Universities in the selected city:")
    for _, row in filtered_df.iterrows():
        st.write(f"- **{row['name']}**")
else:
    st.warning("No universities found in the selected city.")

# Step 2: Select Program Category
st.subheader("Select Program Category")
program = st.selectbox("Choose your program category:", options=sorted({prog for prog_list in df_universities["programs"] for prog in prog_list}))

# Filter by Program
filtered_df = filtered_df[filtered_df["programs"].apply(lambda x: program in x)]

# Step 3: English Proficiency Test
st.subheader("English Proficiency Test Requirement")
english_test = st.selectbox("Select English proficiency test (or 'None'):", options=["None"] + sorted({test for test_list in df_universities["english_tests"] for test in test_list}))

# Filter by English Proficiency Test
filtered_df = filtered_df[filtered_df["english_tests"].apply(lambda x: english_test in x or english_test == "None")]

# Step 4: Tuition Fee and Living Expense Range
st.subheader("Set Your Budget")
tuition_range = st.slider("Select tuition fee range (in GBP):", min_value=0, max_value=20000, value=(10000, 15000))
living_range = st.slider("Select living expense range (in GBP):", min_value=0, max_value=20000, value=(5000, 10000))

# Filter by Fee and Expenses
filtered_df = filtered_df[
    (filtered_df["tuition_fee"] >= tuition_range[0]) & (filtered_df["tuition_fee"] <= tuition_range[1]) &
    (filtered_df["living_expense"] >= living_range[0]) & (filtered_df["living_expense"] <= living_range[1])
]

# Display Results
st.subheader("Filtered Universities:")
if not filtered_df.empty:
    for _, row in filtered_df.iterrows():
        st.write(f"- **{row['name']}** in {row['city']} ({row['country']})")
else:
    st.warning("No universities found matching your criteria.")

# Email Results
st.subheader("Email the Results")
user_email = st.text_input("Enter your email address:")
cc_email = st.text_input("Enter CC email address (optional):")
bcc_email = st.text_input("Enter BCC email address (optional):")
if st.button("Send Email"):
    try:
        # Prepare email content
        email_content = "\n".join([f"{row['name']} ({row['city']}, {row['country']})" for _, row in filtered_df.iterrows()])
        if not email_content:
            email_content = "No universities found matching the criteria."

        # Email settings
        sender_email = "farhaan@csmeta.pro"
        sender_password = "FARhaan101&"
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = user_email
        msg["Subject"] = "Filtered University List"
        if cc_email:
            msg["Cc"] = cc_email
        if bcc_email:
            msg["Bcc"] = bcc_email
        msg.attach(MIMEText(email_content, "plain"))

        # Send email
        with smtplib.SMTP_SSL("send.one.com", 465) as server:
            # server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Error sending email: {e}")

