from getkey import getkey
try:
  from src.lib import color
except:
  from . import color

import os, sys, time

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def inputCommands(commands, start_txt, raritys):

        
        
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