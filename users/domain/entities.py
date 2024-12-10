from dataclasses import dataclass

@dataclass
class UserEntity:
    username: str
    email: str
    password: str
    first_name: str = ''
    last_name: str = ''
    telephone: str = ''
    country: str = ''