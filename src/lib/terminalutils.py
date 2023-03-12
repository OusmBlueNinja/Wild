# Thire will be code here that is used for terminal
# utilitys. if you want you can use this code in any 
# projects that you want. it will have an error function 
# that you can call. it will use color to print a good 
# looking error


# \/ Error Codes \/ 
"""
0. WARNING (call this if a non fatal error occors. like its unable to get the latest update)

1. FAIL (call this if an error happens that makes the program no longer run)

2. INFO (call this code to print test to terminal that just states that something happend (use like print statment))


"""

# Example output (not in color)

# {WHITE}[{RED}ERROR{WHITE] {YOU ERROR MESSAGE HERE}

# [ERROR] Unable to import json
# [WARNING] Unable to get update
# [INFO] Connected to host


# - - - - - - - - - - - - - - - -

import sys, os

class _color:
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
  ITALIC = '\033[24m'
  BLACK = '\u001b[1;30m'

_color = _color()

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def error(errorMessage:str, errorCode:int):
  print(f"{_color.ENDC}[{_errorConverter(errorCode)}] {errorMessage}")
  if errorCode == 1:
    sys.exit()
  


# private function to decode error codes
def _errorConverter(errorCode:int):
  if errorCode == 1:
    return _color.FAIL + "ERROR" + _color.ENDC
  elif errorCode == 0:
    return _color.WARNING + "WARNING" + _color.ENDC
  elif errorCode == 2:
    return _color.HEADER + "INFO" + _color.ENDC
  else:
    print(f"{_color.ENDC}[{_color.FAIL}ERROR{_color.ENDC}] Invalid Error Code {errorCode}")
    
    raise ValueError("Invalid Error Code "+ str(errorCode))

def inputCommands(commands, start_txt, colors):

        raritys = colors
        del colors

        
        
        global selected
        global on_screen_text
        on_screen_text = start_txt
    
        txt = ""
    
        colors = []
        if raritys != None:
          rarityColor = raritys
        else:
          rarityColor = ['\u001b[37m','\u001b[37m','\u001b[37m','\u001b[37m','\u001b[37m','\u001b[37m']
    
        selected_one = 1
        start = True
    
        y = 0
    
        while True:
            if start is False:
                clear()
                print(color.ENDC + start_txt)
            else:
                start = False
    
            z = 1
            y = 0
            txt = ""
            for i in commands:
    
                if selected_one == z:
                    print(f"{color.HEADER}>{color.ENDC} {color.BOLD}{rarityColor[commands.index(i)]}{i}{color.ENDC}")
                    txt = f"  {txt}> \n"
                else:
                    print(f"  {rarityColor[commands.index(i)]}{i}{color.ENDC}")
                    txt = f"  {rarityColor[commands.index(i)]}{i}\n"
                z += 1
                y += 1
                if y == len(colors):
                    y = 0
    
            answer = getkey()
    
            if answer == "\n":
                selected = commands[selected_one - 1]
                on_screen_text = f"{on_screen_text}\n{txt}"
                return selected
                break
    
            if answer == "\033[A":
                selected_one -= 1
            if answer == "\033[B":
                selected_one += 1
            if selected_one == len(commands) + 1:
                selected_one = 1
            if selected_one == 0:
                selected_one = len(commands)
  
  