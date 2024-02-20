# Define the rooms and their connections
rooms = {
    'Castle Courtyard': {'name': 'Castle Courtyard',
                         'west': 'Sorcerer Sanctum', 'east': 'Mage Tower',
                         'north': 'Enchanted Forest', 'south': 'Elven Village',
                         'text': 'You are in the Castle Courtyard.'},

    'Elven Village': {'name': 'Elven Village', 'east': 'Dwarven Mines', 'north': 'Castle Courtyard',
                      'text': 'You are in the Elven Village.', 'items': ['Elven Bow']},

    'Dwarven Mines': {'name': 'Dwarven Mines', 'west': 'Elven Village',
                      'text': 'You are in the Dwarven Mines', 'items': ['Dwarven Hammer']},

    'Sorcerer Sanctum': {'name': 'Sorcerer Sanctum', 'east': 'Castle Courtyard',
                         'text': 'You are in the Sorcerer Sanctum', 'items': ['Elixir of Healing']},

    'Mage Tower': {'name': 'Mage Tower', 'west': 'Castle Courtyard', 'north': 'Dragon Lair',
                   'text': 'You are in the Mage Tower', 'items': ['Sorcerer Crystal']},

    'Dragon Lair': {'name': 'Dragon Lair', 'south': 'Mage Tower',
                    'text': 'You are in the Dragon Lair', 'items': ['Dragon Scale Armor']},

    'Enchanted Forest': {'name': 'Enchanted Forest', 'east': 'Final Showdown', 'south': 'Castle Courtyard',
                         'text': 'You are in the Enchanted Forest'},

    'Final Showdown': {'name': 'Final Showdown', 'west': 'Enchanted Forest',
                       'text': 'You are in the Final Showdown'}
}

# Define valid directions
directions = ['north', 'south', 'east', 'west']

# Define Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} is not in the inventory.")

    def show_inventory(self):
        print(f"Inventory of {self.name}:")
        for item in self.inventory:
            print(item)

# Function to determine the possible directions the player can move from the current room.
def possible_directions(current_room):
    directions_available = []
    for direction in directions:
        if direction in current_room:
            directions_available.append(direction)
    return directions_available

# Function to display player's status and possible commands
def display_status(player, current_room):
    print(f"You are in {current_room['name']}")
    print(f"Inventory: {player.inventory}")
    print(f"Possible moves:", possible_directions(current_room))
    if 'items' in current_room:
        print(f"You see: {', '.join(current_room['items'])}")
    else:
        print("You see nothing of value.")
    print("-" * 20)

# Game narrative and rules
print("Welcome to the Adventure Game!")
print("In this game, you'll explore various locations to collect items needed for the Final Showdown.")
print("You start in the Castle Courtyard.")
print("Your goal is to collect the following items:")
print("- Elixir of Healing from Sorcerer Sanctum")
print("- Dragon Scale Armor from Dragon Lair")
print("- Sorcerer Crystal from Mage Tower")
print("- Elven Bow from Elven Village")
print("- Dwarven Hammer from Dwarven Mines")
print("To change rooms, enter a direction. Example: 'east' to move east.")
print("To pick up an item you see in a room you are in, the command is 'take'. Example: 'take Elven Bow'")
print("You need all the items to win the game. Enter 'quit' to exit the game at any time.\n")

# Get player name
player_name = input("Enter your name: ")
player = Player(player_name)

current_room = rooms['Castle Courtyard']

# Gameplay loop
while True:
    if current_room['name'] == 'Final Showdown':
        if all(item in player.inventory for item in
               ['Elixir of Healing', 'Dragon Scale Armor', 'Sorcerer Crystal', 'Elven Bow', 'Dwarven Hammer']):
            print('Congratulations! You have collected all items and defeated the dragon!')
            print('Thanks for playing the game. Hope you enjoyed it.')
        else:
            print('NOM NOM...GAME OVER!')
            print('Thanks for playing the game. Hope you enjoyed it.')
        break

    # Display player's status and possible commands
    display_status(player, current_room)

    # Get user input
    command = input('Enter your move: ')

    # Movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            print('You cannot go that way.')

    # Quit game
    elif command == 'quit':
        print('Thanks for playing!')
        break

    # Add item to player's inventory
    elif command.startswith('take '):
        item_name = command[5:]  # Extract the item name from the command
        room_items = current_room.get('items', [])
        if item_name in room_items:
            player.add_item(item_name)
            room_items.remove(item_name)
            current_room['items'] = room_items  # Update the room's items
        else:
            print(f"There is no {item_name} in this room.")

    # Show player's inventory
    elif command == 'inventory':
        player.show_inventory()

    # Bad command
    else:
        print('Invalid input.')
