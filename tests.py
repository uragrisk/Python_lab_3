import unittest
from models.ship import Ship
from models.ferry import Ferry
from models.hydrofoil_ship import HydrofoilShip
from models.hovercraft import Hovercraft
from managers.ShipManager import ShipManager
from models.movement_type import MovementType
from models.surface_type import SurfaceType
from models.wing_types import WingTypes
from models.sort_order import SortOrder

class TestShipManager(unittest.TestCase):
    def setUp(self):
        self.hovercraft = Hovercraft(300, 400, 700, SurfaceType.WATER, 
        MovementType.PROPELLERS, 1234.55, SurfaceType.GROUNG)
        self.hydrofoil_ship = HydrofoilShip(100.00, 400, 500, SurfaceType.WATER, 
             MovementType.PROPELLERS, 125.45, WingTypes.FULLY_SUBMERGED_WINGS)
        self.ferry = Ferry(100.00, 25, 23.5,SurfaceType.WATER, MovementType.PROPELLERS, 100)
        result = [self.hovercraft, self.hydrofoil_ship, self.ferry]
        self.shipManager = ShipManager(result)


    def test_search_by_tonnage(self):
        self.assertEqual(self.shipManager.search_by_tonnage(100.00), [self.hydrofoil_ship, self.ferry])

    def test_search_by_max_speed(self):
        self.assertEqual(self.shipManager.search_by_max_speed(400), [self.hovercraft, self.hydrofoil_ship])
        
    def test_sort_by_fuel_per_100miles(self):
        self.assertEqual(self.shipManager.sort_by_fuel_per_100miles(SortOrder.ASC), [self.ferry, self.hydrofoil_ship, self.hovercraft])

if __name__ == "__main__":
    unittest.main()

        


