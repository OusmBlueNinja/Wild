HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\u001b[31m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
WHITE = '\u001b[37m'
BROWN = '\u001b[33m'
YELLOW = '\u001b[33m'
GREEN = '\u001b[32m'
BLUE = '\u001b[34m'
BLACK = '\u001b[1;30m'



def getRareColor(number: int):

  

  rarity = number

  
  if rarity == 1:
    return str(BOLD+WHITE)
  elif rarity == 2:
    return str(BOLD+YELLOW)
  elif rarity == 3:
    return str(BOLD+GREEN)
  elif rarity == 4:
    return str(BOLD+BLUE)
  elif rarity == 5:
    return str(BOLD+HEADER)
  elif rarity == -1:
    return str(BOLD+BLACK)