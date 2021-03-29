from models.ship import Ship
from models.ferry import Ferry
from models.hydrofoil_ship import HydrofoilShip
from models.hovercraft import Hovercraft
from managers.ShipManager import ShipManager
from models.movement_type import MovementType
from models.surface_type import SurfaceType
from models.wing_types import WingTypes
from models.sort_order import SortOrder


def print_ships(ships = []):
    for ship in ships:
        print(ship)
        print("-------------------------------")

def main():
    print("hello")
    ships = [Ferry(100.00, 25, 23.5,SurfaceType.WATER, MovementType.PROPELLERS, 100),
             HydrofoilShip(100.00, 400, 500, SurfaceType.WATER, 
             MovementType.PROPELLERS, 125.45, WingTypes.FULLY_SUBMERGED_WINGS),
             Hovercraft(300, 400, 700, SurfaceType.WATER, MovementType.PROPELLERS,
             1234.55, SurfaceType.GROUNG)]
    manager = ShipManager(ships)
    print("Ships with choosen tonnage:")
    list_of_ships_with_tonage = manager.search_by_tonnage(100.00) 
    print_ships(list_of_ships_with_tonage)
    print("Ships with choosen max speed:")
    list_of_ships_with_max_speed = manager.search_by_max_speed(400)
    print_ships(list_of_ships_with_max_speed)
    print("Sort by fuel consumption per 100 miles:")
    list_of_ships_sorted_by_fuel_per_100miles = manager.sort_by_fuel_per_100miles(SortOrder.ASC)
    print_ships(list_of_ships_sorted_by_fuel_per_100miles)


if __name__ == "__main__":
    main()
