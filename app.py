from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/api/calculate', methods=['POST'])
def calculate_service():
    data = request.get_json()
    mileage = int(data["mileage"])
    last_service_date = datetime.datetime.strptime(data["last_service_date"], "%Y-%m-%d")
    
    next_service = mileage + 5000
    next_service_date = last_service_date + datetime.timedelta(days=180)
    next_service_date = next_service_date.strftime("%Y-%m-%d")
    
    return jsonify({"mileage": next_service, "date": next_service_date})

if __name__ == '__main__':
    app.run(debug=True)
