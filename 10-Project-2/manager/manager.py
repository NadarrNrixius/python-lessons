def use_item(inventory, name, count):
    for key in inventory.keys():
        if key == name:
            name_exists = True
    if name_exists == False:
        pass
    elif inventory[name] - count < 0:
        pass
    else:
        inventory[name] -= count

def stock_item(inventory, name, count):
    name_exists = False
    for key in inventory.keys():
        if key == name:
            name_exists = True
    if name_exists:
        inventory[name] += count
    else:
        inventory[name] = count

def item_amount(inventory, name):
    return(inventory[name])

def is_stocked(inventory, name):
    if inventory[name] > 0:
        return True
    else:
        return False

def has_enough(inventory, name, count):
    if inventory[name] >= count:
        return True
    else:
        return False

def in_history(inventory, name):
    name_exists = False
    for key in inventory.keys():
        if key == name:
            name_exists = True
    return name_exists

def current_inventory(inventory):
    list1 = []
    for key in inventory.keys():
        if key > 0:
            list1.append(key)
    return list1

def report(inventory):
    for key in inventory.keys():
        return '{}: {}\n'.format(key, inventory[key])