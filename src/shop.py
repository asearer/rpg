class Item:
    def __init__(self, name, description, price, quantity=1):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"{self.name}: {self.description} - Price: {self.price} gold")

    def reduce_quantity(self, amount=1):
        self.quantity -= amount
        if self.quantity < 0:
            self.quantity = 0


class Shop:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        # Check if the item already exists in the shop
        existing_item = next((x for x in self.items if x.name == item.name), None)
        if existing_item:
            existing_item.quantity += quantity
        else:
            item.quantity = quantity
            self.items.append(item)

    def display_items(self):
        print("Items available in the shop:")
        for index, item in enumerate(self.items):
            print(f"{index + 1}. ", end="")
            item.display_info()

    def buy_item(self, item_index, player, quantity=1):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            total_price = item.price * quantity
            if player.gold >= total_price and item.quantity >= quantity:
                player.gold -= total_price
                player.inventory.add_item(item, quantity)
                item.reduce_quantity(quantity)
                print(f"You bought {quantity} {item.name}.")
            elif player.gold < total_price:
                print("Not enough gold to buy this quantity of items.")
            else:
                print("Not enough items available in the shop.")
        else:
            print("Invalid item index.")


# Example usage:
# shop = Shop()
# shop.add_item(Item("Health Potion", "Restores 20 HP", 10), quantity=5)
# shop.add_item(Item("Sword", "Deals extra damage", 50))
# shop.display_items()
# shop.buy_item(1, player)

