from datetime import datetime, timedelta
from battery.battery import Battery  # Assuming the Battery class is in the battery module
from utils import add_years_to_date

class SpindlerBattery:
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_due_date = add_years_to_date(self.last_service_date, 2)
        return service_due_date < self.current_date
