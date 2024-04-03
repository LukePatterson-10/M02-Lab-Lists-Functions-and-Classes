class Vehicle:
    def __init__ (self):
        self.vehicle_type = None

class Automobile(Vehicle):
    def __init__(Self):
        super().__init__()
        Self.year = None
        Self.make = None
        Self.model = None
        Self.doors = None
        Self.roof = None

vehicle_type = "car"
year = input("Please enter the vehicle's year: ")
make = input("Please enter the vehicle's make: ")
model = input("Please enter the vehicle's model: ")
doors = input("Please enter the number of door in the vehicle: ")
roof = input("Does your vehicle have a solid or sun roof: ")

car = Automobile()
car.vehicle_type = vehicle_type
car.year = year
car.make = make
car.model = model
car.doors = doors
car.roof = roof

print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Door count:", car.doors)
print("Roof Type:", car.roof)
