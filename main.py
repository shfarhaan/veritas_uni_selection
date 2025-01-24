import streamlit as st

# Example university data (can be replaced with a full dataset as needed)
universities = [
    {
        "name": "Ulster University",
        "country": "UK",
        "city": "Belfast",
        "living_cost": "£500 to £1000 per month",
        "distance_from_city_center": 3.5  # in miles
    },
    {
        "name": "University of East London",
        "country": "UK",
        "city": "London",
        "living_cost": "£800 to £1500 per month",
        "distance_from_city_center": 7.2
    },
    {
        "name": "Middlesex University",
        "country": "UK",
        "city": "London",
        "living_cost": "£900 to £1400 per month",
        "distance_from_city_center": 8.0
    },
    {
        "name": "The University of the West of Scotland",
        "country": "UK",
        "city": "Paisley",
        "living_cost": "£600 to £1100 per month",
        "distance_from_city_center": 1.2
    },
    {
        "name": "Seoul National University",
        "country": "South Korea",
        "city": "Seoul",
        "living_cost": "₩800,000 to ₩1,200,000 per month",
        "distance_from_city_center": 5.0
    },
    {
        "name": "Kyung Hee University",
        "country": "South Korea",
        "city": "Seoul",
        "living_cost": "₩750,000 to ₩1,100,000 per month",
        "distance_from_city_center": 6.0
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
