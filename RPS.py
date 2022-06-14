
import random
while True :
    player_action = input("pls pick 'R' for rock 'S' for scissior 'P' for paper")
    possible_action = ["R", "S", "P"]
    cpu_action = random.choice(possible_action)
    if player_action == cpu_action :
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
        play_again = input("play again? (y/n)")
        if play_again.lower() != "y":
            break
    elif player_action == "R" and cpu_action == "S" \
    or player_action == "S" and cpu_action == "P" \
    or player_action == "P" and cpu_action == "R":
        result = """   
               __      __                  ___
               \ \    / /                 \   \                      /  (_)   __      __    
                \ \  / /_____   __    __   \   \                    /  /     |  \    |  |
                 \ \/ /      \ |  |  |  |   \   \      _____       /  / | |  |   \   |  |
                  |  |   / \  ||  |  |  |    \   \   /  ___  \    /  /  | |  |    \  |  |
                  |  |   \_/  ||  |__|  |     \   \ /  /   \  \  /  /   | |  |  \  \_|  |
                  |__|\______/ \ _____  |      \   /  /     \      /    | |  |  |\      |
                                        |       \____/       \____/     |_|  |__| \_____|
        """
        print(result)
    elif player_action == "R" and cpu_action == "P" \
    or player_action == "S" and cpu_action == "R" \
    or player_action == "P" and cpu_action == "S":
        result = """
             ________    ______      __   __                             ___
            /   _____| /        \   | |   | |           | |      | | (_) |  \    | |
            |  /        |   | |  |  | |   | |           | |      | | | | |   \   | |
            |           |  |_____/  | |   | |           | |      | | | | |  \ \  | |
            |  \ ______ |  |        | |___| |           | | | |  | | | | | | \ \_| |
             \________| |__|        \_______/           |_|_| |__|_| | | |_|  \____|

        
        """
        print(result)
    elif player_action != possible_action :
        print("ur value is not accepted pls make sure ur letters are in upper case value ")
        play_again = input("RE RUN CODE? (y/n)")
        if play_again.lower() != "y":
            break