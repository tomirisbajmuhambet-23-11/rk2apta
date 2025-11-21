class SecurityCamera:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def status(self):
        print(f"Security Camera is {'ON' if self.is_on else 'OFF'}")
