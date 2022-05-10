# login.py
# Modules
import pyrebase
import streamlit as st
from datetime import datetime
import webbrowser

# Configuration Key
firebaseConfig = {
    'apiKey': "AIzaSyBqwL_-oqmo4D8hS7NUpyisMCXmULmJuD4",
    'authDomain': "test-firestore-streamlit-56.firebaseapp.com",
    'databaseURL': "https://test-firestore-streamlit-56-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "test-firestore-streamlit-56",
    'storageBucket': "test-firestore-streamlit-56.appspot.com",
    'messagingSenderId': "1022976520010",
    'appId': "1:1022976520010:web:668de590f84b90ea6fdbb3",
    'measurementId': "G-XK627Z638H"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("Our community app")

# Authentication
choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

# Obtain User Input for email and password
email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password', type='password')

# App

# Sign up Block
if choice == 'Sign up':
    handle = st.sidebar.text_input(
        'Please input your app handle name', value='Default')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created suceesfully!')
        st.balloons()
        # Sign in
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome' + handle)
        st.info('Login via login drop down selection')

# Login Block
if choice == 'Login':
    login = st.sidebar.checkbox('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email, password)
        st.write(
            '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        bio = st.radio('Jump to', ['Home', 'Workplace Feeds', 'Settings'])

# SETTINGS PAGE
        if bio == 'Home':
            url = 'http://localhost:8502/'
            if st.button('Open Recommendation'):
                webbrowser.open_new_tab(url)
            
            
        