from dataclasses import dataclass
from typing import List


@dataclass
class ConfigKafka:
    bootstrap_servers: List[str] = None
    client_id: str = 'kafka-client'
    group_id: str = 'default-group'
    topics: List[str] = None

    def __post_init__(self):
        if self.bootstrap_servers is None:
            self.bootstrap_servers = ['localhost:9092']
        if self.topics is None:
            self.topics = ['default-topic','second-topic','third-topic']


Config = ConfigKafka()