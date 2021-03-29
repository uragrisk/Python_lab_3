from models.movement_type import MovementType
from models.surface_type import SurfaceType

class Ship():

    def __init__(self, tonnage: float, max_speed: int, fuel_per_100miles: float, movement_surface: SurfaceType , movement_type = MovementType):
        self.tonnage = tonnage
        self.max_speed = max_speed
        self.fuel_per_100miles = fuel_per_100miles
        self.movement_surface = movement_surface
        self.movement_type = movement_type

    def __str__(self):
        return f'Tonnage: {self.tonnage} \n' \
               f'Maximum speed: {self.max_speed} \n' \
               f'Fuel consumption per 100 miles: {self.fuel_per_100miles} \n' \
               f'Movement surface: {self.movement_surface} \n' \
               f'Moves thanks: {self.movement_type}'