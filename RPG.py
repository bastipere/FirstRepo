
#RPG GAME TEST

# Define the Player class
class Player:
    def __init__(self, name, role, level, hp, attack, magic, defense):
        self.name = name
        self.role = role
        self.level = level
        self.hp = hp
        self.attack = attack
        self.magic = magic
        self.defense = defense

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

# Role assignment
if player_role == 1:
    player_role = 'Warrior'
    player_hp += 15
    player_attack = 10
    player_magic -= 5
    player_defense += 10
elif player_role == 2:
    player_role = 'Mage'
    player_hp = 10
    player_attack -= 5
    player_magic += 10
    player_defense = 10
elif player_role == 3:
    player_role = 'Archer'
    player_hp -= 15
    player_attack += 10
    player_magic = 10
    player_defense -= 5
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

# Create the player object
player1 = Player(player_name, player_role, 1, player_hp, player_attack, player_magic, player_defense)

#print(f'\nWelcome {player1.name}, you have chosen the role of {player1.role}.')

details(player1)

print('\nYour adventure begins now!')

enter = input('\nPress Enter to continue ')

if enter == '':
    print('\nYou find yourself in a dark forest. The trees are tall and the path ahead is unclear.')
    print('Suddenly, you hear a rustling in the bushes. A wild goblin appears!')
    