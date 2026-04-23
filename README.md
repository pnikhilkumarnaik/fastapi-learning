# fastapi-learning
# 🚀 FastAPI Learning Project

A backend API built using **FastAPI** and deployed on Render.

---

## 🌐 Live API

🔗 https://fastapi-learning-psvg.onrender.com/

---

## 📚 API Documentation

* Swagger UI:
  https://fastapi-learning-psvg.onrender.com/docs

* ReDoc:
  https://fastapi-learning-psvg.onrender.com/redoc

---

## 📌 Features

* FastAPI framework
* Modular structure (routers, schemas)
* Authentication system
* Blog and User APIs
* RESTful endpoints
* Deployed on Render

---

## 📁 Project Structure

```
app/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── routers/
│     ├── authentication.py
│     ├── blog.py
│     ├── user.py

requirements.txt
README.md
```

---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository

```
git clone https://github.com/pnikhilkumarnaik/fastapi-learning.git
cd fastapi-learning
```

---

### 2. Create virtual environment

```
python -m venv venv
```

Activate it:

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
DATABASE_URL=sqlite:///./blog.db
```

---

## 🚀 Deployment (Render)

* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## 📸 Screenshots

### 🔹 API Home
![API Home](images/fapi1.PNG)

### 🔹 Swagger UI
![Swagger UI](images/fapi2.PNG)

### 🔹 API Response
![API Response](images/fapi3.PNG)

## 🛠️ Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Uvicorn

---

## 👨‍💻 Author

**Nikhil Kumar Naik**
GitHub: https://github.com/pnikhilkumarnaik

---

## ⭐ Future Improvements

* PostgreSQL integration
* JWT authentication enhancement
* Docker support
* CI/CD pipeline
* Frontend integration
