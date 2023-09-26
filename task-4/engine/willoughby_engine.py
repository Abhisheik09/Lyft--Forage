from datetime import datetime, timedelta
from engine.engine import Engine

class WilloughbyEngine(Engine):
    SERVICE_INTERVAL_MONTHS = 12  # Service interval in months

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.now()

    def needs_service(self):
        service_due_date = self.last_service_date + timedelta(days=365 * WilloughbyEngine.SERVICE_INTERVAL_MONTHS)
        return self.current_date >= service_due_date
