from fastapi import FastAPI, Depends
from stages import router, sanitizer, generator, output_filter
from vector_store import query as vector_query
from audit import log_entry
from auth import get_current_user  # you'll build this against your SSO
from backend.search import search_web

app = FastAPI()

@app.post("/chat")
async def chat(question: str, user=Depends(get_current_user)):
    r = router.classify(question, user.role, user.allowed_domains)

    web_results = None
    if r.get("requires_web_search"):
        s = sanitizer.sanitize(question, user.role)
        if not s["cannot_sanitize"] and s["confidence"] != "low":
            web_results = search_web(s["sanitized_query"])

    context = vector_query(question, user.allowed_domains) if r["classification"] != "external_only" else None
    draft = generator.generate(question, context, web_results, user)
    checked = output_filter.check(draft, user)

    log_entry(user, question, r, checked)
    return {"answer": checked["redacted_answer"] if checked["action"] != "block_and_escalate" else "I'm not able to answer that from available data."}