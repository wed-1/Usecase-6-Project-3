import streamlit as st

st.set_page_config(page_title="Data Overview", page_icon="📊", layout="wide")


st.markdown("# Dataset Overview")

# TODO: List of EDA steps that applied on data with description
st.markdown("## Introducion")

st.markdown("### Data")
st.markdown("The dataset contains the following columns:")
st.markdown("1. `city`: The city of the property.")
st.markdown("2. `district`: The district of the property.")
st.markdown("3. `neighborhood`: The neighborhood of the property.")
st.markdown("4. `type`: The type of the property (apartment or villa).")
st.markdown("5. `price`: The price of the property.")
st.markdown("6. `bedrooms`: The number of bedrooms in the property.")
st.markdown("7. `bathrooms`: The number of bathrooms in the property.")
st.markdown("8. `parking_spaces`: The number of parking spaces in the property.")
st.markdown("9. `living_rooms`: The number of living rooms in the property.")
st.markdown("10. `area`: The area of the property.")
st.markdown("11. `latitude`: The latitude of the property.")
st.markdown("12. `longitude`: The longitude of the property.")
st.markdown("13. `url`: The URL of the property.")
st.markdown("14. `source`: The source of the property.")
st.markdown("15. `date`: The date of the property.")

st.markdown("### Data Source")
st.markdown("The data is collected from the following sources:")
st.markdown("1. [Kaggle - Scrapped Data from Aqar](https://www.kaggle.com/datasets/salmanshir/riyadhhousingdata)")
