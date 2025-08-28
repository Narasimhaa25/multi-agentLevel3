# multi-agentLevel3


Level 3 — LLM + Multi-Step Tool Use (Full Agentic AI)

This project is the third level of a multi-stage AI assignment. At this level, we extend the LLM + single-tool chatbot from Level 2 into a multi-step agentic system.

The focus here is on multi-step reasoning and tool chaining:
	•	The agent breaks complex queries into multiple sub-tasks.
	•	Sub-tasks are delegated to the correct tool (calculator, translator) or directly answered by the LLM.
	•	Multiple steps can be executed in sequence (e.g., translate → calculate, or calculate → LLM).
	•	The chatbot maintains execution order and memory across steps.
	•	All interactions are logged with a timestamp for history.

⸻

🔹 Setup and Installation
	1.	Ensure you have Python 3.9 or higher installed.
	2.	Clone this repository and navigate to the level3 directory.
	3.	Install dependencies:

 pip install -r ../requirements.txt

 The requirements.txt includes:


 google-generativeai
python-dotenv


4.create .env file in the same directory with your Gemini api key:

 GEMINI_API_KEY=your_api_key_here


 ▶️ Running the Multi-Step Agent

Start the chatbot with multi-step tool support by running:

python full_agent.py



You: Translate 'Good Morning' into German and then multiply 5 and 6
Bot: Guten Morgen
Result: 30

You: Add 10 and 20, then translate 'Have a nice day' into German
Bot: Result: 30
Einen schönen Tag noch

You: Tell me the capital of Italy, then multiply 12 and 12
Bot: Rome
Result: 144

You: Translate 'Sunshine' into German
Bot: Sonnenschein

You: Add 2 and 2 and multiply 3 and 3
Bot: Result: 4
Result: 9

You: What is the distance between Earth and Mars?
Bot: The distance between Earth and Mars is constantly changing because both planets are orbiting the Sun at different speeds and distances.  There's no single answer.

At their closest approach (a phenomenon called "opposition"), Earth and Mars can be approximately **54.6 million kilometers (33.9 million miles)** apart.  At their furthest, they can be over **401 million kilometers (249 million miles)** apart.


