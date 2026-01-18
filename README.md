# 🚀 Django Blog API

A professional starter project designed to demonstrate REST API development using Django.

---

## 🛠 1. Installation & Setup

Follow these steps:

```bash
# Clone the repository
git clone https://github.com/Maydash/tutorial-django-blog.git
cd tutorial-django-blog

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

http://127.0.0.1:8000/swagger
