# 📊 Real-Time Salary Prediction using Kafka (Streaming ML Inference)

This project demonstrates **real-time machine learning inference** using **Apache Kafka** with a **Linear Regression model**.  
Instead of calling a REST API, predictions are generated **continuously** as data streams in.

The system simulates live input (`years_experience`) sent to Kafka, consumes the data in real time, and produces salary predictions using a trained ML model.

This project focuses on:
- Event-driven ML inference
- Kafka producer–consumer pattern
- Model consistency between training and inference
- Local Kafka setup using Docker (no cloud required)

---

## 🚀 Key Features

- Trained **Linear Regression** model using scikit-learn
- **Kafka Producer** sends streaming experience data
- **Kafka Consumer** performs real-time predictions
- **Docker Compose** for easy Kafka + Zookeeper setup
- Clean, minimal, beginner-friendly code
- Industry-relevant streaming ML architecture

---

## 🧠 How the Model Works (Brief)

- Input feature: `YearsExperience`
- Output: `Predicted Salary`
- Model trained using historical salary data
- Same feature format is used during inference to avoid schema mismatch

---

## 🧪 Prerequisites

Make sure you have the following installed:

- Python **3.10+**
- Docker
- Docker Compose
- Git (optional)

---

## 📦 Python Dependencies

Install all required Python packages:

```powershell
pip install -r requirements.txt
```

---

## 🐳 Step-by-Step: Running the Project

### Start Kafka and Zookeeper

```powershell
docker-compose up
```
- Wait 20–30 seconds until Kafka finishes starting.
- Leave this terminal running.

### Step 3: Start the Kafka Consumer

In a new terminal, run:
```powershell
python consumer.py
```

### Start the Kafka Producer

In another terminal, run:
```powershell
python producer.py
```

## ✅ Conclusion

This project successfully demonstrates how a traditional machine learning model can be extended into a **real-time, event-driven inference system** using **Apache Kafka**.

By integrating Kafka with a trained Linear Regression model, we moved beyond request-based predictions and implemented **continuous streaming inference**, where incoming data is processed and predicted instantly. Running Kafka locally with Docker allowed for fast experimentation while still following **industry-standard streaming patterns**.

Overall, this project provides a strong foundation in **real-time ML system design** and mirrors how modern machine learning models are deployed in production environments. It serves as an excellent stepping stone toward building large-scale, cloud-native streaming ML applications.

