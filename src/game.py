import random
from characters import Player, Enemy
from shop import Shop, Item
from quests import Quest, QuestManager

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
    shop = Shop()
    quest_manager = QuestManager()

    # Initialize quests
    quest1 = Quest("Defeat the Goblin", "Defeat the Goblin terrorizing the village.", 50)
    quest2 = Quest("Retrieve the Artifact", "Retrieve the ancient artifact hidden in the cave.", 100)
    quest_manager.add_quest(quest1)
    quest_manager.add_quest(quest2)

    # Initialize shop items
    shop.add_item(Item("Health Potion", "Restores 20 HP", 10))
    shop.add_item(Item("Sword", "Deals extra damage", 50))

    while player.is_alive():
        enemy = Enemy("Goblin", 30, 8, 20)
        battle(player, enemy)
        if player.is_alive():
            player.level += 1
            print(f"{player.name} leveled up to level {player.level}!")
            shop.display_items()
            choice = input("Enter the index of the item you want to buy (or 'q' to quit): ")
            if choice.lower() == 'q':
                break
            try:
                item_index = int(choice) - 1
                shop.buy_item(item_index, player)
            except ValueError:
                print("Invalid input.")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
