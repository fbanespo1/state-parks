# travel.py -- Tony Esposito

import openai 
import streamlit as st
from PIL import Image
import requests

openai.api_key = 'sk-xxxxxx'

# Set page configuration
st.set_page_config(page_title='Tennessee Travel Assistant', page_icon=':airplane:')

# Custom background
#image = Image.open('background.png')
#st.image(image, use_column_width=True)

# Custom CSS
#st.markdown("""
#    <style>
#    .reportview-container {
#        background: url("https://en.wikipedia.org/wiki/Tennessee_Department_of_Tourist_Development#/media/File:TN-Dept-of-Tourist-Dev-ColorPMS.png") no-repeat center center fixed; 
#        -webkit-background-size: cover;
#        -moz-background-size: cover;
#        -o-background-size: cover;
#        background-size: cover;
#    }
#    </style """, unsafe_allow_html=True)

st.header('Welcome to State Parks!')

def generate_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json",
        "User-Agent": "OpenAI Python"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful travel assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    if 'choices' in response_json and len(response_json['choices']) > 0:
        message = response_json['choices'][0]['message']['content']
    else:
        message = "Sorry, I couldn't generate a response."
    return message



# List of keywords that we want to check for
keywords = ["Tennessee", "Tennessee State Park", "State Parks"]

def validate_query(query):
    # Make the query lower case and split it into words
    words = query.lower().split()

    # Check if any of the keywords appear in the query
    for keyword in keywords:
        if keyword.lower() in words:
            return True

    # If none of the keywords appear in the query, return False
    return False

user_input = st.text_area('Ask me anything about traveling in Tennessee!', height=150)
if user_input:
    if validate_query(user_input):
        output = generate_response(user_input)
        st.write(output)
    else:
        st.write("I'm sorry, I can only provide information about State Parks.")
