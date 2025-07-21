from kafka import KafkaProducer

from config import Config
from message import Message, SendingConfig


class KafkaPublisher:
    def __init__(self, config):
        self.producer = KafkaProducer(bootstrap_servers=config.bootstrap_servers,  # Now handles List[str]
                                      client_id=f"{config.client_id}-producer",
                                      value_serializer=lambda v: v.encode('utf-8'), acks='all', # Wait for all replicas
                                      retries=3, retry_backoff_ms=100)

    def publish(self, message: Message) -> bool:
        try:
            self.producer.send(topic=message.sending_config.topic, value=message.to_json(), partition=message.sending_config.partition)
            self.producer.flush()
            print(f"Published: {message.id} {message.payload} to {message.sending_config.topic}")
            return True
        except Exception as e:
            print(f"Error publishing: {e}")
            return False

    def close(self):
        self.producer.close()
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Kafka Publisher with dynamic user_id prefix")
    parser.add_argument("user_prefix", type=str, help="Prefix for user_id (e.g., clientA)")
    parser.add_argument("topic_index", type=int, default=0, help="topic index (default: 0) i.e. [default-topic, second-topic, third-topic]")
    parser.add_argument("--count", type=int, default=50000, help="Number of messages to publish (default: 50000)")
    args = parser.parse_args()

    # Publisher Example
    publisher = KafkaPublisher(Config)

    # Publish some messages
    for i in range(args.count):
        partition = int(i % 2==0)
        sending_config = SendingConfig(
            topic=Config.topics[args.topic_index],
            partition=partition
        )
        # Round-robin partitioning
        publisher.publish(Message(
            id=str(i),
            sending_config=sending_config,
            payload={"user_id": f"{args.user_prefix}_{i}", "item_id": i, "amount": i * 10.0}))
    publisher.close()
