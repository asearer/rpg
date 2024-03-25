import unittest
from shop import Shop, Item
from characters import Player

class TestShop(unittest.TestCase):
    def test_item_creation(self):
        item = Item("Test Item", "Test item description", 50)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.description, "Test item description")
        self.assertEqual(item.price, 50)

    def test_shop_buy_item(self):
        shop = Shop()
        shop.add_item(Item("Test Item", "Test item description", 50))
        player = Player("John")
        player.gold = 100
        shop.buy_item(0, player)
        self.assertEqual(player.gold, 50)
        self.assertEqual(len(player.inventory.items), 1)

if __name__ == '__main__':
    unittest.main()
