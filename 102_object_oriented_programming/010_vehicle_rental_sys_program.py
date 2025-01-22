# ### Problem Title: **Vehicle Rental System**
# **Difficulty Rating: 4/5 (Advanced)**
#
# #### **Problem Description:**
# You are tasked with designing a **Vehicle Rental System** for a company that rents out different types of vehicles. The system should allow users to:
# 1. **Add vehicles** to the inventory (cars, bikes, and trucks).
# 2. **Rent vehicles** (based on availability and type).
# 3. **Return rented vehicles** (and calculate the rental charges).
# 4. Display the **details of all vehicles** in the inventory.
#
# #### **Requirements:**
# 1. **Vehicle Class** (Base Class):
#    - Attributes: `vehicle_id`, `type`, `rental_price_per_day`, `availability`.
#    - Methods:
#      - `rent_vehicle(days)` - Update availability and calculate the rental cost.
#      - `return_vehicle()` - Mark the vehicle as available again.
#      - `display_vehicle()` - Display the vehicle details.
#
# 2. **Subclasses for Each Vehicle Type** (e.g., `Car`, `Bike`, `Truck`):
#    - Should inherit from the `Vehicle` class.
#    - May add specific attributes (e.g., `Car` might have `number_of_seats`, `Bike` might have `engine_cc`, etc.).
#
# 3. **VehicleRentalSystem Class**:
#    - Attributes: `vehicles` (a list to store all the vehicles).
#    - Methods:
#      - `add_vehicle(vehicle)` - Add a new vehicle to the system.
#      - `rent_vehicle(vehicle_id, days)` - Rent a vehicle by ID if available.
#      - `return_vehicle(vehicle_id)` - Mark the vehicle as returned.
#      - `display_all_vehicles()` - Show details of all vehicles in the system.
#
# 4. **Implement Object-Oriented Principles:**
#    - Use **inheritance** to create specialized vehicle classes.
#    - Implement **polymorphism** for displaying vehicle details.
#    - Apply **encapsulation** for data protection.
#
# #### **Example Scenario:**
# 1. Add vehicles to the system:
#    - Car: ID=101, Rental Price=₹1000/day, Seats=4, Available=True
#    - Bike: ID=201, Rental Price=₹300/day, Engine CC=150, Available=True
#    - Truck: ID=301, Rental Price=₹2000/day, Capacity=10 tons, Available=True
#
# 2. Rent a car for 3 days (ID=101):
#    - Output: `Car rented successfully! Total rental cost: ₹3000`.
#
# 3. Return the car (ID=101):
#    - Output: `Car returned successfully!`.
#
# 4. Display details of all vehicles:
#    - Show ID, Type, Rental Price, Availability, and any specific attributes for the vehicle.
#
# #### **Bonus Challenge:**
# - Add **discounts** for rentals longer than 7 days (e.g., 10% off).
# - Allow filtering vehicles by type when displaying.

# Take your time to implement this solution! Let me know if you need hints or guidance. 🚀