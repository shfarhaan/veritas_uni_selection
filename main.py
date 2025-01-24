import streamlit as st

# Example university data (can be replaced with a full dataset as needed)
universities = [
    {
        "name": "Harvard University",
        "country": "USA",
        "city": "Cambridge",
        "living_cost": "$2,000 to $3,000 per month",
        "tuition_fee": "$50,000 to $60,000 per year",
        "distance_from_city_center": 2.1,  # in miles
        "notable_courses": {
            "Bachelor's": ["Economics", "Computer Science", "Biological Sciences"],
            "Master's": ["Business Administration", "Law", "Public Health"],
            "PhD": ["Physics", "Education", "Political Science"]
        },
        "additional_information": "One of the Ivy League universities, known for its academic excellence and extensive research opportunities."
    },
    {
        "name": "Stanford University",
        "country": "USA",
        "city": "Stanford",
        "living_cost": "$2,500 to $3,500 per month",
        "tuition_fee": "$55,000 to $60,000 per year",
        "distance_from_city_center": 3.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Engineering", "Human Biology", "Psychology"],
            "Master's": ["Artificial Intelligence", "Business Analytics", "Mechanical Engineering"],
            "PhD": ["Materials Science", "Linguistics", "Sociology"]
        },
        "additional_information": "Located in Silicon Valley, it’s a hub for innovation and entrepreneurship."
    },
    {
        "name": "University of California, Berkeley",
        "country": "USA",
        "city": "Berkeley",
        "living_cost": "$2,000 to $3,000 per month",
        "tuition_fee": "$40,000 to $50,000 per year",
        "distance_from_city_center": 1.8,  # in miles
        "notable_courses": {
            "Bachelor's": ["Electrical Engineering", "Environmental Science", "Economics"],
            "Master's": ["Data Science", "Urban Planning", "Computer Science"],
            "PhD": ["Public Policy", "Chemistry", "Mechanical Engineering"]
        },
        "additional_information": "Ranked among the top public universities globally."
    },
    {
        "name": "Massachusetts Institute of Technology (MIT)",
        "country": "USA",
        "city": "Cambridge",
        "living_cost": "$2,500 to $3,500 per month",
        "tuition_fee": "$55,000 to $60,000 per year",
        "distance_from_city_center": 2.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Aeronautics and Astronautics", "Computer Science", "Mathematics"],
            "Master's": ["Engineering Management", "Artificial Intelligence", "Economics"],
            "PhD": ["Biotechnology", "Nuclear Science", "Physics"]
        },
        "additional_information": "Globally renowned for its engineering and technology programs."
    },
    {
        "name": "California Institute of Technology (Caltech)",
        "country": "USA",
        "city": "Pasadena",
        "living_cost": "$2,000 to $3,000 per month",
        "tuition_fee": "$55,000 to $60,000 per year",
        "distance_from_city_center": 1.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Physics", "Chemical Engineering", "Applied Mathematics"],
            "Master's": ["Data Science", "Astrophysics", "Mechanical Engineering"],
            "PhD": ["Astronomy", "Geology", "Computer Science"]
        },
        "additional_information": "Specializes in science and engineering with small class sizes."
    },
    {
        "name": "University of Chicago",
        "country": "USA",
        "city": "Chicago",
        "living_cost": "$1,800 to $2,500 per month",
        "tuition_fee": "$50,000 to $60,000 per year",
        "distance_from_city_center": 4.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Economics", "Political Science", "Philosophy"],
            "Master's": ["Public Policy", "MBA", "Statistics"],
            "PhD": ["Econometrics", "Sociology", "Law"]
        },
        "additional_information": "Known for its rigorous academics and Nobel laureate alumni."
    },
    {
        "name": "University of California, Los Angeles (UCLA)",
        "country": "USA",
        "city": "Los Angeles",
        "living_cost": "$2,500 to $3,000 per month",
        "tuition_fee": "$40,000 to $50,000 per year",
        "distance_from_city_center": 6.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Film Studies", "Biology", "Psychology"],
            "Master's": ["Public Health", "Urban Planning", "Economics"],
            "PhD": ["Anthropology", "Physics", "Public Policy"]
        },
        "additional_information": "Located in a vibrant city with diverse opportunities."
    },
    {
        "name": "Columbia University",
        "country": "USA",
        "city": "New York",
        "living_cost": "$2,500 to $4,000 per month",
        "tuition_fee": "$55,000 to $60,000 per year",
        "distance_from_city_center": 5.2,  # in miles
        "notable_courses": {
            "Bachelor's": ["Journalism", "History", "Political Science"],
            "Master's": ["International Affairs", "Data Science", "Law"],
            "PhD": ["Psychology", "Neuroscience", "Education"]
        },
        "additional_information": "An Ivy League institution located in the heart of New York City."
    },
    {
        "name": "University of Michigan, Ann Arbor",
        "country": "USA",
        "city": "Ann Arbor",
        "living_cost": "$1,500 to $2,500 per month",
        "tuition_fee": "$40,000 to $50,000 per year",
        "distance_from_city_center": 2.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Mechanical Engineering", "Psychology", "Business"],
            "Master's": ["Data Science", "Public Policy", "Education"],
            "PhD": ["Biology", "Physics", "Social Work"]
        },
        "additional_information": "A top public university with strong research output."
    },
    {
        "name": "New York University (NYU)",
        "country": "USA",
        "city": "New York",
        "living_cost": "$3,000 to $4,000 per month",
        "tuition_fee": "$55,000 to $60,000 per year",
        "distance_from_city_center": 2.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Film Studies", "Computer Science", "Finance"],
            "Master's": ["Business Analytics", "International Relations", "Journalism"],
            "PhD": ["Economics", "Public Administration", "Mathematics"]
        },
        "additional_information": "A globally recognized university located in downtown Manhattan."
    },
    
    {
        "name": "University of Oxford",
        "country": "UK",
        "city": "Oxford",
        "living_cost": "£1,200 to £1,800 per month",
        "tuition_fee": "£26,000 to £30,000 per year",
        "distance_from_city_center": 1.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Philosophy, Politics and Economics (PPE)", "Computer Science", "Law"],
            "Master's": ["Artificial Intelligence", "Data Science", "Business Administration"],
            "PhD": ["Physics", "Public Policy", "History"]
        },
        "additional_information": "One of the oldest universities in the world, offering excellent academic and research opportunities."
    },
    {
        "name": "University of Cambridge",
        "country": "UK",
        "city": "Cambridge",
        "living_cost": "£1,200 to £1,800 per month",
        "tuition_fee": "£24,000 to £28,000 per year",
        "distance_from_city_center": 1.8,  # in miles
        "notable_courses": {
            "Bachelor's": ["Engineering", "Medicine", "Mathematics"],
            "Master's": ["Applied Mathematics", "Economics", "Linguistics"],
            "PhD": ["Neuroscience", "Climate Science", "Literature"]
        },
        "additional_information": "Globally recognized for research and academics with Nobel laureate alumni."
    },
    {
        "name": "Imperial College London",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,500 to £2,500 per month",
        "tuition_fee": "£30,000 to £34,000 per year",
        "distance_from_city_center": 2.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Biomedical Engineering", "Electrical Engineering", "Computing"],
            "Master's": ["Finance", "Artificial Intelligence", "Renewable Energy"],
            "PhD": ["Chemical Engineering", "Life Sciences", "Machine Learning"]
        },
        "additional_information": "Specializes in STEM subjects and is located in the heart of London."
    },
    {
        "name": "University College London (UCL)",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,500 to £2,500 per month",
        "tuition_fee": "£25,000 to £30,000 per year",
        "distance_from_city_center": 1.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Architecture", "Psychology", "Economics"],
            "Master's": ["Urban Planning", "Data Science", "Cognitive Neuroscience"],
            "PhD": ["Philosophy", "Medicine", "Computer Vision"]
        },
        "additional_information": "A multidisciplinary university with a strong emphasis on global research."
    },
    {
        "name": "University of Edinburgh",
        "country": "UK",
        "city": "Edinburgh",
        "living_cost": "£1,000 to £1,500 per month",
        "tuition_fee": "£20,000 to £24,000 per year",
        "distance_from_city_center": 1.2,  # in miles
        "notable_courses": {
            "Bachelor's": ["Artificial Intelligence", "Medicine", "History"],
            "Master's": ["Data Science", "Business Analytics", "Public Health"],
            "PhD": ["Sustainability", "Economics", "Physics"]
        },
        "additional_information": "Ranked highly for AI research and located in Scotland's capital."
    },
    {
        "name": "University of Manchester",
        "country": "UK",
        "city": "Manchester",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": "£18,000 to £22,000 per year",
        "distance_from_city_center": 2.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Materials Science", "Biotechnology", "Business"],
            "Master's": ["Data Science", "Renewable Energy", "Economics"],
            "PhD": ["Astronomy", "Medicine", "Sociology"]
        },
        "additional_information": "Known for pioneering graphene research and a diverse student population."
    },
    {
        "name": "King's College London",
        "country": "UK",
        "city": "London",
        "living_cost": "£1,500 to £2,500 per month",
        "tuition_fee": "£25,000 to £30,000 per year",
        "distance_from_city_center": 2.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Law", "Nursing", "War Studies"],
            "Master's": ["International Relations", "Public Health", "Data Science"],
            "PhD": ["History", "Psychology", "Neuroscience"]
        },
        "additional_information": "Located in central London with a focus on healthcare and social sciences."
    },
    {
        "name": "University of Warwick",
        "country": "UK",
        "city": "Coventry",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": "£20,000 to £25,000 per year",
        "distance_from_city_center": 3.5,  # in miles
        "notable_courses": {
            "Bachelor's": ["Economics", "Engineering", "Philosophy"],
            "Master's": ["Business Analytics", "Statistics", "Environmental Engineering"],
            "PhD": ["Econometrics", "Cybersecurity", "Physics"]
        },
        "additional_information": "Known for its business school and strong engineering programs."
    },
    {
        "name": "University of Bristol",
        "country": "UK",
        "city": "Bristol",
        "living_cost": "£1,000 to £1,500 per month",
        "tuition_fee": "£20,000 to £25,000 per year",
        "distance_from_city_center": 1.0,  # in miles
        "notable_courses": {
            "Bachelor's": ["Aerospace Engineering", "Veterinary Science", "Philosophy"],
            "Master's": ["Quantum Engineering", "Data Science", "Global Health"],
            "PhD": ["Robotics", "Physics", "Environmental Science"]
        },
        "additional_information": "Focuses on interdisciplinary research and sustainability."
    },
    {
        "name": "Durham University",
        "country": "UK",
        "city": "Durham",
        "living_cost": "£800 to £1,200 per month",
        "tuition_fee": "£19,000 to £23,000 per year",
        "distance_from_city_center": 0.8,  # in miles
        "notable_courses": {
            "Bachelor's": ["Theology", "Archaeology", "Physics"],
            "Master's": ["Astronomy", "Business Analytics", "Environmental Studies"],
            "PhD": ["Anthropology", "Climate Science", "Astronomy"]
        },
        "additional_information": "Highly regarded for humanities and natural sciences."
    }
    
    
    
]


# Helper function to extract and convert living cost ranges
def extract_range(range_str, currency="£"):
    try:
        # Remove non-numeric characters and split the range
        cleaned_str = range_str.replace(currency, "").replace(",", "").replace("per month", "").strip()
        return list(map(int, cleaned_str.split("to")))
    except ValueError:
        st.error(f"Error parsing range: {range_str}")
        return [0, 0]

# Streamlit app layout and filters
def main():
    st.title("University Selection and Filter App")

    # Country filter
    countries = sorted(set(uni["country"] for uni in universities))
    selected_country = st.selectbox("Select a Country", countries)

    # University filter (filtered by selected country)
    filtered_universities = [uni for uni in universities if uni["country"] == selected_country]
    university_names = sorted(uni["name"] for uni in filtered_universities)
    selected_university = st.selectbox("Select a University", university_names)

    # Get details of the selected university
    selected_uni_details = next(uni for uni in filtered_universities if uni["name"] == selected_university)

    # Living cost range filter
    default_living_cost_range = extract_range(selected_uni_details["living_cost"])
    adjusted_living_cost_range = st.slider(
        "Adjust Living Cost Range (£)",
        min_value=0,
        max_value=3000,
        value=(default_living_cost_range[0], default_living_cost_range[1]),
        step=50
    )

    # Distance from city center filter
    max_distance = max(uni["distance_from_city_center"] for uni in filtered_universities)
    selected_distance = st.slider(
        "Maximum Distance from City Center (miles)",
        min_value=0.0,
        max_value=max_distance,
        value=max_distance,
        step=0.1
    )

    # Apply filter button
    if st.button("Apply Filter"):
        # Filter universities based on living cost and distance
        filtered_results = [
            uni for uni in filtered_universities
            if extract_range(uni["living_cost"])[0] >= adjusted_living_cost_range[0]
            and extract_range(uni["living_cost"])[1] <= adjusted_living_cost_range[1]
            and uni["distance_from_city_center"] <= selected_distance
        ]

        # Display filtered results
        if filtered_results:
            st.subheader("Filtered Universities")
            for uni in filtered_results:
                st.write(f"**{uni['name']}**")
                st.write(f"City: {uni['city']}")
                st.write(f"Living Cost: {uni['living_cost']}")
                st.write(f"Distance from City Center: {uni['distance_from_city_center']} miles")
                st.write("---")
        else:
            st.warning("No universities match the selected filters.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
