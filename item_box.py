def display_inventory(inventory):
    print("Inventory :")
    item_total =0
    for k,v in inventory.items():
        print(v, k)
        item_total += v
    print("total item: " + str(item_total))


stuff = {"knife" :1, "test" : 4526}
display_inventory(stuff)


