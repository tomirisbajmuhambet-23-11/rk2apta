from devices.light import LightDevice
from devices.thermostat import Thermostat
from devices.camera import SecurityCamera
from controller import SmartHomeController

if __name__ == "__main__":
    light = LightDevice()
    thermostat = Thermostat()
    camera = SecurityCamera()

    home = SmartHomeController([light, thermostat, camera])

    home.turn_all_on()
    home.show_status()

    thermostat.set_temp(26)

    home.turn_all_off()
    home.show_status()
