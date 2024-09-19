from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# fetching data from JSON file
def get_data_from_json():
    with open('last_30_days_data.json', 'r') as file:
        data = json.load(file)
    return data

@app.route('/data', methods=['GET'])
def get_users():
    data = get_data_from_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
