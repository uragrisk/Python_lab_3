from models.movement_type import MovementType
from models.surface_type import SurfaceType
from models.ship import Ship

class Ferry(Ship):
    def __init__(self, tonnage: float, max_speed: int, fuel_per_100miles: float, movement_surface: SurfaceType , movement_type: MovementType, max_number_of_cars = 100):
        super().__init__(tonnage, max_speed, fuel_per_100miles, movement_surface, movement_type)
        self.max_number_of_cars = max_number_of_cars

    def __str__(self):
        return f'{super().__str__()} \n'\
               f'Max number of car: {self.max_number_of_cars}'