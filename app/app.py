from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps 🚀"

@app.route("/db")
def db():
    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="testdb"
    )
    return "DB Connected ✅"

app.run(host="0.0.0.0", port=5000)