# Import libraries
import openai
import streamlit as st
from streamlit_chat import message

# Background css
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background: rgba(0,0,0,0);
}}
[data-testid="stSidebar"] > div:first-child {{
background: rgba(211, 84, 106, 0.8);
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar 
st.sidebar.header("About")
API_KEY = st.sidebar.text_input(
            "Enter your OpenAI API key",
            type='password')

# Pass API Key
openai.api_key = API_KEY

# Create function to use OpenAI text-davinci-003 model
def generate_response(prompt):
    completion=openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    message=completion.choices[0].text
    return message

st.header(" 🤖 Heli - Your Everlasting Companion")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input=st.text_input("You:",key='input')

if user_input:
    try:
        output=generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
    except Exception as e:
        st.error(str(e), icon="🚨")
        

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

