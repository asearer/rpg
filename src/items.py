class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, player):
        pass  # Placeholder method for using the item


class HealthPotion(Item):
    def __init__(self, heal_amount=20):
        super().__init__("Health Potion", "Restores 20 HP")
        self.heal_amount = heal_amount

    def use(self, player):
        player.heal(self.heal_amount)


class ManaPotion(Item):
    def __init__(self, restore_amount=20):
        super().__init__("Mana Potion", "Restores 20 MP")
        self.restore_amount = restore_amount

    def use(self, player):
        player.restore_mana(self.restore_amount)


class Inventory:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def add_item(self, item, quantity=1):
        for _ in range(quantity):
            if len(self.items) < self.capacity:
                self.items.append(item)
                print(f"You obtained {item.name}.")
            else:
                print("Inventory is full.")
                return

    def use_item(self, item_index, player):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            item.use(player)
            del self.items[item_index]
            print(f"You used {item.name}.")
        else:
            print("Invalid item index.")


class Player:
    def __init__(self, name, max_hp=100, max_mana=100):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_mana = max_mana
        self.mana = max_mana

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} healed for {amount} HP. Current HP: {self.hp}/{self.max_hp}")

    def restore_mana(self, amount):
        self.mana = min(self.max_mana, self.mana + amount)
        print(f"{self.name} restored {amount} MP. Current MP: {self.mana}/{self.max_mana}")


# Example usage:
player = Player("Player1", max_hp=120, max_mana=80)
inventory = Inventory()

health_potion = HealthPotion()
mana_potion = ManaPotion()

inventory.add_item(health_potion)
inventory.add_item(mana_potion)

inventory.use_item(0, player)
inventory.use_item(0, player)

