# **Problem:**
# Create a class called `Car` with the following attributes:
# - `make`: The brand of the car (e.g., "Toyota")
# - `model`: The model of the car (e.g., "Corolla")
# - `year`: The year the car was manufactured
# - `mileage`: The number of miles the car has driven
#
# The class should have the following methods:
# 1. A `__init__` method to initialize the car's attributes.
# 2. A method called `display_info` to display the car's details in a readable format (e.g., "2021 Toyota Corolla with 15,000 miles").
# 3. A method called `drive` that takes an integer as input representing the miles driven, and adds that to the car's current mileage.
#
# Once you've written the class, create an instance of it, display the information, and simulate the car being driven.


class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"The car ran {self.mileage}, and the model is {self.model}.")

    def drive(self, miles):
        miles = miles + self.mileage
        print(f"The car ran {miles} upto now.")


car1 = Car("Toyota", "Corolla", 2000, 15000)
car1.display_info()
miles = int(input("What is the mile ran: "))
car1.drive(miles)