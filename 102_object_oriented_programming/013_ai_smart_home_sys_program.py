### **Advanced Python OOP Challenge 🔥🔥🔥🔥🔥**
# **Problem Statement:**
#
# You are designing an **AI-powered Smart Home System** using **OOP in Python**. The system should manage different types of smart devices and allow remote control via a central hub.
# ### **🛠 Requirements:**
# 1. **Base Class: `SmartDevice`**
#    - Common attributes: `device_id`, `name`, `status` (`on`/`off`).
#    - Common methods: `turn_on()`, `turn_off()`, `get_status()`.
#    - Implement **encapsulation** to protect `device_id`.
#
# 2. **Derived Classes (Inheritance & Polymorphism)**
#    - `SmartLight`:
#      - Additional attributes: `brightness (0-100)`, `color (RGB)`.
#      - Method: `set_brightness(level)`, `set_color(rgb)`.
#    - `SmartThermostat`:
#      - Additional attributes: `temperature (in °C)`.
#      - Method: `set_temperature(degrees)`.
#    - `SmartLock`:
#      - Additional attributes: `is_locked (True/False)`.
#      - Methods: `lock()`, `unlock()`.
#
# 3. **Central Hub (`SmartHomeHub` - Singleton Pattern)**
#    - Manages all connected devices.
#    - Methods:
#      - `add_device(device)`: Add a smart device.
#      - `remove_device(device_id)`: Remove a device.
#      - `get_device(device_id)`: Get a device by ID.
#      - `control_device(device_id, action, *args)`:
#        - Turns on/off, changes settings (brightness, temperature, etc.).
#      - `list_devices()`: Show all devices.
#
# 4. **Special Features**
#    - Use **`@classmethod`** and **`@staticmethod`** where necessary.
#    - Ensure proper use of **encapsulation** and **abstraction**.
#    - Use **Python built-in functions** wherever possible.



# My Code:
import logging, threading, asyncio

logging.basicConfig(level=logging.INFO)

class SmartDevice:
    def __init__(self, device_id, name, status):
        self.device_id = device_id
        self.name = name
        self.status = status

    def turn_on(self):
        self.status = "on"
        return self.status

    def turn_off(self):
        self.status = "off"
        return self.status

    def set_device_id(self, device_id):
        self.device_id = device_id
        return self.device_id


class SmartLight(SmartDevice):
    def __init__(self, device_id, name, status, brightness, color):
        super().__init__(device_id, name, status)
        self.brightness = brightness
        self.color = color

    def set_brightness_level(self, level):
        if 0 < level <= 100:
            self.brightness = int(level)
        else:
            logging.info(f"Invalid brightness level entered {level}, please check.")
        return self.brightness

    def set_color(self, rgb):
        self.color = rgb
        return self.color


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, name, status, temperature):
        super().__init__(device_id, name, status)
        self.temperature = temperature

    def set_temperature(self, degree):
        self.temperature = degree
        return self.temperature


class SmartLock(SmartDevice):
    def __init__(self, device_id, name, status, is_locked):
        super().__init__(device_id, name, status)
        self.is_locked = is_locked

    def lock(self):
        if not self.is_locked:
            self.is_locked = True
            logging.info(f"SmartLock locked successfully!")
        else:
            logging.info("Already locked!")

    def unlock(self):
        if self.is_locked:
            self.is_locked = False
            logging.info("SmartLock unlocked successfully!")
        else:
            logging.info("Already unlocked!")


class SmartHomeHub:
    __instance_exists = None

    @staticmethod
    def create_instance():
        if not SmartHomeHub.__instance_exists:
            SmartHomeHub()
        return SmartHomeHub.__instance_exists

    def __init__(self):
        if SmartHomeHub.__instance_exists:
            raise Exception("SmartHomeHub Object already exists.")
        else:
            SmartHomeHub.__instance_exists = self
            self.devices_list = {}


    def add_device(self, device):
        if device.device_id not in self.devices_list:
            self.devices_list[device.device_id] = device
            logging.info(f"The device {device.name}, added successfully!")
        else:
            logging.info(f"The device {device.name}, already exists..")

    def remove_device(self, device_id):
        if device_id in self.devices_list:
            removed_device = self.devices_list.pop(device_id)
            logging.info(f"Device {removed_device.name} was removed successfully!")
        else:
            logging.error(f"Device with id:{device_id} was not found.")

    def get_device(self, device_id):
        if device_id in self.devices_list:
            get_device = self.devices_list[device_id]
            logging.info(f"Device id:{device_id} found, name: {get_device.name}, status: {get_device.status}")
        else:
            logging.error(f"Device with id:{device_id} was not found.")

    async def control_device(self, device_id, action, *values):
        device = self.devices_list.get(device_id)

        if not device:
            logging.error(f"Device with id:{device_id} was not found.")
            return

        command_dict = {
            "turn_on": device.turn_on,
            "turn_off": device.turn_off,
            "set_temperature": lambda: device.set_temperature(values[0]) if isinstance(device, SmartThermostat) else None,
            "set_brightness_level": lambda: device.set_brightness_level(values[0]) if isinstance(device, SmartLight) else None,
            "set_color": lambda: device.set_color(values[0]) if isinstance(device, SmartLight) else None,
            "lock": device.lock if isinstance(device, SmartLock) else None,
            "unlock": device.unlock if isinstance(device, SmartLock) else None,
        }

        command = command_dict.get(action)
        if command:
            # thread = threading.Thread(target=command)
            # thread.start()
            task = command()
            await task
            logging.info(f"Device '{device.name}' successfully executed '{action}'.")
        else:
            logging.warning(f"Action '{action}' is not available for {device.name}.")

    def list_devices(self):
        for device_id, device in self.devices_list.items():
            logging.info(f"Device id: {device_id}, name: {device.name}, status: {device.status}.")


def main():
    # need to use the asyncio functions to run here..
    pass

hub = SmartHomeHub()
light = SmartLight(1, "Living Room Light", "on", 55, "white" )
thermostat = SmartThermostat(2, "Bedroom Thermostat", "on", 23)
lock = SmartLock(3, "Keypad Lock", "on", True)

hub.add_device(light)
hub.add_device(thermostat)
hub.add_device(lock)

hub.control_device(light.device_id, "turn_off")
hub.control_device(light.device_id, "turn_on")
hub.control_device(light.device_id, "set_brightness_level", 95)
hub.control_device(thermostat.device_id, "set_temperature", 22)
hub.control_device(lock.device_id, "unlock")

hub.list_devices()

hub.remove_device(1)
hub.get_device(2)

# Using the best practices of threading and asyncio






