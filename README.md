# ⚡ E-Bike Showroom Management System

A modern, full-stack web application built using **FastAPI**, **SQLAlchemy**, **SQLite/PostgreSQL**, and **Bootstrap 5**. This system is designed to efficiently manage e-bike showroom customers, contact numbers, bike models, and battery numbers.

---

## 🎥 Project Demo

[![Watch Demo on Facebook](https://img.shields.io/badge/▶_Watch_Project_Demo-Facebook-1877F2?style=for-the-badge&logo=facebook)](https://www.facebook.com/61594547758097/videos/pcb.122114287281484925/1631191598793700)

*(Click the badge above to watch the full application walkthrough on Facebook)*

---

## 🚀 Features
* **Full CRUD Operations:** Seamlessly add, view, update, and delete customer records.
* **Live Search Filter:** Instantly filter records by customer name, phone number, or bike model.
* **FastAPI Backend:** High-performance asynchronous endpoints powered by Pydantic data validation.
* **SQLAlchemy ORM:** Robust relational database management and clean session handling.
* **Responsive UI:** Modern Bootstrap 5 dark mode dashboard optimized for both desktop and mobile devices.

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
└── README.md            # Project Documentation
