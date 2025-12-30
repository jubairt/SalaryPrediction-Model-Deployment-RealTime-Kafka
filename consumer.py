from kafka import KafkaConsumer
import json
import joblib
import numpy as np
import pandas as pd

model = joblib.load("model.pkl")

consumer = KafkaConsumer(
    "salary-topic",
    bootstrap_servers="localhost:9092",
    group_id="salary-group",
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Consumer started...")

for msg in consumer:
    years = msg.value["years_experience"]
    input_data = pd.DataFrame([[years]], columns=["YearsExperience"])
    salary = model.predict(input_data)[0]

    print("Years:", years, "Salary:", round(salary, 2))
