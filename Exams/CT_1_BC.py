# ## Task - 1 (E-Mart):
# class Item:
#     def __inti__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.amount = 0

#     def __str__(self):
#         return f"Item name: {self.name}; Price: {self.price}; Quantity: {self.quantity}"

#     def add_to_cart(self, cart, amount):
#         self.amount = amount
        

    

# class Cart:
#     def __init__(self, order_id):
#         self.order_id = order_id
#         self.item_list = []

#     def remove_item(self, item):
#         self.item_list.remove(item)

#     def display_items(self):
#         print(f"Items in the cart: ")
#         print(*self.item_list)

# cart = Cart("76372")
# cart.display_items()
# alu = Item("Alu", 230, "1kg")
# cart.item_list.append(alu)




## Task - 2: Fantastic Beasts and How to Encapsulate Them-
class Beasts:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hunger_level = 50
        self.happiness_level = 50

    def __str__(self):
        return f"Name: {self.name} \nType: {self.type} \nHunger: {self.hunger_level}% \nHappiness: {self.happiness_level}"
    
class Owner:
    pass