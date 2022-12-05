import restaurant.finance
import restaurant.inventory

class POS:
    def __init__(self, balance, inventory, menu):
        self._balance = restaurant.finance.Finance(balance)
        self._inventory = restaurant.inventory.Inventory(inventory)
        self._menu = menu

    def take_customer_order(self, dish):
        #if inventory is available, and dish is on menu, subtract the inventory, according to the ingredients, and add the profit to the finance manager. Returns True on success, False otherwise

        on_menu = False
        enough_ingredients = True
        can_order = True
        bal = 0

        for key in self._menu.keys():
            if dish == key:
                on_menu = True
        
        if on_menu == True:
            for key in self._menu[dish].ingredients.keys():
                item_amount = self._inventory.amount(key)
                if self._menu[dish].ingredients[key] > item_amount:
                    enough_ingredients = False
        else:
            can_order = False
        
        if enough_ingredients == True and can_order == True:
            for key in self._menu[dish].ingredients.keys():
                self._inventory.use(key, self._menu[dish].ingredients[key])
            self._balance.credit(self._menu[dish].price)
        else:
            can_order = False

        if can_order == True:
            return True
        else:
            return False

    def place_restock_order(self, items, catalogue):
        #add items to inventory, if there is enough money to pay for it, according to the finance manager. If an item is not in the catalogue, skip over it. Do nothing if there are not enough funds. Prices are gotten from the catalogue(key: ingredient name, value: cost). Returns False if the order fails completely, True otherwise
        
        cost = 0

        for item in items.keys():
            for key in catalogue.keys():
                if item == key:
                    for amount in range(0,items[item]):
                        cost += catalogue[key]

        order_complete = self._balance.debit(cost)

        if order_complete == True:
            for item in items.keys():
                for key in catalogue.keys():
                    if item == key:
                        self._inventory.stock(item, items[item])
            return True
        else:
            return False

    def menu(self):
        #returns the restaurant's menu as a dictionary (key: dish name, value: price)

        out_menu = {}
        name = ''
        price = 0

        for dish in self._menu.keys():
            name = dish
            price = self._menu[dish].price
            out_menu[name] = price
        
        return out_menu

    def inventory(self):
        #returns the full inventory, including items that are out of stock (key: item name, value: amount)

        return self._inventory.full_inventory()

    def balance(self):
        #returns the current balance of finance

        return self._balance.balance()