import random

def generate_random_name():
    """Generate a random name for enemies."""
    adjectives = ["Vicious", "Fierce", "Sneaky", "Cunning", "Mighty", "Swift"]
    nouns = ["Goblin", "Orc", "Bandit", "Troll", "Skeleton", "Dragon"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def print_separator():
    """Print a separator line."""
    print("-" * 30)

def display_player_status(player):
    """Display player's status."""
    print(f"Player: {player.name} | Level: {player.level} | HP: {player.hp}/{player.max_hp} | Gold: {player.gold}")

def display_enemy_status(enemy):
    """Display enemy's status."""
    print(f"Enemy: {enemy.name} | HP: {enemy.hp}/{enemy.max_hp} | Attack: {enemy.attack}")

