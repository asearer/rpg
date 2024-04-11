import random

class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack = 10
        self.gold = 0
        self.level = 1
        self.experience = 0

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self):
        self.hp += 20
        self.hp = min(self.hp, self.max_hp)

    def gain_experience(self, experience):
        self.experience += experience
        print(f"{self.name} gained {experience} experience points.")
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        print(f"{self.name} leveled up to level {self.level}! Max HP increased to {self.max_hp}.")

    def receive_gold(self, gold):
        self.gold += gold
        print(f"{self.name} received {gold} gold.")

class Enemy:
    def __init__(self, name, hp, attack, gold_reward, experience_reward=0):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.attack = attack
        self.gold_reward = gold_reward
        self.experience_reward = experience_reward

    def is_alive(self):
        return self.hp > 0

    def attack_player(self):
        return random.randint(1, self.attack)

    def take_damage(self, damage):
        self.hp -= damage

    def give_reward(self, player):
        player.receive_gold(self.gold_reward)
        player.gain_experience(self.experience_reward)
        print(f"{player.name} defeated {self.name} and received {self.gold_reward} gold and {self.experience_reward} experience points.")
