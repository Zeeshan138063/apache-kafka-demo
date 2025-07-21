import random
import socket
import threading
import time
from typing import Callable, List

from kafka import KafkaConsumer

from config import Config
from message import Message


class KafkaConsumerClient:
    def __init__(self, config):
        unique_id = f"{config.client_id}-{socket.gethostname()}-{random.randint(1000, 9999)}"

        self.consumer = KafkaConsumer(bootstrap_servers=config.bootstrap_servers,  # Now handles List[str]
                                      group_id=config.group_id, client_id=unique_id,
                                      value_deserializer=lambda m: m.decode('utf-8'), auto_offset_reset='latest',
                                      enable_auto_commit=True, session_timeout_ms=30000, heartbeat_interval_ms=3000)

    def subscribe(self, topics: List[str]):
        self.consumer.subscribe(topics)
        print(f"Subscribed to: {topics}")

    def consume(self, handler: Callable[[Message], None]):
        print(f"Starting to consume messages... {self.consumer.config.get('client_id')}")
        for kafka_msg in self.consumer:
            try:
                message = Message.from_json(kafka_msg.value)
                handler(message)
            except Exception as e:
                print(f"Error processing message: {e}")

    def close(self):
        self.consumer.close()


def message_handler(message: Message):
    print(f"Received: {message.id} - {message.payload}")


if __name__ == '__main__':
    # Consumer Example
    consumer = KafkaConsumerClient(Config)
    consumer.subscribe(Config.topics)

    # Run consumer in background
    consumer_thread = threading.Thread(target=consumer.consume, args=(message_handler,))
    consumer_thread.daemon = True
    consumer_thread.start()

    # Keep running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

        consumer.close()
