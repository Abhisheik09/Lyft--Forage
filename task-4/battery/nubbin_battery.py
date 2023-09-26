from datetime import datetime, timedelta
from utils import add_years_to_date

class NubbinBattery:
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_due_date = add_years_to_date(self.last_service_date, 4)
        return service_due_date < self.current_date

# Assuming the `add_years_to_date` function is defined in the `utils` module.
# You should import the necessary function or implement it as needed.

