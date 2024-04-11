import random
from characters import Player, Enemy
from shop import Shop, Item
from quests import Quest, QuestManager
from utils import generate_random_name, print_separator, display_player_status, display_enemy_status

def battle(player, enemy):
    """Simulate a battle between player and enemy."""
    print(f"A wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        print_separator()
        display_player_status(player)
        display_enemy_status(enemy)
        print_separator()

        player_attack = player.attack_enemy()
        enemy_attack = enemy.attack_player()

        print(f"{player.name} attacks for {player_attack} damage!")
        enemy.take_damage(player_attack)

        if enemy.is_alive():
            print(f"{enemy.name} attacks for {enemy_attack} damage!")
            player.take_damage(enemy_attack)

    if player.is_alive():
        print(f"{player.name} defeated {enemy.name}!")
        player.receive_gold(enemy.gold_reward)
        player.heal()
        print(f"{player.name} healed 20 HP.")
    else:
        print(f"{player.name} was defeated by {enemy.name}... Game Over!")

def main():
    """Main function to run the game."""
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
        enemy = Enemy(generate_random_name(), random.randint(20, 50), random.randint(5, 15), random.randint(10, 30))
        battle(player, enemy)
        if player.is_alive():
            player.level += 1
            print(f"{player.name} leveled up to level {player.level}!")
            quest_manager.complete_quest("Defeat the Goblin")  # Mark quest as completed
            if quest_manager.quests_completed() == 2:
                print("Congratulations! You completed all quests.")
                break
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

