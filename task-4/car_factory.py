class SpindlerBattery:
    # ... Existing code ...

    def service_required(self, months):
        # Updated service requirement to three years (36 months)
        return months >= 36


class CarriganTire:
    # ... Existing code ...

    def set_tire_wear(self, tire_wear):
        self.tire_wear = tire_wear

    def service_required(self):
        # Service required if any tire wear value is greater than or equal to 0.9
        return any(wear >= 0.9 for wear in self.tire_wear)


class OctoprimeTire:
    # ... Existing code ...

    def set_tire_wear(self, tire_wear):
        self.tire_wear = tire_wear

    def service_required(self):
        # Service required if the sum of all tire wear values is greater than or equal to 3
        return sum(self.tire_wear) >= 3
