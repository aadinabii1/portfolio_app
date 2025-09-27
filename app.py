from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Health check
@app.route('/health')
def health():
    return 'Server is up and running'

# About page
@app.route('/about')
def about():
    return render_template("about.html")

# Projects page
@app.route('/projects')
def projects():
    return render_template("projects.html")
