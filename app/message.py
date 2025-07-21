import json
from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass()
class SendingConfig:
    topic: str = 'default-topic'
    partition: int = 0

@dataclass
class Message:
    id: str
    sending_config: SendingConfig
    payload: Dict[str, Any]

    def to_json(self) -> str:
        return json.dumps(asdict(self))  # ✅ Handles nested dataclasses

    @classmethod
    def from_json(cls, json_str: str) -> 'Message':
        data = json.loads(json_str)
        return cls(**data)