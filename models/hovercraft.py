from models.movement_type import MovementType
from models.surface_type import SurfaceType
from models.ship import Ship

class Hovercraft(Ship):
    def __init__(self, tonnage: float, max_speed: int, fuel_per_100miles: float,
                 movement_surface: SurfaceType, movement_type = MovementType, 
                 volume_of_air = 1200.00, additional_surface = SurfaceType.GROUNG):
        super().__init__(tonnage, max_speed, fuel_per_100miles, 
        movement_surface, movement_type)
        self.volume_of_air = volume_of_air
        self.additional_surface = additional_surface

    def __str__(self):
        return f'{super().__str__()} \n' \
               f'Additional movement surface: {self.additional_surface}\n'\
               f'Volume of air in bag: {self.volume_of_air}'
               
         