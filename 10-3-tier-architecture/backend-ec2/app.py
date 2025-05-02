from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    db = mysql.connector.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        passwd=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )
    cursor = db.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    return f"Hello from backend! Current DB time: {result[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

