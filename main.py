# Super class that contains the attribute for the vehicle type.
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Class that inherits the attributes from vehicle.
class automobile(Vehicle):
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)
        self.vehicle = input("Enter the vehicle type: ")
        self.year = input("Enter the year the vehicle was made: ")
        self.make = input("Enter the make of the car: ")
        self.model = input("Enter the model of the car: ")
        self.doors = input("Does the car have two or four doors?: ")
        self.roof = input("Does the car have a solid roof or a sun roof?: ")

    def __str__(self):
        return f"Vehicle Type: {self.vehicle}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}"

# Prints out the information the user entered that was stored in the vehicle class.
vehicleInfo = automobile("")
print(vehicleInfo)