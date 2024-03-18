import random

moves = ["Right Hand", "Left Hand", "Right Foot", "Left Foot", 
         "Right Hand Off", "Left Hand Off", "Right Foot Off", "Left Foot Off"]

def play_twister():
    play = "y"
    last_move = None

    moves_stored = []

    bad_dups = ["Right Foot Off", "Right Hand Off", "Left Foot Off", "Left Hand Off"]

    check_dup = []

    while play == "y":
        
        the_move = random.choice(moves)

        if the_move in bad_dups:
            if the_move in check_dup:
                continue
            else:
                check_dup.append(the_move)
        
        if the_move == "Right Hand Off" or the_move == "Left Hand Off":
            moves_stored.append(the_move)
            
            if "Right Hand Off" in moves_stored and "Left Hand Off" in moves_stored:
                moves_stored.remove(the_move)
                continue

        else:
            corresponding_move = the_move + " Off"
            if corresponding_move in moves_stored:
                moves_stored.remove(corresponding_move)

            if corresponding_move in check_dup:
                check_dup.remove(corresponding_move)
    
        print(f"Move: {the_move}")

        play = input("Another move? (y/n)").lower()

play_twister()
