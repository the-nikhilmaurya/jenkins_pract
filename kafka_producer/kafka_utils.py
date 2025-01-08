from confluent_kafka import Producer

def create_kafka_producer():
    return Producer({'bootstrap.servers': 'localhost:9092'})

def produce_event(topic, key, message):
    producer = create_kafka_producer()
    try:
        producer.produce(topic, key=key, value=message)
        producer.flush()
        return {"status": "success", "message": "Event produced successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
