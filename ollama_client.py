import ollama, json, os
from dotenv import load_dotenv
load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL")

def call_llm(system_prompt: str, user_content: str, json_mode: bool = True) -> dict:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        format="json" if json_mode else None,
        options={"temperature": 0.1},
    )
    content = response["message"]["content"]
    return json.loads(content) if json_mode else content