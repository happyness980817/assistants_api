from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st
import time

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

if 'thread_id' not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

THREAD_ID = st.session_state.thread_id 
# THREAD_ID = 'thread_W23yHaxNItZBfPWmIdlx3W1b'
ASSISTANT_ID = 'asst_giiV8gCJ0nXYNt55AeeLH63P'


thread_messages = client.beta.threads.messages.list(THREAD_ID, order='asc')

st.header('현진건 작가 챗봇 - 운수 좋은 날')

for message in thread_messages.data:
    with st.chat_message(message.role):
        st.write(message.content[0].text.value)
    
prompt = st.chat_input("소설에 관해 질문하세요.")
if prompt:
    message = client.beta.threads.messages.create(
    thread_id=THREAD_ID,
    role="user",
    content=prompt
)
    with st.chat_message(message.role):
        st.write(message.content[0].text.value)

    run = client.beta.threads.runs.create(
    thread_id=THREAD_ID,
    assistant_id=ASSISTANT_ID,
    )

    with st.spinner('답변 생성중...'):       
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(
                thread_id = THREAD_ID,
                run_id = run.id
            )
    messages_list = client.beta.threads.messages.list(
        thread_id=THREAD_ID
    )
    with st.chat_message(messages_list.data[0].role):
        st.write(messages_list.data[0].content[0].text.value)

