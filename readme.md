# 🏡 House Price Predictor – Inference API

This is the backend inference service for the **House Price Predictor** project. It exposes a simple REST API built with **FastAPI** that takes in property details and returns the predicted house price using a pre-trained machine learning model.

---

## 🔧 Tech Stack

- Python 3.11+
- FastAPI
- scikit-learn
- Uvicorn (ASGI server)
- Pickle (`model.pkl` and `features.pkl`)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ranesh1104/house_price_predictor_inference.git
cd house_price_predictor_inference
```

### 2. Install Dependencies
 
```bash
pip install -r requirements.txt
```

### 3. Start the API Server
```bash
uvicorn inference:app --host 0.0.0.0 --port 8000
```

Once the server is running, you can visit:

Docs: http://localhost:8000/docs

### 🧠 How It Works
model.pkl – Your trained machine learning model.

features.pkl – A list of feature names used during training to ensure consistent ordering at inference time.

inference.py – Contains the FastAPI app with a /predict endpoint.

#### 🔌 Endpoint
POST /predict

Example request payload:

```bash
{
  "area": 1200,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 1,
  "mainroad": "yes",
  "guestroom": "no",
  "basement": "no",
  "hotwaterheating": "no",
  "airconditioning": "yes",
  "parking": 1,
  "prefarea": "no",
  "furnishingstatus": "semi-furnished"
}
```
Example response:
```bash
{
  "predicted_price": 752345.67
}
```
### 🧪 Testing the API
You can use tools like:

Postman

Insomnia

curl in your terminal

Or the built-in Swagger UI at http://localhost:8000/docs

### 🛠️ Deployment (e.g. Render, Railway, etc.)
If deploying to a platform like Render:

Make sure uvicorn is in your requirements.txt.

Set your Start Command to:

```bash
uvicorn inference:app --host 0.0.0.0 --port 10000
```
(or whatever port your service uses)

### 📁 Project Structure
```bash
├── inference.py             # FastAPI app
├── model.pkl                # Trained model
├── features.pkl             # List of features used during training
├── requirements.txt         # Dependencies
├── house-pricing-regression.ipynb # Original notebook (optional)
```

### 🙌 Acknowledgements
Built with ❤️ using FastAPI and scikit-learn



