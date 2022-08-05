# it did not save 😭😭 i spent hours
# always do git repo
# i will have to write this back  from memory
# i cant remember
# i had luckily saved some of the functions
# ALWAYS DO VERSION CONtrol AND GIt

from os import system
import random
import time
import click
import json
import os.path
import sys

game = {
  "gold":100,
  
  "player_inventory":{
  "sword":{"quantity":0},
  "shield":{"quantity":0},
  "magic staff":{"quantity":0},
  "health potion":{"quantity":0},
  "magic potion":{"quantity":0},
  "magic feather":{"quantity":0},
  "dragon scale":{"quantity":0}},
  
  "shop_inventory":{
  "sword":{"quantity":3, "value":50},
  "shield":{"quantity":6, "value":30},
  "magic staff":{"quantity":1, "value":500},
  "health potion":{"quantity":5, "value":75},
  "magic potion":{"quantity":4, "value":100}},

  "password":""
}

system("clear")

usr_input = int(input("Which save file? >> "))
print("")
path = "saves/save" + str(usr_input) + ".json"
if os.path.exists(path) == True:
  
  
  with open(path, "r") as save_file:
    temp_game = json.load(save_file)
    usr_input1 = input("Please enter the password for save file " + str(usr_input) + " >> ")
    if usr_input1 == temp_game["password"]:
      game = temp_game
      print("Save file " + str(usr_input) + " selected.")
    else:
      sys.exit("Wrong password.")
else:
  print("No save file " + str(usr_input) + " found.")
  with open(path, "w") as save_file: 
    game["password"] = input("Please enter a new password for save file " + str(usr_input) + " >> ")
    json.dump(game, save_file)
  print("Save file " + str(usr_input) + " created.")

print("\n")
    
#mob_list = ["chicken", "goblin", "loot_goblin", "bandit", "mage", "dragon"]
# chicken drops 1-5 gold small chance to drop magic feather
# goblin drop 10-25 gold small chance to drop sword and shield
# loot goblin drops 100-250 gold
# bandit drops 15-20 gold medium chance to drop sword, shield and a small chance to drop healtht potion
# mage drops 25-50 gold high chance to drop magic potion, tiny chance to drop magic staff
# dragon has a very small chance to spawn a a 50% chance to kill you(loosing all your gold) drops 100-500 gold, and can drop anything



def print_gold():#Prints amount of gold in a neat way
    print ("Gold >>", u"\u001b[38;5;" + "226" + "m" +  str(game["gold"]), u"\u001b[38;5;" + "255" + "m" + "<<")
    print ("")


def dead():#function for dying
  global game
  system("clear")
  print_gold()
  print(u"\u001b[38;5;" + "1" + "m" + "You died.")
  rand = random.randint(0, game["gold"])
  game["gold"] -= rand
  print("")
  print("You lost", rand, "gold.")
  print(u"\u001b[38;5;" + "255" + "m" + "")
  print("Time left untill you recover.")
  with click.progressbar(length=30) as bar:
    for length in bar:
        time.sleep(1)
  print("")
  
def chicken_loot():#Function for chickens loot
  global game
  got_drop = False
  print("")
  fighting = "Fighting"
  for i in range(5):
    print(fighting)
    fighting = fighting + "."
    time.sleep(1)
  print("")
  if(random.random() < 0.8):
    got_drop = True
    rand = random.randint(1,5)
    game["gold"] += rand
    print("You got", rand, "gold.")
    print("")
    print("You now have", game["gold"], "gold.")
  if(random.random() < 0.075):
    got_drop = True
    game["gold"] += random.randint(1,5)
    game["player_inventory"]["magic feather"]["quantity"] += 1
    print("You got a rare drop!! (Magic Feather)")
  if got_drop != True:
    dead()

def goblin_loot():
  global game
  got_drop = False
  fighting = "Fighting"
  for i in range(5):
    print(fighting)
    fighting = fighting + "."
    time.sleep(1)
  print("")
  if(random.random() < 0.8):
    got_drop = True
    rand = random.randint(10,25)
    game["gold"] += rand
    print("You got", rand, "gold.")
    print("")
    print("You now have", game["gold"], "gold.")
  if(random.random() < 0.15):
    got_drop = True
    game["player_inventory"]["sword"]["quantity"] += 1
    print("You got a rare drop!! (Sword)")
  if(random.random() < 0.15):
    got_drop = True
    game["player_inventory"]["shield"]["quantity"] += 1
    print("You got a rare drop!! (Shield)")
  if got_drop != True:
    dead()

def loot_goblin_loot():
  global game
  got_drop = False
  if(random.random() < 0.8):
    got_drop = True
    rand = random.randint(25, 75)
    game["gold"] += rand
    print("You got", rand, "gold.")
    print("")
  if(random.random() < 0.1):
    got_drop = True
    rand = random.randint(50,100)
    game["gold"] += rand
    print("You got", rand, "gold.")
    print("")
  if(random.random() < 0.01):
    got_drop = True
    rand = random.randint(200,250)
    game["gold"] += rand
    print("You got a rare drop!! >>", rand, "Gold <<")
    print("")
  if got_drop == True:
    print("You now have", game["gold"], "gold.")
  else:
    dead()
    






def bandit_loot():
  global game
  got_drop = False
  
  if(random.random() < 0.8):
    got_drop = True
    fighting = "Fighting"
    for i in range(5):
      print(fighting)
      fighting = fighting + "."
      time.sleep(1)
    print("")
    rand = random.randint(15,20)
    game["gold"] += rand
    print("You got", rand, "gold.")
    print("")
    print("You now have", game["gold"], "gold.")
    print("")
  if(random.random() < 0.25):
    got_drop = True
    game["player_inventory"]["sword"]["quantity"] += 1
    print("You got a drop!! (Sword)")
    print("")
  if(random.random() < 0.25):
    got_drop = True
    game["player_inventory"]["shield"]["quantity"] += 1
    print("You got a drop!! (Shield)")
    print("")
  if(random.random() < 0.05):
    got_drop = True
    game["player_inventory"]["health potion"]["quantity"] += 1
    print("You got a rare drop!! (Health Potion)")
    print("")
  if got_drop != True:
    dead()


def mage_loot():
  global game
  got_drop = False
  fighting = "Fighting"
  for i in range(5):
    print(fighting)
    fighting = fighting + "."
    time.sleep(1)
  print("")
  if(random.random() < 0.8):
    got_drop = True
    rand = random.randint(25,50)
    game["gold"] += rand
    print("You got", rand, "gold.")
    print("")
    print("You now have", game["gold"], "gold.")
  if(random.random() < 0.35):
    got_drop = True
    game["player_inventory"]["magic potion"]["quantity"] += 1
    print("You got a drop!! (Magic Potion)")
  if(random.random() < 0.05):
    got_drop = True
    game["player_inventory"]["magic staff"]["quantity"] += 1
    print("You got a rare drop!! (Magic Staff)")
  if got_drop != True:
    dead()

def dragon_loot():
  global game
  fighting = "Fighting"
  for i in range(10):
    print(fighting)
    fighting = fighting + "."
    time.sleep(1)
  print("")
  if random.random() < 0.5:
    if(random.random() < 0.8):
      rand = random.randint(100,250)
      game["gold"] += rand
      print("You got", rand, "gold.")
      print("")
      print("You now have", game["gold"], "gold.")
    if(random.random() < 0.15):
      game["player_inventory"]["sword"]["quantity"] += 1
      print("You got a rare drop!! (Sword)")
    if(random.random() < 0.01):
      game["player_inventory"]["dragon scale"]["quantity"] += 1
      print("You got a super rare drop!! (Dragon Scale)")
  else:
    dead()




def inv_print(display_txt, inventory):
  #total 16 wo >> 14
  item = display_txt.lower()
  while len(display_txt) < 14:
    display_txt = display_txt + " "
  display_txt = display_txt + ">>"
  if inventory == game["shop_inventory"]:
    print(display_txt, inventory[item]["quantity"], "<<   >>", inventory[item]["value"], "<<")
  else:
    print(display_txt, inventory[item]["quantity"], "<<")

def shop():
    global buy, game
    system("clear")
    print_gold()
    print("             ↓ Stock ↓  ↓ Price ↓")
    inv_print("Sword", game["shop_inventory"])
    inv_print("Shield", game["shop_inventory"])
    inv_print("Magic Staff", game["shop_inventory"])
    inv_print("Health Potion", game["shop_inventory"])
    inv_print("Magic Potion", game["shop_inventory"])
    print("")
    buy = input("Would you like to buy something? y/n >> ")
    if buy == "y":
        usr_input = input("What would you like to buy? >> ")
        usr_input = usr_input.lower()
        if game["shop_inventory"][usr_input]["quantity"] > 0:
            game["shop_inventory"][usr_input]["quantity"] -= 1
            game["gold"] -= game["shop_inventory"][usr_input]["value"]
            game["player_inventory"][usr_input]["quantity"] += 1
            print("")
            print("You have", game["gold"], "gold left.")
        else:
            print("There is no", usr_input, "in stock.")


print_gold()

while(True):
  usr_input = input("What would you like to do? (hunt, go shopping, see inventory, settings) >> ")
  usr_input = usr_input.lower()
  if usr_input == "hunt" or usr_input == "h":
    system("clear")
    print_gold()
    rand = random.random()
    if rand < 0.3:
      print("You encountered a Chicken.")
      print("")
      chicken_loot()
    elif rand < 0.5:
      print("You encountered a Goblin.")
      print("")
      goblin_loot()
    elif rand < 0.8:
      print("You encountered a Loot Goblin.")
      print("")
      loot_goblin_loot()
    elif rand < 0.9:
      print("You encountered a Bandit.")
      print("")
      bandit_loot()
    elif rand < 0.975:
      print("You encountered a Mage.")
      print("")
      mage_loot()
    elif rand < 1.0:
      print("You encountered a Dragon.")
      print("")
      dragon_loot()
    print("")

  elif usr_input == "go shopping" or usr_input == "s":
    shop()
  elif usr_input == "see inventory" or usr_input == "i":
    system("clear")
    print_gold()
    print("            ↓ Quantity ↓")
    inv_print("Sword", game["player_inventory"])
    inv_print("Shield", game["player_inventory"])
    inv_print("Magic Staff", game["player_inventory"])
    inv_print("Health Potion", game["player_inventory"])
    inv_print("Magic Potion", game["player_inventory"])
    if game["player_inventory"]["magic feather"]["quantity"] > 0:
      inv_print("Magic Feather", game["player_inventory"])
    if game["player_inventory"]["dragon scale"]["quantity"] > 0:
      inv_print("Dragon Scale", game["player_inventory"])

  elif usr_input == "settings" or usr_input == "g":
    system("clear")
    print("Settings")
    print("")
    print("None. (0)")
    print("Delete save file. (1)")
    print("Change password. (2)")
    print("Save. (3)")
    print("")
    usr_input = input("Which setting would you like to change? >> ")
    if usr_input == "1" or usr_input == "Delete save file":
      usr_input = input("Are you sure? y/n >> ")
      if usr_input == "y":
        sys.remove(path)
    elif usr_input == "2" or usr_input == "Change password":
      usr_input = input("Enter current password. >> ")
      if usr_input == game["password"]:
        usr_input = input("Enter new password. >> ")
        game["password"] = usr_input
    elif usr_input == "Save" or usr_input == "3":
      with open(path, "w") as save_file:
        json.dump(game, save_file)
      
  print("")


  
  

