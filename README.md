# Apache Kafka Demo Project

A demonstration project showcasing Apache Kafka messaging system implementation using Python. This project implements a publisher-consumer pattern using Apache Kafka 4.0.

## Features

- Kafka Publisher (Producer) implementation
- Kafka Consumer implementation
- Configurable message handling
- Docker-based setup for easy deployment
- KRaft mode configuration (No ZooKeeper dependency)

## Prerequisites

- Docker and Docker Compose
- Python 3.8 or higher
- Apache Kafka 4.0
- pip (Python package manager)

## Project Structure

```
apache-kafka-demo/
  ├── app/
  │   ├── __init__.py
  │   ├── config.py      # Configuration settings
  │   ├── consumer.py    # Kafka consumer implementation
  │   ├── main.py        # Application entry point
  │   ├── message.py     # Message models
  │   └── publisher.py   # Kafka publisher implementation
  └── docker-compose.yml # Docker configuration
```

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd apache-kafka-demo
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Kafka cluster using Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Configuration

The project uses environment variables for configuration. Create a `.env` file in the `app` directory with the following variables:

```env
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC=your_topic_name
```

## Usage

1. Start the consumer:
   ```bash
   python -m app.consumer
   ```

2. In a separate terminal, run the publisher:
   ```bash
   python -m app.publisher
   ```

3. The main application can be run with:
   ```bash
   python -m app.main
   ```

## Key Features of Kafka 4.0

- KRaft (Kafka Raft) mode enabled by default
- No ZooKeeper dependency
- Improved scalability and performance
- Enhanced security features
- Simplified cluster management

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Apache Kafka documentation
- Python Kafka client libraries
- Docker and Docker Compose documentation 
