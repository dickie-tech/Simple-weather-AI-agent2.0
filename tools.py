import os
import json
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_weather(lat: float, lon: float):
    weather_key = os.getenv("OPENWEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": weather_key, "units": "metric"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return json.dumps(
            {
                "location": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "weather": data["weather"][0]["description"],
            }
        )
    except Exception as e:
        return json.dumps({"error": str(e)})


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather using latitude and longitude",
            "parameters": {
                "type": "object",
                "additionalProperties": False,
                "properties": {"lat": {"type": "number"}, "lon": {"type": "number"}},
                "required": ["lat", "lon"],
            },
            "strict": True,
        },
    },
]
messages = [{"role": "user", "content": "What is the weather in Nyeri?"}]
response = client.chat.completions.create(
    model="gpt-5-nano", messages=messages, tools=tools
)
response_message = response.choices[0].message

if response_message.tool_calls:
    tool_call = response_message.tool_calls[0]

    function_name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)

    if function_name == "get_weather":
        lat = args["lat"]
        lon = args["lon"]

        result = get_weather(lat, lon)
    else:
        result = "No tool execution needed"

    messages.append(response_message)

    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": function_name,
            "content": result,
        }
    )
    final_response = client.chat.completions.create(
        model="gpt-5-nano", messages=messages, tools=tools
    )

    print("Final Response:", final_response.choices[0].message.content)
