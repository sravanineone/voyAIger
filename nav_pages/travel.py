# Import packages and modules | External
import streamlit as st

# Import packages and modules | Internal
from voyAIger_package import config as cfg

# Page title
st.title("Travel")

# Set page tabs
flight_tab, train_tab, hotel_tab, bookings_tab = st.tabs([":material/flight: Flight", ":material/train: Train", ":material/hotel: Hotel", ":material/calendar_month: Bookings"])

