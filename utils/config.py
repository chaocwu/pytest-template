from dataclasses import dataclass


@dataclass
class GitCodeConfig:
    base_url: str
    owner: str
    access_token: str
