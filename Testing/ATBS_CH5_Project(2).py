'''
###########################################
## Automate the Boring Stuff with Python ##
## CH5 Practice Project                  ##
###########################################

Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the inventory
parameter is a dictionary representing the player’s inventory (like in the previous project)
and the addedItems parameter is a list like dragonLoot. The addToInventory() function should
return a dictionary that represents the updated inventory. Note that the addedItems list can
contain multiples of the same item. Your code could look something like this:

def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

The previous program (with your displayInventory() function from the previous project)
would output the following:

Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
'''

# inventory of player's items
playerInv = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

# function prints key:value pairs representing player's inventory
def displayInventory(inventory):
    totalItems = 0 # initialize variable. will track total number of items in inventory
    print('Items in your inventory:')
    for k, v in inventory.items(): # iterate through dictionary items
        inventory.get(k, 0) # check if given key:value pair exists. if not, set to zero
        totalItems += v # increment totalItems with every item in the dictionary
        print(k, v) # print each key:value pair

    print('You have ' + str(totalItems) + ' total items')
    

# function should return a dict representing the updated inventory
# inventory is a dict representing the player's inventory
# addedItems is a list like dragonLoot. NOTE: Can contain multiples of the same item
def addToInventory(inventory, addedItems):
    totalItems = 0
    '''
    #################
    ## PSUEDO CODE ##
    #################

    For each item in the dragonLoot list
        If the item from dragonLoot (addedItems) exists as a key in playerInv (inventory), add 1 to the dict. value
        Else, create the key:value pair in playerInv (inventory) and add 1 to totalItems
    Print the updated playerInv (inventory) as well as the total number of items (totalItems)
    '''


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
playerInv = addToInventory(playerInv, dragonLoot)


displayInventory(playerInv)
