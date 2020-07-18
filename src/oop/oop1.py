# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# parent class
class Vehicle:
    def __init__(self):
       pass

# inherits from Vehicle class
class GroundVehicle(Vehicle):
    def __init__(self):
        pass

# inherits from GroundVehicle class
class Car(GroundVehicle):
    def __init__(self):
        pass

# inherits from GroundVehicle class
class Motorcycle(GroundVehicle):
    def __init__(self):
        pass

# inherits from Vehicle class
class FlightVehicle(Vehicle):
    def __init__(self):
        pass

# inherits from FlightVehicle class
class Airplane(FlightVehicle):
    def __init__(self):
        pass

# inherits from FlightVehicle class
class Starship(FlightVehicle):
    def __init__(self):
        pass
