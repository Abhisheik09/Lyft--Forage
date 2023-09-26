from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        total_wear = sum(self.tire_wear)
        return total_wear >= 3.0
