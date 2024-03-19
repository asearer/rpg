import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.gold = 0
        self.level = 1

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

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        print(f"{player.name}'s HP: {player.hp}")
        print(f"{enemy.name}'s HP: {enemy.hp}")

        player_attack = player.attack_enemy()
        enemy_attack = enemy.attack_player()

        print(f"{player.name} attacks for {player_attack} damage!")
        enemy.take_damage(player_attack)

        if enemy.is_alive():
            print(f"{enemy.name} attacks for {enemy_attack} damage!")
            player.take_damage(enemy_attack)

    if player.is_alive():
        print(f"{player.name} defeated {enemy.name}!")
        player.gold += enemy.gold_reward
        print(f"{player.name} received {enemy.gold_reward} gold.")
        player.heal()
        print(f"{player.name} healed 20 HP.")
    else:
        print(f"{player.name} was defeated by {enemy.name}... Game Over!")

def main():
    print("Welcome to The Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    while player.is_alive():
        enemy = Enemy("Goblin", 30, 8, 20)
        battle(player, enemy)
        if player.is_alive():
            player.level += 1
            print(f"{player.name} leveled up to level {player.level}!")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
