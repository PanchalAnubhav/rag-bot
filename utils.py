class SafeDict(dict):
    def __missing__(self, key):
        return f"{{{key}}}"  # leaves placeholder visible if truly missing, easier to debug

def safe_format(template: str, **kwargs) -> str:
    return template.format_map(SafeDict(**kwargs))