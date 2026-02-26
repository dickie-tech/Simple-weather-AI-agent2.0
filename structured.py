import os
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


response = client.beta.chat.completions.parse(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    response_format=CalendarEvent,
)

event = response.choices[0].message.parsed
print("Event Name:", event.name)
print("Event Date:", event.date)
print("Participants:", event.participants)
