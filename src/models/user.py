from dataclasses import dataclass
from models.default import DefaultModel


@dataclass
class User(DefaultModel):
    login: str
    email: str
    name: str
    surname: str
    password: str
