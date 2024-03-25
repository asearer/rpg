import random
from items import Inventory  # Importing the Inventory class

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.gold = 0
        self.level = 1
        self.inventory = Inventory()  # Initialize the inventory

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self):
        self.hp += 20


class Enemy:
    def __init__(self, name, hp, attack, gold_reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.gold_reward = gold_reward

    def is_alive(self):
        return self.hp > 0

    def attack_player(self):
        return random.randint(1, self.attack)

    def take_damage(self, damage):
        self.hp -= damage
