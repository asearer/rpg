class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display_info(self):
        print(f"{self.name}: {self.description} - Price: {self.price} gold")


class Shop:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        print("Items available in the shop:")
        for index, item in enumerate(self.items):
            print(f"{index + 1}. ", end="")
            item.display_info()

    def buy_item(self, item_index, player):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            if player.gold >= item.price:
                player.gold -= item.price
                player.inventory.add_item(item)
                print(f"You bought {item.name}.")
            else:
                print("Not enough gold to buy this item.")
        else:
            print("Invalid item index.")


# Example usage:
# shop = Shop()
# shop.add_item(Item("Health Potion", "Restores 20 HP", 10))
# shop.add_item(Item("Sword", "Deals extra damage", 50))
# shop.display_items()
# shop.buy_item(1, player)
