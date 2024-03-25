import unittest
from characters import Player, Enemy

class TestCharacters(unittest.TestCase):
    def test_player_creation(self):
        player = Player("John")
        self.assertEqual(player.name, "John")
        self.assertEqual(player.hp, 100)
        self.assertEqual(player.attack, 10)
        self.assertEqual(player.gold, 0)
        self.assertEqual(player.level, 1)

    def test_enemy_creation(self):
        enemy = Enemy("Goblin", 30, 8, 20)
        self.assertEqual(enemy.name, "Goblin")
        self.assertEqual(enemy.hp, 30)
        self.assertEqual(enemy.attack, 8)
        self.assertEqual(enemy.gold_reward, 20)

if __name__ == '__main__':
    unittest.main()
