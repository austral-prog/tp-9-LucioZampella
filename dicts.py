
def create_inventory(items):
    dictt = dict()
    inventario = []
    for i in items:
        inventario.append(i)
    for a in inventario:
        if a in dictt:
            dictt[a] += 1
        else:
            dictt[a] = 1
    return dictt
print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

def add_items(inventory, items):
    for i in items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))



def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory

print(decrement_items({"coal": 3, "diamond": 1, "iron": 5}, ["diamond", "coal", "iron", "iron"]))

def remove_item(inventory, item):
        if item in inventory:
            del inventory[item]
        return inventory
print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))


def list_inventory(inventory):
    keys_to_remove = [key for key, value in inventory.items() if value == 0]
    for key in keys_to_remove:
        del inventory[key]
    return list(inventory.items())

print(list_inventory({"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0}))

