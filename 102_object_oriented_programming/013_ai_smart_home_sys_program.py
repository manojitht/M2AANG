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
            print(f"Invalid brightness level entered {level}, please check.")
        return self.brightness

    def set_color(self, rgb):
        self.color = rgb
        return self.color


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, name, status, temperature):
        super().__init__(device_id, name, status)
        self.temperature = temperature

    def set_temperature(self, degree):
        if type(degree) == 'int':
            self.temperature = degree
        else:
            print(f"The degree must be a numeral value, please check!")
        return self.temperature


class SmartLock(SmartDevice):
    def __init__(self, device_id, name, status, is_locked):
        super().__init__(device_id, name, status)
        self.is_locked = is_locked

    def lock(self):
        if not self.lock:
            self.is_locked = True
            print(f"SmartLock locked successfully!")
        else:
            print("Already locked!")

    def unlock(self):
        if self.lock:
            self.is_locked = False
            print("SmartLock unlocked successfully!")
        else:
            print("Already unlocked!")

