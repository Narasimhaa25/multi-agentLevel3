import re
import os
from dotenv import load_dotenv
import google.generativeai as genai
from calculator_tool import calculate
from translator_tool import translate_to_german
from datetime import datetime   # 🔹 for timestamps

# -------------------------------
# 🔹 Load API Key
# -------------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

LOG_FILE = "interaction_logs.txt"   # 🔹 Log file path


# -------------------------------
# Translation Task Detector
# -------------------------------
def detect_translation_task(user_input: str):
    match = re.search(r"translate '(.*?)' into (\w+)", user_input, re.IGNORECASE)
    if match:
        phrase, language = match.groups()
        return phrase, language.lower()
    return None, None


# -------------------------------
# Math Task Detector
# -------------------------------
def detect_calculations(user_input: str):
    patterns = [
        (r"add (\d+) and (\d+)", "add"),
        (r"subtract (\d+) and (\d+)", "subtract"),
        (r"multiply (\d+) and (\d+)", "multiply"),
        (r"divide (\d+) and (\d+)", "divide"),
    ]
    results = []

    for pattern, operation in patterns:
        matches = re.findall(pattern, user_input, re.IGNORECASE)
        for m in matches:
            results.append((operation, int(m[0]), int(m[1])))

    return results


# -------------------------------
# LLM Fallback
# -------------------------------
def llm_answer(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error calling Gemini API: {e}"


# -------------------------------
# Main Agent (Step-wise Execution)
# -------------------------------
def agent(user_input: str):
    responses = []

    # 🔹 Step 1: Split into sub-tasks
    steps = re.split(r"\bthen\b", user_input, flags=re.IGNORECASE)

    for step in steps:
        step = step.strip()
        if not step:
            continue

        # 🔹 Translation
        phrase, language = detect_translation_task(step)
        if phrase:
            if language == "german":
                responses.append(translate_to_german(phrase))
            else:
                responses.append(f"Error: Only German translation is supported (got {language}).")
            continue

        # 🔹 Math
        calculations = detect_calculations(step)
        if calculations:
            for op, n1, n2 in calculations:
                res = calculate(op, n1, n2)
                responses.append(res)
            continue

        # 🔹 Otherwise → ask LLM
        responses.append(llm_answer(step))

    final_response = "\n".join(responses)
    return final_response


# -------------------------------
# Save logs to file with timestamp
# -------------------------------
def save_log(user_input: str, bot_response: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] You: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_response}\n")
        f.write("-" * 60 + "\n")   # separator


# -------------------------------
# CLI Runner
# -------------------------------
def run_cli():
    print("🤖 Full Agentic AI (Dynamic Multi-Step) with Gemini. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = agent(user_input)
        print(f"Bot: {response}\n")

        # 🔹 Save to logs
        save_log(user_input, response)


if __name__ == "__main__":
    run_cli()