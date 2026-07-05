from backend.ollama_client import call_llm

MASTER_POLICY = open("stages/master_policy.txt").read()

ROUTER_PROMPT = MASTER_POLICY + """
You are a query sanitizer. You will rewrite an internal question into a generic,
public-safe search query. You must strip:
- Company name, product names, internal codenames
- Employee names, client names, partner names
- Financial figures, internal metrics, project identifiers
- Any term appearing in this sensitive-terms list: {sensitive_terms_list}

Rewrite the query so it captures the general knowledge need only. If the question
cannot be sanitized without losing all meaning (i.e. it is inherently about internal
data), output "cannot_sanitize": true instead of a rewritten query.

Output format:
{
  "sanitized_query": "<generic search string, or empty if cannot_sanitize>",
  "cannot_sanitize": true | false,
  "terms_removed": ["<term1>", "<term2>", ...],
  "confidence": "high" | "medium" | "low"
}

Rule: if terms_removed has 3 or more entries, set confidence to "low" — this signals
the calling system to route this query to human review before it is sent externally.

ORIGINAL QUESTION:
{user_query}
"""

def classify(user_query: str, user_role: str, allowed_domains: list) -> dict:
    prompt = ROUTER_PROMPT.format(user_role=user_role, allowed_domains=allowed_domains)
    return call_llm(prompt, user_query)