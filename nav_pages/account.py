# Import packages and modules | External
import streamlit as st
from datetime import date
from datetime import datetime

# Import packages and modules | Internal
from voyAIger_package import config as cfg

# Page title
st.title("Account")

# Set page tabs
login_tab, forgot_password_tab, signup_tab = st.tabs([":material/login: Login", ":material/lock_reset: Forgot Password", ":material/app_registration: Sign Up"])

with login_tab:
    with st.form(key="login_form", clear_on_submit=False, border=True):
        st.caption(":blue-background[*Fields marked :red[*] are required.*]")
        user_id = st.text_input(label=":material/person: User ID :red[*]", placeholder="Enter your User ID here", help="User ID cn be either User ID or 10 digit phone number or E-Mail ID or Unique ID")
        password = st.text_input(label=":material/password: Password :red[*]", placeholder="Enter your password here", type="password", help="")
        login_form_submitted = st.form_submit_button(label="Submit")
        
with forgot_password_tab:
    with st.form(key="forgot_password_form", clear_on_submit=False, border=True):
        st.caption(":blue-background[*Fields marked :red[*] are required.*]")
        user_id = st.text_input(label=":material/person: User ID :red[*]", placeholder="Enter your User ID here", help="User ID cn be either User ID or 10 digit phone number or E-Mail ID or Unique ID")
        password = st.text_input(label=":material/password: Password :red[*]", placeholder="Enter your password here", type="password", help="")
        forgot_password_form_submitted = st.form_submit_button(label="Submit")

with signup_tab:
    with st.form(key="signup_form", clear_on_submit=False, border=True):
        st.caption(":blue-background[*Fields marked :red[*] are required.*]")
        col_1, col_2 = st.columns(2)
        full_name = col_1.text_input(label="Full Name")
        password = col_2.text_input(label="Password :red[*]", placeholder="********", type="password", help="")
        id_type = col_1.selectbox(label="ID Type", options=["Aadhaar", "Passport", "Drivign License", "Voter ID", "PAN"])
        id_value = col_2.text_input(label="ID Value")
        col_email, col_country_code, col_phone_num = st.columns([68, 9, 23])
        email = col_email.text_input(label="Email :red[*]", placeholder="user@domain.com")
        country_code = col_country_code.text_input(label=" ", value="+91", disabled=True)
        phone_num = col_phone_num.text_input(label="Phone Number", placeholder="9876543210", max_chars=10)
        col_dob, col_gender, col_marital_sta = st.columns([32, 35, 33])
        dob = col_dob.date_input(label="Date of Birth", format="YYYY-MM-DD", min_value=datetime.strptime("1900-01-01", "%Y-%m-%d").date(), max_value=date.today())
        gender = col_gender.selectbox(label="Gender", options=["Female", "Male"], placeholder="--Select--")
        marital_sta = col_marital_sta.selectbox(label="Marital Status", options=["Yes, married", "No"], placeholder="--Select--")
        address_col1, address_col2, address_col3, address_col4 = st.columns([32, 35, 19, 14])
        address_line1 = address_col1.text_input(label="Address Line 1")
        state = address_col2.selectbox(label="State", options=["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"])
        city = address_col3.text_input(label="City")
        pincode = address_col4.text_input(label="Pincode :red[*]", max_chars=6, placeholder="123456")
        col_sec_q, col_sec_a = st.columns([68, 33])
        security_question = col_sec_q.selectbox(label="Security Question", options=["What city were you born in?", "What sport do you prefer the most?", "What was the name of your first school?", "In what city or town did your parents meet?"])
        security_q_answer = col_sec_a.text_input(label="Answer")
        signup_form_submitted = st.form_submit_button(label="Submit")
