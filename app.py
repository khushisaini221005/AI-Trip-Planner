import streamlit as st

# Page Title and Layout
st.set_page_config(page_title="AI Trip Planner", page_icon="✈️")

st.title("✈️ AI Trip Planner")
st.write("Plan your custom travel itinerary with AI-powered suggestions!")

# Input fields
destination = st.text_input("🌍 Enter Destination:", placeholder="e.g. Paris, Goa, Tokyo")
days = st.number_input("📅 Number of Days:", min_value=1, max_value=30, value=3)
budget = st.selectbox("💰 Budget Level:", ["Budget", "Moderate", "Luxury"])

# Generate Plan Button
if st.button("Generate Travel Plan"):
    if destination:
        st.success(f"🎉 Travel Itinerary generated for {destination}!")
        st.subheader(f"📍 Trip Summary for {destination} ({days} Days - {budget} Budget)")
        
        for i in range(1, days + 1):
            with st.expander(f"Day {i} Schedule"):
                st.write(f"- **Morning:** Sightseeing and local breakfast in {destination}.")
                st.write(f"- **Afternoon:** Visit popular cultural spots and try local cuisine.")
                st.write(f"- **Evening:** Relaxation, shopping at local markets, and dinner.")
    else:
        st.warning("⚠️ Please enter a destination first!")
