class SmartHomeController:
    def __init__(self, devices):
        self.devices = devices

    def turn_all_on(self):
        for device in self.devices:
            device.turn_on()

    def turn_all_off(self):
        for device in self.devices:
            device.turn_off()

    def show_status(self):
        for device in self.devices:
            device.status()
