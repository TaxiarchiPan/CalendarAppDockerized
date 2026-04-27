from flask import Flask, request, jsonify, render_template
import mysql.connector
import os
import time
import json

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'rootpassword'),
        database=os.environ.get('DB_NAME', 'calendar_db')
    )

def init_db():
    max_retries = 10
    for i in range(max_retries):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS saved_events (
                    id INT PRIMARY KEY,
                    events_json JSON
                )
            ''')
            cursor.execute('INSERT IGNORE INTO saved_events (id, events_json) VALUES (1, "[]")')
            conn.commit()
            conn.close()
            print("database initialized successfully!")
            return
        except Exception as e:
            print(f"try {i+1}/{max_retries}: database not ready, retrying in 5 seconds...")
            time.sleep(5)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT events_json FROM saved_events WHERE id = 1')
        row = cursor.fetchone()
        conn.close()
        
        if row and row['events_json']:
            data = row['events_json']
            if isinstance(data, str):
                data = json.loads(data)
            return jsonify(data)
    except Exception as e:
        print(e)
    return jsonify([])


@app.route('/api/events', methods=['POST'])
def save_events():
    events_data = request.json
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        json_string = json.dumps(events_data)
        cursor.execute('UPDATE saved_events SET events_json = %s WHERE id = 1', (json_string,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(e)
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)