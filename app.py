import streamlit as st
with st.expander('About this app'):
    st.write('In this application you can upload a picture of a crowd of people and it will predict the number of people in it')

st.sidebar.header('Please enter your details:')
user_name = st.sidebar.text_input('What is your name?')

col1, col2 = st.columns(2)

with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your *name*!')

st.button(“predict the number of people in this crowd”)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image')
import keras as keras
from keras import keras.models
from keras.models import load_model
model = load_model(‘C:\Users\Liran\Downloads\saved_model.pb’)

def predict(data):
return model.predict(data)

if st.button(“predict the number of people in this crowd”):
result = predict(uploaded_file)
st.text(result)

streamlit run app.py
