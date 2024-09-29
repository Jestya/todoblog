from dataclasses import dataclass

from models.default import DefaultModel


@dataclass
class Category(DefaultModel):
    title: str
