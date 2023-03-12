import json, time, random, os, sys
from src.lib import keys
from src.lib import color
from src.lib import rareity
from src.lib import randomRarityItem as RRI
#  RandomRarityItem adds
#  support for sudo randomly sellected items baced on
#  level



path = "./src"
f = open("./src/config/config.json")
data = json.load(f)
f.close()

with open("./src/config/config.json", "r") as f:
  data = json.load(f)

# Loads config data
version = data["config"]["version"]

del data


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


path = "./src"
#f = open(f'{path}/appdata/items.json')
#items = json.load(f)
#f.close()

f = open("./src/data/UserData.json")
userData = json.load(f)
f.close()


def save(name: str, data: str):
  f = open('./src/data/UserData.json')
  userData = json.load(f)
  f.close()

  userData[name] = data

  json_object = json.dumps(userData, indent=4)
  with open("./src/data/UserData.json", "w") as f:
    f.write(json_object)


def load(name: str):
  f = open('./src/data/UserData.json')
  userData = json.load(f)
  f.close()

  return userData[name]


logo = f"""
{color.OKGREEN} _    _  _  _      _ 
| |  | |(_)| |    | |{color.BROWN}
| |  | | _ | |  __| |
| |/\| || || | / _` |
\  /\  /| || || (_| |
 \/  \/ |_||_| \__,_|{color.ENDC}
            V {version}


"""

winIcon = f"""

{color.BLUE}More {color.GREEN}Items{color.BLUE} / {color.FAIL}Enemys {color.BLUE}coming soon{color.WARNING}!!!
{color.GREEN}
 __      __                          __       __  __           
|  \\    /  \\                        |  \\  _  |  \\|  \\          
 \\$$\  /  $$______   __    __       | $$ / \\ | $$ \$$ _______  
  \\$$\/  $$/      \ |  \\  |  \\      | $$/  $\\| $$|  \|       \\ 
   \\$$  $$|  $$$$$$\| $$  | $$      | $$  $$$\ $$| $$| $$$$$$$\\
    \\$$$$ | $$  | $$| $$  | $$      | $$ $$\\$$\$$| $$| $$  | $$
    | $$  | $$__/ $$| $$__/ $$      | $$$$  \\$$$$| $$| $$  | $$
    | $$   \$$    $$ \$$    $$      | $$$    \\$$$| $$| $$  | $$
     \$$    \$$$$$$   \$$$$$$        \$$      \\$$ \\$$ \\$$   \\$$
                                   {color.WHITE}{color.BOLD}Gigabite-Studios Development{color.ENDC}
                                                               
                                                               
                                                               


"""


def reset():
  f1 = open("./src/data/UserData.json", "w")
  f2 = open("./src/data/default.txt", "r")
  #print(f2.read())
  f1.write(f2.read())
  f1.close()
  f2.close()
  #time.sleep(10)


def export():
  f2 = open("./src/data/UserData.json", "r")
  f1 = open("./UserData.json", "a")
  #print(f2.read())
  f1.write(f2.read())
  f1.close()
  f2.close()
  #time.sleep(10)


def credits():
  clear()
  print("Made by GigabiteStudios Develompent \n\n")
  print("Please do not Sell for Profit\n")
  with open("./src/config/LICENSE", "r") as f:
    print(f.read())
  input(f"{color.BLACK}ENTER to close{color.ENDC}")


def rename():
  clear()
  print(logo)
  oldName = userData["name"]
  print(
    f"Your old name was {color.BOLD}{color.HEADER}{oldName}{color.ENDC}, keep blank to keep same"
  )
  name = input(" \nPlease Enter New Name: ")
  print(color.ENDC)
  if name == None:
    return
  save("name", name)
  clear()
  print(logo)


print(logo)

Playing = False
while not Playing:
  f = open('./src/data/UserData.json')
  userData = json.load(f)
  f.close()
  menu = keys.inputCommands(["Play", "Settings", "Credits"], logo, None)
  if menu == "Settings":
    clear()
    print(logo)
    settingsMenu = keys.inputCommands(
      ["Reset", "Rename", "Export User Data", "Return"], logo,
      [color.FAIL, color.WHITE, color.WHITE, color.BLACK])
    if settingsMenu == "Return":
      clear()
      print(logo)
      pass
    elif settingsMenu == "Rename":
      rename()
      clear()
    elif settingsMenu == "Reset":
      reset()
      clear()
      print(logo)
    elif settingsMenu == "Export User Data":
      export()
      clear()
      print(logo)
  elif menu == "Credits":
    credits()
    clear()
    print(logo)

  else:
    Playing = True

with open("./src/appdata/enemies.json", "r") as f:
  enemies = json.load(f)


def loadData():
  f = open('./src/data/UserData.json')
  userData = json.load(f)
  f.close()

  global PlayerHP, itemRaw, isPotion, itemEffects, itemsDamage, itemsRareity, items
  PlayerHP = int(userData["health"])
  slot1 = userData["items"]["1"]["item"]
  slot2 = userData["items"]["2"]["item"]
  slot3 = userData["items"]["3"]["item"]

  with open("./src/appdata/items.json", "r") as f:
    data = json.load(f)

  item1 = data[str(slot1)]
  item2 = data[str(slot2)]
  item3 = data[str(slot3)]

  items = [item1["name"], item2["name"], item3["name"]]
  itemRaw = [item1, item2, item3]
  isPotion = [item1["potion"], item2["potion"], item3["potion"]]
  itemEffects = [item1["effect"], item2["effect"], item3["effect"]]
  itemsDamage = [item1["damage"], item2["damage"], item3["damage"]]
  itemsRareity = [item1["rarity"], item2["rarity"], item3["rarity"]]


loadData()

f = open('./src/data/UserData.json')
userData = json.load(f)
f.close()

name = userData["name"]
if not name:
  print('Welcome Traveler')
  name = input("What is your name: ")
  save("name", name)
else:
  name = userData["name"]

clear()
print(
  f'\b\rWelcome the the jungle {color.HEADER}{color.BOLD}{name}{color.ENDC}')

time.sleep(1)

clear()

oldText = ""


def saveItem(slot, itemIndex):

  f = open('./src/data/UserData.json')
  userData = json.load(f)
  f.close()

  userData["items"][str(slot)]["item"] = int(itemIndex)

  json_object = json.dumps(userData, indent=4)
  with open("./src/data/UserData.json", "w") as f:
    f.write(json_object)


def FAIL(enemie, name):
  clear()
  print(
    f"You Encountered a wild {color.WARNING}{enemie}{color.ENDC},\nit killed you."
  )

  #23

  spaces = " " * (23 - len(name))

  nameResised = name + spaces

  skull = f"""

    

 _;~)                  (~;_
(   |                  |   )
 ~', ',    ,''~'',   ,' ,'~
     ', ','       ',' ,'
       ',: (') (') :,'
         ;         ;
          ~\  ~  /~
        ,' ,~~~~~, ',
      ,' ,' ;~~~; ', ',
    ,' ,'    '''    ', ',
  (~  ;               ;  ~)
   -;_)               (_;-

|#############################|
| Rip {color.FAIL}{nameResised}{color.ENDC} |
|#############################|

"""
  print(skull)
  sys.exit()


def WIN():
  clear()
  print(logo, winIcon)
  sys.exit()


def getIndex(name: str):
  with open("./src/appdata/items.json", "r") as f:
    data = json.load(f)
  for key in data.keys():
    if data[key]["name"] == name:
      return key


def getRarity(name: str):
  with open("./src/appdata/items.json", "r") as f:
    data = json.load(f)
  for key in data.keys():
    if data[key]["name"] == name:
      return data[key]["rarity"]


def getItem(level: int):
  y = []
  for i in range(3):
    new = RRI.getRandomRarity()
    while new in y:
      new = RRI.getRandomRarity()
    y.append(new)
  question = "You Found An Item \nPlease Select one\n\n"
  print(question)

  with open("./src/appdata/items.json", "r") as f:
    data = json.load(f)

  x = []
  for i in range(len(y)):
    #print(y[i])
    x.append(data[str(y[i])]["name"])

  sellected = keys.inputCommands([x[0], x[1], x[2], "None"], question, [
    rareity.getRareColor(getRarity(x[0])),
    rareity.getRareColor(getRarity(x[1])),
    rareity.getRareColor(getRarity(x[2])), color.BLACK
  ])

  if sellected == "None":
    clear()
    return

  itemIndex = getIndex(sellected)

  question2 = "What item would you like to replace? \n"
  clear()
  print(question2)
  slot = keys.inputCommands([1, 2, 3], question2, None)

  saveItem(int(slot), str(itemIndex))
  loadData()

  del sellected
  clear()


for x in range(len(enemies)):

  #print(x)

  # ______ Load / save automatic level system ______

  if x < load("level"):
    x += load("level")
    if x >= len(enemies):
      WIN()

  if x > load("level"):
    save("level", x)

  #print("Level", load("level"), " x:",x)

  i = load("level")

  #print(load("health"), PlayerHP)
  if load("health") != PlayerHP:
    save("health", PlayerHP)

  health = int(enemies[str(i)]["health"])

  #print(x, i)

  while not health <= 0:
    if PlayerHP <= 0:
      FAIL(enemies[str(i)]["name"], name)
    oldText = ""
    print(f"Health: {color.FAIL}{color.BOLD}{PlayerHP}{color.ENDC}\n")
    print("You encounter a " + color.HEADER + color.BOLD +
          enemies[str(i)]["name"] + color.ENDC)
    print("It has " + color.HEADER + color.FAIL + str(health) + color.ENDC +
          " health")
    oldText += (f"Health: {color.FAIL}{color.BOLD}{PlayerHP}{color.ENDC}\n\n")
    oldText += "You encounter a " + color.HEADER + color.BOLD + enemies[str(
      i)]["name"] + color.ENDC + "\n"
    oldText += "It has " + color.HEADER + color.FAIL + str(
      health) + color.ENDC + " health \n"

    print("\nWhat do you use?\n")
    oldText += " \nWhat do you use?\n "

    optionrarity = (itemsRareity[0], itemsRareity[1], itemsRareity[2])

    rarityColors = (rareity.getRareColor(optionrarity[0]),
                    rareity.getRareColor(optionrarity[1]),
                    rareity.getRareColor(optionrarity[2]))

    del optionrarity
    option = "Empty"

    while option == "Empty":

      option = keys.inputCommands(items, oldText, rarityColors)

      clear()
      print(oldText)

    optionrarity = itemsRareity[items.index(option)]

    print(
      f"\nYou Selected {rareity.getRareColor(optionrarity)}{option}{color.ENDC}\n"
    )
    #print(items.index(option), itemsDamage[items.index(option)])
    damage = int(itemsDamage[items.index(option)])
    time.sleep(0.2)
    print(f"it did {color.FAIL}{color.BOLD}{damage}{color.ENDC} damage")
    health -= damage
    #print(itemEffects[items.index(option)])

    if isPotion[items.index(option)]:
      PotionEffectDamage = itemRaw[items.index(option)]["effect"]["amount"]
      effected = itemRaw[items.index(option)]["effect"]["effected"]
      if PotionEffectDamage >= 0:
        symbol = color.BOLD + color.OKGREEN + "+"
      else:
        symbol = color.FAIL
      print(
        f"You have used your {rareity.getRareColor(optionrarity)}{option}{color.ENDC}, it did {symbol}{color.ENDC}{color.BOLD}{color.FAIL}{PotionEffectDamage}{color.ENDC} to your {color.ITALIC}{color.HEADER}{effected}{color.ENDC}"
      )
      del symbol

      if effected == "self":
        PlayerHP += PotionEffectDamage
      else:
        health += PotionEffectDamage

    time.sleep(0.3)
    print(f"It has {color.FAIL}{color.BOLD}{health}{color.ENDC} Health Left")

    num = random.randint(1, 2)
    time.sleep(0.2)

    attack = num
    del num
    if not health <= 0:

      print("the " + color.HEADER + color.HEADER + enemies[str(i)]["name"] +
            color.ENDC + " Has attacked!!")
      playerDamage = str(enemies[str(i)]["attacks"][str(attack)]["damage"])
      print("it used " + color.WARNING + color.BOLD +
            enemies[str(i)]["attacks"][str(attack)]["name"] + color.ENDC +
            " attack, it did " + color.FAIL + color.BOLD + playerDamage +
            color.ENDC + " Damage")
      PlayerHP -= int(playerDamage)
    else:
      print(
        f"You Have Killed The {color.BOLD}{color.FAIL}{enemies[str(i)]['name']}{color.ENDC}"
      )

    input(f"press {color.OKGREEN}{color.BOLD}ENTER{color.ENDC} to continue")
    clear()
  #if i < len(enemies):

  if PlayerHP <= 0:
    FAIL(enemies[str(i)]["name"], name)
  save("health", PlayerHP)
  getItem(i)

WIN()
