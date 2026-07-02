from stages.router import classify

result = classify("What's our Q3 revenue vs industry average?", "analyst", ["finance"])
print(result)