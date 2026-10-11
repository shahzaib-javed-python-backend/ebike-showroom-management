# ⚡ E-Bike Showroom Management System

Ek modern, full-stack web application jo **FastAPI**, **SQLAlchemy**, **SQLite**, aur **Bootstrap 5** ko use karke banayi gayi hai. Is system ka maqsad e-bike showroom ke customers, unke phone numbers, bike models aur battery numbers ko efficiently manage karna hai.

---

## 🚀 Features
* **Full CRUD Operations:** Customers ko add, view, update, aur delete karna bilkul asaan hai.
* **Live Search Filter:** Showroom ke andar name, phone number, ya bike model ke zariye instant search ki ja sakti hai.
* **FastAPI Backend:** Asynchronous endpoints aur Pydantic validation ke sath high performance backend.
* **SQLAlchemy ORM:** Relational database management aur clean session handling.
* **Responsive UI:** Bootstrap 5 dark mode dashboard jo mobile aur desktop dono par smooth chalta hai.

---

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, SQLAlchemy, Pydantic, Uvicorn, SQLite
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
└── README.md            # Project Documentation
Installation & Running Locally
Apne local system par project chalane ke liye yeh steps follow karein:

Clone the Repository:
git clone [https://github.com/shahzaib-javed-python-backend/ebike-showroom-management.git](https://github.com/shahzaib-javed-python-backend/ebike-showroom-management.git)
cd ebike-manager
Install Dependencies:
pip install -r requirements.txt
Run the FastAPI Server:
uvicorn main:app --reload
Open in Browser:
http://127.0.0.1:8000
👨‍💻 Developer
Developed by Shahzaib Javed

Python Backend Engineer & Data Science Student
