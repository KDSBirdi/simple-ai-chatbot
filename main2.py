import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import json

#just to hide the token and store it in json file and accessing the token from json file
with open('credentials.json', 'r') as f:
    file = json.load(f)
    token = file['token']

#function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response
#function to recieve user queries
def get_text():
    input_text=st.text_input("MY bot: ",key="input")
    return input_text
#title of the steamlit app
st.title('personal tutoring bot')

#url='"

changes = '''
<style>
[data-testid="stAppViewContainer"]
    {
    background-image:url('https://wallpaperaccess.com/full/1244405.jpg');
    background-size:cover;
    }

</style>
'''
st.markdown(changes, unsafe_allow_html=True)
print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

#accepting user input
user_input=get_text()
if user_input:
    print(user_input)
    output=generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['generated'][i],key=str(i))
        message(st.session_state['past'][i], key="user_"+str(i),is_user=True)
