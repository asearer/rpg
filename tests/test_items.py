import unittest
from items import Item, HealthPotion, Inventory

class TestItems(unittest.TestCase):
    def test_health_potion_creation(self):
        health_potion = HealthPotion()
        self.assertEqual(health_potion.name, "Health Potion")
        self.assertEqual(health_potion.description, "Restores 20 HP")
        self.assertEqual(health_potion.price, 10)

    def test_inventory_add_item(self):
        inventory = Inventory()
        health_potion = HealthPotion()
        inventory.add_item(health_potion)
        self.assertEqual(len(inventory.items), 1)
        self.assertEqual(inventory.items[0].name, "Health Potion")

if __name__ == '__main__':
    unittest.main()
