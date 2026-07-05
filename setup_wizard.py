import subprocess, json, os

print("Setting up your private assistant. Nothing here leaves this machine.\n")

model = input("Model to use [qwen2.5:7b-instruct-q4_K_M]: ") or "qwen2.5:7b-instruct-q4_K_M"
subprocess.run(["ollama", "pull", model])
subprocess.run(["ollama", "pull", "nomic-embed-text"])

domains_input = input("Personal " \
"domains to track (comma-separated) [finance,journal,notes]: ") or "finance,journal,notes"
domains = [d.strip() for d in domains_input.split(",")]

os.makedirs("data", exist_ok=True)
with open("data/profile.json", "w") as f:
    json.dump({"id": "local-user", "role": "owner", "allowed_domains": domains}, f)

with open(".env", "w") as f:
    f.write(f"OLLAMA_MODEL={model}\nOLLAMA_HOST=http://localhost:11434\nCHROMA_PATH=./data/chroma_db\nSQLITE_PATH=./data/personal.db\n")

print("\nDone. Drop files into ./import/ then run ingestion, or start the app directly.")