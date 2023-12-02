from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

ASSISTANT_ID = "asst_8JqsfDVmarxqrzPS1SFOo9PZ"
THREAD_ID = "thread_fFyNHULCSv1qhtPSlVP5pajC"
MESSAGE_ID = "msg_SMQqJCyPPj8A988czWBftEwE"
RUN_ID = "run_QszELhSRWY58Y9SumIWJlYta"

# assistant = client.beta.assistants.create(
#     name="Math Tutor",
#     instructions="You are a personal math tutor. Write and run code to answer math questions.",
#     tools=[{"type": "code_interpreter"}],
#     model="gpt-4-1106-preview"
# )

# print(assistant)

# thread = client.beta.threads.create()
# print(thread)

# msg_SMQqJCyPPj8A988czWBftEwE
# message = client.beta.threads.messages.create(
#     thread_id="thread_fFyNHULCSv1qhtPSlVP5pajC",
#     role="user",
#     content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
# )
# print(message)

# run = client.beta.threads.runs.create(
#   thread_id=THREAD_ID,
#   assistant_id=ASSISTANT_ID,
#   instructions="Please address the user as Jane Doe. The user has a premium account."
# )
# print(run)

# run = client.beta.threads.runs.retrieve(
#   thread_id=THREAD_ID,
#   run_id=RUN_ID
# )
# print(run)

messages = client.beta.threads.messages.list(
  thread_id=THREAD_ID
)
print(messages.data[0].content[0].text.value)