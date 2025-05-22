from flask import Flask, request, jsonify
import csv
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = 'study_data.csv'

# CSV 파일 초기화 (헤더 포함)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'subject', 'time'])

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data['date'], data['subject'], data['time']])
    return jsonify({'status': 'success'})

@app.route('/data', methods=['GET'])
def get_data():
    result = []
    with open(DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['time'] = float(row['time'])
            result.append(row)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
