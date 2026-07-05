import json, os

PROFILE_PATH = "data/profile.json"

def get_current_user():
    if not os.path.exists(PROFILE_PATH):
        raise RuntimeError("No profile found — run setup_wizard.py first")
    with open(PROFILE_PATH) as f:
        return json.load(f)