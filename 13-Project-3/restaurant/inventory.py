class Inventory:
    def __init__(self, inventory):
        self.inv = inventory

    def use(self, name, count):
        #subtract an item from the inventory, if it exists and there is enough

        for key in self.inv.keys():
            if key == name:
                if self.inv[key] >= count:
                    self.inv[key] -= count

    def stock(self, name, count):
        #add an item to the inventory, even if it hasn't been ordered before

        key_exists = False

        for key in self.inv.keys():
            if key == name:
                key_exists = True

        if key_exists:
            self.inv[key] += count
        else:
            self.inv[name] = count

    def amount(self, name):
        #return the current amount of the item. if the item isn't in the inventory, return None

        key_exists = False

        for key in self.inv.keys():
            if key == name:
                key_exists = True
        
        if key_exists:
            return self.inv[name]
        else:
            return None

    def is_stocked(self, name):
        #return a boolean indicating if the item is stocked or not

        key_exists = False

        for key in self.inv.keys():
            if key == name:
                key_exists = True
                if self.inv[name] > 0:
                    return True
                else:
                    return False

        if key_exists:
            pass
        else:
            return False

    def has_enough(self, name, count):
        #return a boolean indicating if there are at least count items in stock

        key_exists = False

        for key in self.inv.keys():
            if key == name:
                key_exists = True
                if self.inv[name] >= count:
                    return True
                else:
                    return False
        
        if key_exists:
            pass
        else:
            return False

    def in_history(self, name):
        #return a boolean indicating if the item has ever been stocked

        key_exists = False

        for key in self.inv.keys():
            if key == name:
                key_exists = True
        
        return key_exists

    def current_inventory(self):
        #returns a dictionary of the items currently in stock, including amounts

        dict1 = {}

        for key in self.inv.keys():
            if self.inv[key] > 0:
                dict1[key] = self.inv[key]
        
        return dict1

    def full_inventory(self):
        #returns a dictionary of all items, both in and out of stock

        return self.inv