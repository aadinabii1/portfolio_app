# Flask Portfolio Website

A simple portfolio web application built with **Flask**, showcasing my skills and projects in **DevOps, Cloud, and Automation**.

---

## 🚀 Features

* Home page with a welcome message
* About page with bio and skills
* Projects page listing DevOps/Cloud projects
* Health check endpoint (`/health`) for monitoring
* Responsive design with custom CSS

---

## 🛠️ Tech Stack

* **Python 3**
* **Flask** (backend framework)
* **HTML/CSS** (frontend templates & styling)
* **Docker** (optional: containerization)

---

## 📂 Project Structure

```
portfolio_app/
│
├── app.py               # Flask app (routes only)
├── run.py               # Entry point to start the server
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
│   ├── index.html
│   ├── about.html
│   └── projects.html
└── static/
    └── style.css        # Custom CSS
```

---

## ▶️ How to Run Locally

1. Clone this repo:

   ```bash
   git clone https://github.com/<your-username>/flask-portfolio.git
   cd flask-portfolio
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   python run.py
   ```

5. Open in browser:

   * Home: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
   * About: [http://127.0.0.1:5000/about](http://127.0.0.1:5000/about)
   * Projects: [http://127.0.0.1:5000/projects](http://127.0.0.1:5000/projects)
   * Health check: [http://127.0.0.1:5000/health](http://127.0.0.1:5000/health)

---

## 🐳 Run with Docker (Optional)

1. Build Docker image:

   ```bash
   docker build -t flask-portfolio .
   ```

2. Run container:

   ```bash
   docker run -d -p 5000:5000 flask-portfolio
   ```

3. Access app at:
   [http://localhost:5000](http://localhost:5000)

---

## 📸 Screenshots

<img width="1277" height="334" alt="image" src="https://github.com/user-attachments/assets/b87c1ab1-ecaf-4487-8ecd-d575747a9d5b" />


---

## 👨‍💻 Author

**Adnan**

* Passionate about DevOps, Cloud, and Automation
* [LinkedIn](https://linkedin.com/) | [GitHub](https://github.com/)

---

