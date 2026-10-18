import streamlit as st

st.set_page_config(page_title="AI Trip Planner", page_icon="✈️")

st.title("✈️ AI Trip Planner")
st.write("Welcome to AI Trip Planner! Plan your custom travel itinerary easily.")

destination = st.text_input("Enter Destination:")
days = st.number_input("Number of Days:", min_value=1, max_value=30, value=3)

if st.button("Generate Itinerary"):
    if destination:
        st.success(f"Generating a {days}-day itinerary for {destination}...")
    else:
        st.warning("Please enter a destination!")
