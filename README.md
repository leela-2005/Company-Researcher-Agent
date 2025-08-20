# Company Research Agent

A Django-based web application that allows users to research company information, fetch related news articles from RSS feeds, and display them in a simple interface.

## 🚀 Features
- Search for a company and fetch recent news articles.
- Displays headlines, summaries, and links to external sources.
- Built with Django, `requests`, `feedparser`, and `tenacity`.
- Modular app structure (`research` app).
- Simple and extendable UI using Django templates.

---

## 📂 Project Structure
mysite/
│── manage.py
│── db.sqlite3
│── mysite/
│ │── settings.py
│ │── urls.py
│ │── wsgi.py
│ │── asgi.py
│ └── templates/
│ └── company_profile.html
│
└── research/
│── views.py
│── models.py
│── urls.py
│── apps.py
└── ...
