"""Mock authentication for testing purposes.
the real will be implemented against the SSO provider, 
and will return a user object with the following attributes:
- id: a unique identifier for the user"""


from dataclasses import dataclass

@dataclass
class MockUser:
    id: str = "test-user-1"
    role: str = "analyst"
    allowed_domains: list = None

    def __post_init__(self):
        if self.allowed_domains is None:
            self.allowed_domains = ["finance"]

def get_current_user():
    return MockUser()