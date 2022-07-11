import dataclasses
from typing import List
from uuid import UUID

FilePath = str


@dataclasses.dataclass
class Object:
    name: str


@dataclasses.dataclass
class Data:
    uid: UUID
    level: int
    objects: List[Object]
