
# Coffee Shop Website

A simple and elegant web‑application for a coffee shop built with Python, Flask, HTML/CSS, and SQLite database.

> Repository by Rania Zulfiqar.

## 📝 Table of Contents

* [About](#about)
* [Features](#features)
* [Technology Stack](#technology‑stack)
* [Project Structure](#project‑structure)
* [Installation & Setup](#installation‑setup)
* [Usage](#usage)
* [Configuration](#configuration)
* [Database](#database)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## About

This project is a web application for a coffee shop, created to demonstrate a full‑stack workflow: backend (Flask/Python), SQLite database, and frontend templates (HTML/CSS).
It allows you to serve a coffee shop website where users can browse, and administrators can manage the menu and orders.
The repository contains:

* `app.py` — main Flask application entry point.
* `create_db.py` — script for initializing the SQLite database (`coffee.db`) and schema.
* `coffee.db` — the SQLite database file (sample/populated).
* `templates/` — HTML templates for pages.
* `static/` — CSS, images, JavaScript (if any) assets.
* Additional files such as README, etc.

## Features

* Home page / landing page for the coffee shop.
* Menu listing of coffee items.
* Admin route or script to create/update the database (via `create_db.py`).
* Database storage for coffee items and related metadata.
* Clean, responsive HTML/CSS design for frontend.
* Simple Flask routing and templating for dynamic pages.
* SQLite used for lightweight database management.

## Technology Stack

* **Backend**: Python + Flask (micro web‑framework)
* **Database**: SQLite (`coffee.db`)
* **Frontend**: HTML5, CSS3, optionally JavaScript
* **Templates**: Flask Jinja2 templates stored in `templates/`
* **Static assets**: `static/` folder for CSS/JS/images

## Project Structure

```
coffee‑shop‑website/
│  
├── app.py              # Main Flask application file  
├── create_db.py        # Script to create/populate SQLite DB  
├── coffee.db           # SQLite database file  
├── templates/          # HTML template files  
│   ├── base.html  
│   ├── index.html  
│   └── …  
├── static/             # Static assets  
│   ├── css/  
│   ├── js/  
│   └── images/  
└── README.md           # This file  
```

## Installation & Setup

These steps assume you have Python installed (version 3.x).

1. Clone this repository:

   ```bash
   git clone https://github.com/RANIAZULFIQAR/coffee-shop-website.git  
   cd coffee-shop-website  
   ```
2. (Optional) Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv  
   source venv/bin/activate      # On Linux/macOS  
   venv\Scripts\activate         # On Windows  
   ```
3. Install required Python packages (if any). If you use `requirements.txt` you can run:

   ```bash
   pip install -r requirements.txt  
   ```

   *If `requirements.txt` is not present, ensure Flask is installed:*

   ```bash
   pip install flask  
   ```
4. Initialise the database:

   ```bash
   python create_db.py  
   ```

   This will create `coffee.db` (or update it).
5. Run the application:

   ```bash
   python app.py  
   ```
6. Open your browser and navigate to `http://127.0.0.1:5000/` (or whichever host/port Flask reports).

## Usage

* Browse the homepage and menu items.
* If admin‑functionality is implemented, log in (if needed) to add/edit coffee items.
* Update `coffee.db` via `create_db.py` or via any interface you’ve built.
* Customize CSS, templates and assets in `static/` to suit your branding.

## Configuration

* If you change the database name or location, update `app.py` accordingly (the database URI).
* For production deployment, consider using a more robust database (PostgreSQL, MySQL) and a production server (gunicorn/uwsgi) behind Nginx.
* Ensure debug mode is turned off in production (`app.run(debug=False)`).
* Adjust `templates/` and `static/` paths if you restructure.

## Database

The SQLite database `coffee.db` likely contains at least one table (e.g., `coffee_items`, or `menu`) with columns such as `id`, `name`, `description`, `price`, `image_path`, etc.
You can open the database using SQLite browser to view and edit.
The `create_db.py` script handles creation of tables and populating initial data (if any).



## Contact

Created by [Rania Zulfiqar](rania.zul786@gmail.com).
Feel free to reach out for questions, feedback or collaboration.




