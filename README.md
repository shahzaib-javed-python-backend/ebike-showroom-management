# ⚡ E-Bike Showroom Management System

A modern, full-stack web application built using **FastAPI**, **SQLAlchemy**, **SQLite/PostgreSQL**, and **Bootstrap 5**. This system is designed to efficiently manage e-bike showroom customers, contact numbers, bike models, and battery numbers.

---

## 🎥 Project Demo

[![Project Demo](https://img.shields.io/badge/▶_Watch_Project_Demo-Video-red?style=for-the-badge&logo=youtube)](https://github.com/shahzaib-javed-python-backend/ebike-showroom-management/blob/main/demo.mp4.mp4)

---

## 🚀 Features
* **Full Operations (CRUD):** Seamlessly add, view, update, and delete customer records.
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
├── demo.mp4.mp4         # Project Demo Video
└── README.md            # Project Documentation
