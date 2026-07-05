import json
from datetime import datetime

def log_entry(user, question, router_result, filter_result):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": getattr(user, "id", "unknown"),
        "user_role": user.role,
        "original_query": question,
        "classification": router_result.get("classification"),
        "filter_action": filter_result.get("action"),
        "final_answer_released": filter_result.get("action") != "block_and_escalate",
    }
    with open("logs/audit_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")