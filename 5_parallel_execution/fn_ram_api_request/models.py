from dataclasses import dataclass
from typing import Dict, List, Literal, Optional
from datetime import datetime, timezone


@dataclass
class CharacterSchema:
    id: int
    name: str
    status: Literal["Alive", "Dead", "unknown"]
    species: str
    type: str
    gender: Literal["Female", "Male", "Genderless", "unknown"]
    origin: Dict[str, str]
    location: Dict[str, str]
    image: str
    episode: List[str]
    url: str
    created: datetime

    def __post_init__(self):
        self.created = datetime.strptime(self.created, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
            tzinfo=timezone.utc
        )


@dataclass
class ApiInfo:
    count: int
    pages: int
    next: Optional[str]
    prev: Optional[str]


@dataclass
class ApiResponse:
    info: ApiInfo
    results: List[CharacterSchema]

    def __post_init__(self):
        self.info = ApiInfo(**self.info)
        self.results = [CharacterSchema(**x) for x in self.results]


@dataclass
class ApiParameters:
    page: Optional[str] = None
    name: Optional[str] = None
    status: Optional[Literal["alive", "dead", "unknown"]] = None
    species: Optional[str] = None
    type: Optional[str] = None
    gender: Optional[Literal["female", "male", "genderless", "unknown"]] = None
