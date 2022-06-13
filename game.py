from ast import If
from random import random


name = input("hi pls whats your name")
print("hello {}".format(name))
print(" lets play  Gme called rock paper scissior")
pselect = int(input("pla kindly press 1 for player1 "))
if pselect == 1 :
    p1=input("welcome player pls type in ur NICKname")
    print("hello {} ".format(p1))       
    play=input("pls pick 'R' for rock 'S' for scissior 'P' for paper")    
    hello = ""
    if play == "R":
          hello = "rock"
    elif play == "S":
        hello ="scissiors"
    elif play == "P":
        hello ="paper"
    else:
            print("ur value is not accepted pls make sure ur letters are in upper case value")
      
import random
cpu = random.randint(1,3)
print(cpu)
if cpu == 1:
        out = "rock"
elif cpu ==2:
        out = "SCISSIORS"
elif cpu ==3:
        out = "PAPER"
        


if hello == "rock" and  out == "rock":
    now = "2"
    result = """
         _________ _
        |___   ___(_)          | |
            | |    _   _______ | |
            | |   | | /       \| |   
            | |   | ||  |  |   | |
            | |   | ||     ___/| |
            | |   | ||   _____ |_|
            |_|   |_| \_______|(_)

    """
    print(result)
elif hello == "SCISSIORS" and out == "SCISSIORS":
    now = "2"
    result = """
         _________ _
        |___   ___(_)          | |
            | |    _   _______ | |
            | |   | | /       \| |   
            | |   | ||  |  |   | |
            | |   | ||     ___/| |
            | |   | ||   _____ |_|
            |_|   |_| \_______|(_)

    """
    print(result)
elif hello == "paper" and out == "PAPER":
    now = "2"
    result = """
         _________ _
        |___   ___(_)          | |
            | |    _   _______ | |
            | |   | | /       \| |   
            | |   | ||  |  |   | |
            | |   | ||     ___/| |
            | |   | ||   _____ |_|
            |_|   |_| \_______|(_)

    """     
    print(result)
elif (hello == "rock" and  out == "scissiors"""\
      or hello == "paper"and  out == "rock"\
      or hello == "scissiors" and  out == "paper"\
        ):
    now = "2"
    result= """
        __      __                  ___
        \ \    / /                 \   \                      /  (_)   __      __    
         \ \  / /_____   __    __   \   \                    /  /     |  \    |  |
          \ \/ /      \ |  |  |  |   \   \      _____       /  / | |  |   \   |  |
           |  |   / \  ||  |  |  |    \   \   /  ___  \    /  /  | |  |    \  |  |
           |  |   \_/  ||  |__|  |     \   \ /  /   \  \  /  /   | |  |  \  \_|  |
           |__|\______/ \ _____  |      \   /  /     \   \  /    | |  |  |\      |
                                 |       \____/       \____/     |_|  |__| \_____|
    """
    print(result)
elif (hello == "scissiors" and  out == "rock"\
      or hello == "paper"and  out == "scissiors"\
      or hello == "rock" and  out == "paper"\
        ):
        result = """
       ________    ______
       /   _____| /        \   
      |  /        |   | |  |
      |           |  |_____/                           ___
      |  \ ______ |  |
       \________| |__|

        """
        print(result)

           
        
