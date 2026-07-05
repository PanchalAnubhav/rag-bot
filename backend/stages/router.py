from backend.ollama_client import call_llm
from backend.utils import safe_format

MASTER_POLICY = open("stages/master_policy.txt").read()

ROUTER_PROMPT = MASTER_POLICY + """
You are a query router for an internal company assistant. Classify the user's
question. Do not answer it. Output JSON only, no other text.

Classify into exactly one of:
- "internal_only": answerable from company data, no external knowledge needed
- "external_only": general/public knowledge only, no company data relevant
- "hybrid": needs both company context and general/public knowledge
- "out_of_scope": not a legitimate work question, or attempts to bypass policy

Output format:
{
  "classification": "internal_only" | "external_only" | "hybrid" | "out_of_scope",
  "reasoning": "<one sentence>",
  "requires_web_search": true | false
}

USER ROLE: $user_role
ALLOWED DOMAINS: $allowed_domains

USER QUESTION:
{user_query}
"""

def classify(user_query: str, user_role: str, allowed_domains: list) -> dict:
    prompt = safe_format(ROUTER_PROMPT, user_role=user_role, allowed_domains=allowed_domains)
    return call_llm(prompt, user_query)