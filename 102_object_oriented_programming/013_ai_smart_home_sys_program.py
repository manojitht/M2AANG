### **Advanced Python OOP Challenge 🔥🔥🔥🔥🔥**
# **Problem Statement:**
#
# You are designing an **AI-powered Smart Home System** using **OOP in Python**. The system should manage different types of smart devices and allow remote control via a central hub.
#
# ---
#
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
