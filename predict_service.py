# predict_service.py

from datetime import datetime, timedelta

def calculate_next_service(last_service_date, mileage, service_interval=5000):
    # Convert the last service date to a datetime object
    last_service = datetime.strptime(last_service_date, "%Y-%m-%d")
    
    # Calculate the mileage difference and determine when next service is due
    next_service_mileage = mileage + service_interval
    next_service_date = last_service + timedelta(days=365)  # simple 1-year assumption
    
    return next_service_mileage, next_service_date.strftime("%Y-%m-%d")
