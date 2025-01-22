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


## My Code:
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, day_rental_price, availability):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.day_rental_price = day_rental_price
        self.availability = availability

    def discount_eligibility(self, days):
        if days > 7:
            discount = (10 / 100) * self.day_rental_price
            discount_price = self.day_rental_price - discount
            print(f"Congratulations you are eligible for discount price of Rs.{discount_price}/-")
        else:
            discount_price = self.day_rental_price
        return discount_price

    def rent_vehicle(self, days):
        day_rent_price = self.discount_eligibility(days)
        total_cost = days * day_rent_price
        self.availability = False
        if not self.availability:
            status = "Taken"
        else:
            status = "Not Taken"
        print(f"You are rented the vehicle id: {self.vehicle_id}")
        print(f"-- vehicle type: {self.vehicle_type}")
        print(f"-- vehicle availability: {status}")
        print(f"-- per day rental price: {self.day_rental_price}")
        print(f"-- total rental cost for : {total_cost}")

    def return_vehicle(self):
        self.availability = True
        if self.availability:
            status = "Returned"
        else:
            status = "Not Returned"
        print(f"Returning process of vehicle id: {self.vehicle_id}")
        print(f"-- vehicle type: {self.vehicle_type}")
        print(f"-- vehicle availability: {status}")

    def display_vehicle(self):
        print(f"Vehicle details of vehicle id: {self.vehicle_id}")
        print(f"-- vehicle type: {self.vehicle_type}")
        print(f"-- vehicle availability: {self.availability}")
        print(f"-- per day rental price: {self.day_rental_price}")


class Car(Vehicle):
    def __init__(self, vehicle_id, vehicle_type, day_rental_price, availability, number_of_seats):
        super().__init__(vehicle_id, vehicle_type, day_rental_price, availability)
        self.number_of_seats = number_of_seats

    def rent_vehicle(self, days):
        super().rent_vehicle(days)
        print(f"-- seats capacity: {self.number_of_seats}")

    def return_vehicle(self):
        super().return_vehicle()
        print(f"-- seats capacity: {self.number_of_seats}")

    def display_vehicle(self):
        super().display_vehicle()
        print(f"-- seats capacity: {self.number_of_seats}")


class Bike(Vehicle):
    def __init__(self, vehicle_id, vehicle_type, day_rental_price, availability, engine_cc):
        super().__init__(vehicle_id, vehicle_type, day_rental_price, availability)
        self.engine_cc = engine_cc

    def rent_vehicle(self, days):
        super().rent_vehicle(days)
        print(f"-- engine cc: {self.engine_cc}")

    def return_vehicle(self):
        super().return_vehicle()
        print(f"-- engine cc: {self.engine_cc}")

    def display_vehicle(self):
        super().display_vehicle()
        print(f"-- engine cc: {self.engine_cc}")


class Truck(Vehicle):
    def __init__(self, vehicle_id, vehicle_type, day_rental_price, availability, load_capacity):
        super().__init__(vehicle_id, vehicle_type, day_rental_price, availability)
        self.load_capacity = load_capacity

    def rent_vehicle(self, days):
        super().rent_vehicle(days)
        print(f"-- load capacity in tons: {self.load_capacity}")

    def return_vehicle(self):
        super().return_vehicle()
        print(f"-- load capacity in tons: {self.load_capacity}")

    def display_vehicle(self):
        super().display_vehicle()
        print(f"-- load capacity in tons: {self.load_capacity}")


class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = []

    ## AI code add_vehicle() method best practices suggestion for vehicle validation
    # def add_vehicle(self, vehicle):
    #     if any(v.vehicle_id == vehicle.vehicle_id for v in self.vehicles):
    #         print(f"Vehicle ID {vehicle.vehicle_id} already exists! Cannot add duplicate.")
    #     else:
    #         self.vehicles.append(vehicle)
    #         print(f"Vehicle ID: {vehicle.vehicle_id}, Vehicle Type: {vehicle.vehicle_type} was added successfully!")

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle Id: {vehicle.vehicle_id}, Vehicle Type: {vehicle.vehicle_type}  was added successfully!")

    def rent_vehicle(self, vehicle_id, days):
        for vehicle in self.vehicles:
            if vehicle_id == vehicle.vehicle_id:
                if vehicle.availability:
                    print("\n__________________________________________")
                    return vehicle.rent_vehicle(days)
                else:
                    print("\n__________________________________________")
                    return f"Sorry! Vehicle Id: {vehicle_id} is already booked"
        print("\n__________________________________________")
        return f"Sorry! No Vehicle Id: {vehicle_id} is available, please check!"

    def return_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle_id == vehicle.vehicle_id:
                if not vehicle.availability:
                    print("\n__________________________________________")
                    return vehicle.return_vehicle()
                else:
                    print("\n__________________________________________")
                    return f"This Vehicle Id: {vehicle_id}, already returned"
            else:
                print("\n__________________________________________")
                return f"Sorry! No Vehicle Id: {vehicle_id} is exists, please check!"

    def display_all_vehicles(self):
        count = 0
        for vehicle in self.vehicles:
            count += 1
            print("\n__________________________________________")
            vehicle.display_vehicle()
        print("\n__________________________________________")
        print(f"Total number of vehicles: {count} ")

car = Car(101, "Car", 1000, True, 4)
bike = Bike(201, "Bike", 300, True, 150)
truck = Truck(301, "Truck", 2000, True, 10)

rental_company = VehicleRentalSystem()
rental_company.add_vehicle(bike)
rental_company.add_vehicle(car)
rental_company.add_vehicle(truck)

rental_company.rent_vehicle(201, 3)
rental_company.rent_vehicle(301, 8)
rental_company.display_all_vehicles()













