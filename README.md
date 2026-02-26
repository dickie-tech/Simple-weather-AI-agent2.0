Weather AI Agent 2.0

An intelligent AI-powered weather assistant that combines real-time weather data from OpenWeather API with natural language responses generated using OpenAI.

This project demonstrates:

🔧 Tool-calling AI architecture

🌍 External API integration

🔐 Secure environment variable handling

🧠 Autonomous reasoning workflow

🚀 Live Concept

User asks:

“What’s the weather in Nyeri?”

System flow:

AI detects weather intent

Calls get_weather tool

Fetches real-time data from OpenWeather

Returns structured weather data

OpenAI generates a natural response

AI replies:

“The current temperature in Nyeri is 18°C with light rain and moderate humidity.”

🧠 System Architecture

Below is the simplified architecture of the agent:

User Input
    │
    ▼
OpenAI Model (Reasoning + Tool Detection)
    │
    ├── If weather needed → Call get_weather tool
    │
    ▼
OpenWeather API (External Data Source)
    │
    ▼
Weather JSON Response
    │
    ▼
OpenAI Model (Generates Natural Language Reply)
    │
    ▼
Final AI Response to User


This is a tool-calling agent pattern, commonly used in production AI systems.

🛠 Tech Stack

Python 3.10+

OpenAI SDK

OpenWeather API

Requests

python-dotenv

Git & GitHub (secure workflow)

📂 Project Structure
Weather2.0/
│
├── tools.py              # Main AI agent logic
├── requirements.txt      # Dependencies
├── .gitignore            # Prevents secrets from being committed
├── .env                  # Local API keys (NOT committed)
└── README.md

🔑 Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/weather-ai-agent.git
cd weather-ai-agent

2️⃣ Create Virtual Environment
python -m venv .venv


Activate:

Windows

.\.venv\Scripts\activate


Mac/Linux

source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create .env file:

OPENAI_API_KEY=your_openai_key
OPENWEATHER_API_KEY=your_openweather_key


⚠️ This file is excluded via .gitignore.

▶️ Run the Project
python tools.py

🔒 Security & Best Practices

API keys stored in .env

.env excluded from Git

No secrets committed to repository

Follows GitHub Push Protection standards

📈 Engineering Highlights

This project demonstrates:

✅ AI Tool Calling Architecture
✅ External API Orchestration
✅ Secure Key Management
✅ Modular Code Design
✅ Clean Git Workflow
✅ Production-style Agent Loop

🔮 Future Improvements

🌍 City → Coordinate auto-conversion

🧠 Multi-tool agent (weather + calculator + news)

💬 Web-based chatbot interface (Flask/FastAPI)

☁️ Cloud deployment (Render / Railway / AWS)

🧠 Conversation memory system

📊 Logging & monitoring system

🏗 Production Evolution Roadmap
Stage	Feature
v1	Basic tool-calling weather agent
v2	Multi-tool autonomous agent
v3	Web app deployment
v4	Cloud-hosted AI microservice
v5	Scalable AI product
📜 License

MIT License — Free to use for learning and portfolio projects.

👨‍💻 Author

Built as part of an AI Engineering learning journey focused on:

AI Systems

Tool-Oriented Agents

Production-Level Architecture

DevOps & Secure Workflows
