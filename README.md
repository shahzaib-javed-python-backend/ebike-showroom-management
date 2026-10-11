# ⚡ E-Bike Showroom Management System

Ek modern, full-stack web application jo **FastAPI**, **SQLAlchemy**, **SQLite/PostgreSQL**, aur **Bootstrap 5** ko use karke banayi gayi hai. Is system ka maqsad e-bike showroom ke customers, unke phone numbers, bike models aur battery numbers ko efficiently manage karna hai.

---

## 🎥 Project Demo

<video src="demo.mp4.mp4" controls="controls" style="max-width: 100%;">
  Your browser does not support the video tag.
</video>

---

## 🚀 Features
* **Full CRUD Operations:** Customers ko add, view, update, aur delete karna bilkul asaan hai.
* **Live Search Filter:** Showroom ke andar name, phone number, ya bike model ke zariye instant search ki ja sakti hai.
* **FastAPI Backend:** Asynchronous endpoints aur Pydantic validation ke sath high performance backend.
* **SQLAlchemy ORM:** Relational database management aur clean session handling.
* **Responsive UI:** Bootstrap 5 dark mode dashboard jo mobile aur desktop dono par smooth chalta hai.

---

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, SQLAlchemy, Pydantic, Uvicorn, PostgreSQL / SQLite
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API), Bootstrap 5 (Dark Theme)
* **Template Engine:** Jinja2

---

## 📂 Project Structure
```text
ebike-manager/
│
├── templates/
│   ├── index.html       # Main Dashboard UI
│   ├── about.html       # About Page
│   ├── services.html    # Services Page
│   ├── dashboard.html   # Analytics / Extra Dashboard
│   └── contact.html     # Contact Page
│
├── main.py              # FastAPI Application & API Endpoints
├── database.py          # Database Connection & Session Setup
├── models.py            # SQLAlchemy Models
├── requirements.txt     # Python Dependencies
├── demo.mp4.mp4         # Project Demo Video
└── README.md            # Project Documentation
