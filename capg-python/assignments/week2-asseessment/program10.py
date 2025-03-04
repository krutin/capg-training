class Electronics:
    def __init__(self, voltage_required):
        self.voltage_required = voltage_required

    def display_info(self):
        print(f"Voltage Required: {self.voltage_required}V")

class MobileDevice(Electronics):
    def __init__(self, voltage_required, charging_type):
        super().__init__(voltage_required)
        self.charging_type = charging_type

    def display_info(self):
        super().display_info()
        print(f"Charging Type: {self.charging_type}")

class SmartPhone(MobileDevice):
    def __init__(self, voltage_required, charging_type, company_name):
        super().__init__(voltage_required, charging_type)
        self.company_name = company_name

    def display_info(self):
        super().display_info()
        print(f"Company Name: {self.company_name}")

smartphone = SmartPhone(voltage_required=5, charging_type="USB-C", company_name="Apple")
smartphone.display_info()