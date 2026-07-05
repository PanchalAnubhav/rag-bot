from string import Template

def safe_format(template: str, **kwargs) -> str:
    return Template(template).safe_substitute(**kwargs)