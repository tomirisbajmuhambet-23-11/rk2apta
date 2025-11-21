class Thermostat:
    def __init__(self):
        self.is_on = False
        self.temperature = 22  # әдепкі температура

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_temp(self, value):
        self.temperature = value

    def status(self):
        state = 'ON' if self.is_on else 'OFF'
        print(f"Thermostat is {state}, Temperature: {self.temperature}°C")
