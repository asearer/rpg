class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, player):
        pass  # Placeholder method for using the item


class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion", "Restores 20 HP")

    def use(self, player):
        player.heal()


class Inventory:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"You obtained {item.name}.")
        else:
            print("Inventory is full.")

    def use_item(self, item_index, player):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            item.use(player)
            del self.items[item_index]
            print(f"You used {item.name}.")
        else:
            print("Invalid item index.")



# Example usage:
# health_potion = HealthPotion()
# inventory = Inventory()
# inventory.add_item(health_potion)
# inventory.use_item(0, player)
