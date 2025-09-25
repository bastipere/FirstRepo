#RPG GAME TEST

# Define the Player class
class Player:
    def __init__(self, name, role, level, hp, attack, magic, defense, weapon_name):
        self.name = name
        self.role = role
        self.level = level
        self.hp = hp
        self.attack = attack
        self.magic = magic
        self.defense = defense
        self.weapon_name = weapon_name

# Define the Weapon class        
class Weapon:
    def __init__(self, weapon_name, type, damage, magic_damage):
        self.weapon_name = weapon_name
        self.type = type
        self.damage = damage
        self.magic_damage = magic_damage

# Game introduction
print("Welcome to the RPG Game!")
star = input("\nPress Enter to start ")

# Character creation
player_name = input("\nEnter your character's name: ")
player_role = int(input("\nChoose your role \n1)Warrior \n2)Mage \n3)Archer \n"))
player_hp = 100
player_attack = 10
player_magic = 10
player_defense = 10
weapon_name = ''

# Role assignment
if player_role == 1:
    player_role = 'Warrior'
    player_hp += 15
    player_attack = 10
    player_magic -= 5
    player_defense += 10
    weapon_name = 'Wood Sword'
elif player_role == 2:
    player_role = 'Mage'
    player_hp = 10
    player_attack -= 5
    player_magic += 10
    player_defense = 10
    weapon_name = 'Wood Staff'
elif player_role == 3:
    player_role = 'Archer'
    player_hp -= 15
    player_attack += 10
    player_magic = 10
    player_defense -= 5
    weapon_name = 'Bow'
else:
    print('Invalid option, default role assigned: Warrior')

# Function to display player details
def details(self):
    print('\nName: ' + self.name)
    print('Role: ' + self.role)
    print('Level: ' + str(self.level))
    print('HP: ' + str(self.hp))
    print('Attack: ' + str(self.attack))
    print('Magic: ' + str(self.magic))
    print('Defense: ' + str(self.defense))
    print('Weapon: ' + str(self.weapon_name))   



# Create the player object
player1 = Player(player_name, player_role, 1, player_hp, player_attack, player_magic, player_defense, weapon_name)

# Create the weapon object
warrior_weapon = Weapon(weapon_name, 'Melee', 15, 0)
mage_weapon = Weapon(weapon_name, 'Magic', 5, 15)
archer_weapon = Weapon(weapon_name, 'Ranged', 10, 5)

# Show player details
details(player1)

# Show weapon details
weapon_details = input('\nPress E to see your weapon details ')
def weapon_details(self):
    print('\nWeapon Name: ' + self.weapon_name)
    print('Type: ' + self.type)
    print('Damage: ' + str(self.damage))
    print('Magic Damage: ' + str(self.magic_damage))

if player_role == 'Warrior' and weapon_details == 'E' or 'e':
    weapon_details(warrior_weapon)
elif player_role == 'Mage' and weapon_details == 'E' or 'e':
    weapon_details(mage_weapon)
elif player_role == 'Archer' and weapon_details == 'E' or 'e':
    weapon_details(archer_weapon)
else:
    print('\nYour adventure begins now!')

# Continue the adventure
enter = input('\nPress Enter to continue ')

if enter == '':
    print('\nYou find yourself in a dark forest. The trees are tall and the path ahead is unclear.')
    print('Suddenly, you hear a rustling in the bushes. A wild goblin appears!')

print('\nTo be continued...')  