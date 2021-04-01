from models.sort_order import SortOrder
from models.ship import Ship


class ShipManager:
    def __init__(self, ships = list):
        self.ships = ships 

    def search_by_tonnage(self, tonnage: float):
        found_ships = [ship for ship in self.ships if ship.tonnage == tonnage]
        return found_ships
    
    def search_by_max_speed(self, max_speed: float):
        found_ships = [ship for ship in self.ships if ship.max_speed == max_speed]
        return found_ships

    def sort_by_fuel_per_100miles(self, sort_order = SortOrder):
        return sorted(self.ships, key = lambda ship: ship.fuel_per_100miles, reverse = sort_order.value)
        
        # 3(reverse = sort_order.value, key = lambda ship: ship.flue_per_100miles)





    