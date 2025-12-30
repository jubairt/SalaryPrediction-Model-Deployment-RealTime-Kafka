from kafka import KafkaProducer
import json
import time

years_list = [1, 2, 3, 5, 7, 10]

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

for years in years_list:
    data = {"years_experience": years}
    producer.send("salary-topic", data)
    print("Sent:", data)
    time.sleep(3)
