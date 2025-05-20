# 🛍️ Product Management App (Django + DRF)

A simple web app to add, view, and manage products using Django, Django REST Framework, and Render for cloud deployment.

---

## 🚀 Features

- Add products (name, description, price)
- View a list of products
- View detailed info for each product
- REST API (POST, GET list, GET detail)
- Deployed on Render (cloud platform)

---

## 🧑‍💻 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/amitkrvr/product-assignment.git
cd product-assignment
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

---

## 🧪 REST API Endpoints

| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| POST   | /api/products/     | Create a new product     |
| GET    | /api/products/     | Get list of all products |
| GET    | /api/products/<id>/| Get single product detail|

---

## 🌐 Live Demo on Render

Frontend + Backend:  
[https://product-assignment-9h4v.onrender.com/list/](https://product-assignment-9h4v.onrender.com/list/)

---

## ⚙️ Deploying to Render (Cloud Hosting)

### 1. Push code to GitHub

```bash
git init
git remote add origin https://github.com/amitkrvr/product-assignment.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 2. Create Render Web Service

- Go to: [https://dashboard.render.com](https://dashboard.render.com)
- Click **"New Web Service"**
- Connect your GitHub repo
- Choose:
  - Runtime: Python 3.x
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `gunicorn config.wsgi`
  - Environment: `PYTHON_VERSION=3.11`
- Set `DEBUG=False` and `ALLOWED_HOSTS` appropriately in `settings.py`

### 3. Add `static` settings in `settings.py`

```python
import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### 4. Add `render.yaml` (optional for auto-deploy)

```yaml
services:
  - type: web
    name: product-app
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn config.wsgi"
    envVars:
      - key: DEBUG
        value: False
```

---

## 📁 Folder Structure

```
config/
├── settings.py
├── urls.py
products/
├── models.py
├── views.py
├── serializers.py
├── templates/
│   ├── base.html
│   ├── add_product.html
│   ├── product_list.html
│   └── product_detail.html
static/
├── products/
│   └── styles.css
```

---

## 📝 License

This project is licensed under the MIT License.
