from config import Config
from message import Message
from publisher import KafkaPublisher
from consumer import KafkaConsumerClient
import threading
import time


def message_handler(message: Message):
    print(f"Received: {message.id} - {message.payload}")


def main():

    # Publisher Example
    publisher = KafkaPublisher(Config)

    # Publish some messages
    messages = [
        Message("1", Config.topics[0], {"user_id": 123, "amount": 99.99}),
        Message("2", Config.topics[0], {"user_id": 456, "amount": 149.99})
    ]

    for msg in messages:
        publisher.publish(msg)

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
        publisher.close()
        consumer.close()


if __name__ == "__main__":
    main()