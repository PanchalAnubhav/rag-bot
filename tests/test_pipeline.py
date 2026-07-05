import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from backend.stages.router import classify
result = classify("What's our Q3 revenue vs industry average?", "analyst", ["finance"])
print(result)