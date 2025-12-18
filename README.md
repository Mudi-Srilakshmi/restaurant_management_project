# Restaurant Management System

A full-stack Django web application developed during my internship at Perpex.
This project helps restaurants manage menu items, customer orders, billing, and staff roles through a simple and user-friendly interface.

It is designed to simulate real-world restaurant operations using Django best practices.

---

## Project Overview

The Restaurant Management System allows restaurant administrators and staff to:
- Manage menu items and products
- Handle customer orders
- Generate bills
- Control access based on user roles

This project demonstrates my understanding of Django architecture, authentication, and database-driven web applications.

---

## Features

- User authentication (Login & Signup)
- Role-based access (Admin / Staff / Customer)
- Product and menu management
- Order placement and tracking
- Bill generation
- Simple dashboard for restaurant operations
- Secure session-based authentication

---

## Tech Stack

Backend:
- Python
- Django

Frontend:
- HTML
- CSS
- Django Templates

Database:
- SQLite (default)
- Easily extendable to MySQL / PostgreSQL

---

## Project Structure

restaurant_management_project/
- account/                 User authentication & profiles
- home/                    Homepage and static views
- orders/                  Order handling and billing
- products/                Menu and product management
- restaurant_management/   Project settings and URLs
- manage.py
- README.md

---

## How to Run the Project Locally

1. Clone the repository  
git clone https://github.com/Mudi-Srilakshmi/restaurant_management_project.git  
cd restaurant_management_project  

2. Create virtual environment (recommended)  
python -m venv venv  
source venv/bin/activate  
(Windows: venv\Scripts\activate)

3. Install dependencies  
pip install -r requirements.txt  

4. Apply migrations  
python manage.py migrate  

5. Run the server  
python manage.py runserver  

---

## Access the Application

Open your browser and visit:  
http://127.0.0.1:8000/

---

## User Roles

Admin – Full access to manage users, products, and orders  
Staff – Can manage orders and billing  
Customer – Can view menu and place orders  

---

## Future Improvements

- Add REST APIs using Django REST Framework
- PostgreSQL database for production
- Deployment on Render / Railway / PythonAnywhere
- Improved UI with Bootstrap
- Order analytics and reports
- Payment gateway integration

---

## Project Timeline

Duration: 3–4 weeks  
Developed during internship at Perpex

---

## Author

Mudi Srilakshmi  
GitHub: https://github.com/Mudi-Srilakshmi  
LinkedIn: https://www.linkedin.com/in/sri-lakshmi-mudi-840084350  

If you like this project, feel free to star the repository.


