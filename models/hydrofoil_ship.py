from models.movement_type import MovementType
from models.surface_type import SurfaceType
from models.ship import Ship
from models.wing_types import WingTypes

class HydrofoilShip(Ship):
    def __init__(self, tonnage: float, max_speed: int, 
                 fuel_per_100miles: float, movement_surface: SurfaceType,
                 movement_type: MovementType,
                 wing_length = 100.00, 
                 wing_type = WingTypes.FULLY_SUBMERGED_WINGS, 
                 max_high_above_water = 100.00):
        super().__init__(tonnage, max_speed, fuel_per_100miles, 
        movement_surface, movement_type)
        self.wing_length = wing_length
        self.wing_type = wing_type
        self.max_high_above_water = max_high_above_water

    def __str__(self):
        return f'{super().__str__()} \n' \
               f'Length of wings: {self.wing_length} \n' \
               f'Type of wings: {self.wing_type} \n' \
               f'Max high above water: {self.max_high_above_water} meters'

         