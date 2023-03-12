import random, json


def noInit():
  return True


# there will be code here that askes for a level and it returns
# an item id in the items.json file

# will be called every time you kill an enemy

# W.I.P 

  """
  This code is used to randomly select an item id from the items.json file based on a weighted random number generator. It takes into account the rarity of the item and returns a random item id from the file.

  Returns:
      str: Item id of the item it randomly sellected

  """

RARITY = [
  500, 
  250, 
  150, 
  100, 
  50,
  1000
]


def getWeightedInt():
  num = random.randint(1, 1000)
  if num >= RARITY[0]:
    return 1
  elif num >= RARITY[1]:
    return 2
  elif num >= RARITY[2]:
    return 3
  elif num >= RARITY[3]:
    return 4
  elif num >= RARITY[4]:
    return 5
  elif num >= RARITY[5]:
    return 1


def getRandomRarity():
  with open("./src/appdata/items.json", "r") as f:
    data = json.load(f)

  selectedrarity = getWeightedInt()

  #print(selectedrarity)

  options = data.keys()

  rarity = []

  for i in range(len(options)):
    rarity.append(data[str(i)]["rarity"])

  #print(rarity)

  possable = []

  for i in range(len(rarity)):
    if rarity[i] == selectedrarity:
      possable.append(True)
    else:
      possable.append(False)

  #print(possable)
  returnedItem = 0
  for i in range(10):
    #print(returnedItem)
    for i in range(len(possable)):
      if possable[i]:
        #print(">> ", i)
        if random.randint(1,2) == 2:
          returnedItem = i
          break
    
        

  #print(returnedItem)
  for key in data.keys():
    #print(key)
    if key == str(returnedItem):

      return str(key)