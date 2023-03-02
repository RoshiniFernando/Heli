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

API_KEY = st.sidebar.text_input(
            "Enter your OpenAI API key",
            type='password')


st.sidebar.header("About")
st.sidebar.markdown(
    """
App created by [roshinifer333](https://twitter.com/roshinifer333) using [Streamlit](https://streamlit.io/) 🎈, 
 [streamlit-chat](https://pypi.org/project/streamlit-chat/) and [OpenAI API](https://openai.com/api/)'s 
the most capable GPT-3.5 model [gpt-3.5-turbo](https://platform.openai.com/docs/models/overview) for educational purposes. 
"""
)

st.sidebar.markdown(
    "[Streamlit](https://streamlit.io) is a Python library that allows the creation of interactive, data-driven web applications in Python."
)

st.sidebar.header("Additional Resources")
st.sidebar.markdown(
    """
- [My Github Repo](https://github.com/RoshiniFernando/Heli)
- [Tutorial I followed](https://dragonforest.in/chat-gpt-3-web-app-with-streamlit/)

"""
)

st.sidebar.header("Change Log")
st.sidebar.markdown(
    """
- Current Heli 2.0 powered by OpenAI (ChatGPT) gpt-3.5-turbo model
- Heli 1.0 powered by OpenAI text-davinci-003 model

"""
)

# Pass API Key
openai.api_key = API_KEY

# Create function to use OpenAI gpt-3.5-turbo model
def generate_response(prompt):
    # completion=openai.Completion.create(
    #     engine='gpt-3.5-turbo',
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.8,
    # )

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": prompt}
    ]
    )

    messages=completion['choices'][0]['message']['content']
    print(messages)
    return messages

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

    

