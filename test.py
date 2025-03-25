# test.py
from predict_service import calculate_next_service

# Example data
last_service_date = "2023-10-01"
mileage = 20000

next_service_mileage, next_service_date = calculate_next_service(last_service_date, mileage)

print(f"Next Service Due at: {next_service_mileage} miles on {next_service_date}")
