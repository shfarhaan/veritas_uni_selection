import streamlit as st

# Example data structure for demonstration purposes
uni_data = {
    "Living Cost": "£500 to £1000 per month",
}

# # Corrected function to extract ranges
# def extract_range(range_str):
#     # Remove any non-numeric characters except "to" for splitting
#     cleaned_str = range_str.replace("£", "").replace(",", "").replace("per month", "").strip()
#     try:
#         return list(map(int, cleaned_str.split("to")))
#     except ValueError:
#         st.error(f"Error parsing range: {range_str}")
#         return [0, 0]  # Default fallback

# Adding additional filters
Country = ["USA", "UK", "South Korea", "Japan", "EU", "UAE", "Kyrgyzstan"]

UK_University_list = [
    "Ulster University",
    "University of East London",
    "Middlesex University",
    "The University of the West of Scotland",
    "Heriot-Watt University",
    "University of Wales Trinity Saint David",
    "Queen Mary University of London",
    "BPP University",
    "University of Kent",
    "University of Greenwich",
    "Ravensbourne University",
    "Bolton University - University of Greater Manchester"
]

# Streamlit app interface
st.title("University Selection App")

# Country filter
selected_country = st.selectbox("Select a Country", Country)

# Helper function to extract numeric range from a string
def extract_range(range_str):
    # Remove any non-numeric characters except "to" for splitting
    cleaned_str = range_str.replace("£", "").replace(",", "").replace("per month", "").strip()
    try:
        return list(map(int, cleaned_str.split("to")))
    except ValueError:
        st.error(f"Error parsing range: {range_str}")
        return [0, 0]  # Default fallback
    
    


# UK universities filter (if the country is UK)
if selected_country == "UK":
    selected_university = st.selectbox("Select a UK University", UK_University_list)
    st.write(f"You selected: {selected_university}")

# Example usage of the corrected `extract_range` function
living_cost_range = extract_range(uni_data["Living Cost"])
st.write("Living Cost Range:", living_cost_range)


# Data for universities
universities_data = {
    "Ulster University": {
        "Campuses": ["Belfast", "Coleraine", "Derry~Londonderry", "Jordanstown"],
        "Tuition Fee": "£14,000 to £15,000",
        "Living Cost": "£800 to £1000 per month",
        "Distance from London": "400 miles",
        "Notable Courses": {
            "Bachelor's": ["Biomedical Science", "Computer Science", "Business Studies"],
            "Master's": ["Data Science", "International Business", "Advanced Clinical Practice"],
            "PhD": ["Engineering", "Psychology", "Law"]
        }
    },
    # ... Add the rest of the university data as provided
}


# Sidebar filters
st.sidebar.header("Filter Options")
selected_distance = st.sidebar.slider("Maximum Distance from London (miles)", 0, 500, 100)
selected_tuition = st.sidebar.slider("Maximum Tuition Fee (£)", 10000, 25000, 15000)
selected_living_cost = st.sidebar.slider("Maximum Living Cost (£ per month)", 500, 2000, 1000)
selected_courses = st.sidebar.multiselect("Select Notable Courses", 
                                          ["Biomedical Science", "Computer Science", "Business Studies", 
                                           "Data Science", "International Business", "Engineering", 
                                           "Psychology", "Law", "Medicine", "MBA", "Fashion Design"],
                                          [])

# Main section
st.title("University Explorer")
st.markdown("Use the filters in the sidebar to find universities matching your preferences.")

# Filtered university display
filtered_universities = []

for uni_name, uni_data in universities_data.items():
    # Parse numeric ranges
    tuition_range = extract_range(uni_data["Tuition Fee"])
    living_cost_range = extract_range(uni_data["Living Cost"])
    distance = int(uni_data["Distance from London"].split()[0])
    
    # Apply filters
    if (
        distance <= selected_distance and
        tuition_range and tuition_range[1] <= selected_tuition and
        living_cost_range and living_cost_range[1] <= selected_living_cost
    ):
        # Check if courses filter matches
        if selected_courses:
            courses = []
            for degree_level in uni_data["Notable Courses"].values():
                courses.extend(degree_level)
            if not any(course in courses for course in selected_courses):
                continue
        
        filtered_universities.append(uni_name)

# Display filtered universities
if filtered_universities:
    for uni_name in filtered_universities:
        st.subheader(uni_name)
        uni_data = universities_data[uni_name]
        st.write(f"**Campuses:** {', '.join(uni_data.get('Campuses', ['N/A']))}")
        st.write(f"**Tuition Fee:** {uni_data['Tuition Fee']}")
        st.write(f"**Living Cost:** {uni_data['Living Cost']}")
        st.write(f"**Distance from London:** {uni_data['Distance from London']}")
        st.write("**Notable Courses:**")
        for degree, courses in uni_data["Notable Courses"].items():
            st.write(f"- {degree}: {', '.join(courses)}")
        st.markdown("---")
else:
    st.warning("No universities match your filters. Try adjusting the criteria.")

# Footer
st.markdown("**Note:** Tuition fees and living costs are approximate ranges. Please verify with the respective universities.")
