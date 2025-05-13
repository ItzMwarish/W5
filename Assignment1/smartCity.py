# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

# Base Class

class SmartDevice:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location
        self.__status = "inactive"
        self.__battery_level = 100

    def activate(self):
        self.__status = "active"
        

    def deactivate(self):
        self.__status = "inactive"

    def report_status(self):
        return f"ID: {self.device_id}, Status: {self.__status}, Battery: {self.__battery_level}%"

    def charge_battery(self):
        self.__battery_level = 100


class SmartStreetLight(SmartDevice):
    def __init__(self, device_id, location):
        super().__init__(device_id, location)
        self.brightness_level = 50
        self.motion_detected = False

    def detect_motion(self):
        self.motion_detected = True
        self.brightness_level = 100

    def adjust_brightness(self, level):
        self.brightness_level = level


class SmartTrafficLight(SmartDevice):
    def __init__(self, device_id, location):
        super().__init__(device_id, location)
        self.current_light = "Red"
        self.traffic_density = 0

    def analyze_traffic(self, density):
        self.traffic_density = density
        self.current_light = "Green" if density > 50 else "Red"



light = SmartStreetLight("SL001", "5th Avenue")
light.activate()
light.detect_motion()
print(light.report_status())
print(f"Brightness: {light.brightness_level}")
   