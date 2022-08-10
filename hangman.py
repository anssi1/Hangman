import random

def draw_image(n, progress_list):
    """
    Draws the hangman image based on value of n, where
    0 = start,
    1 = Rope,
    2 = Head,
    3 = Torso
    4 = L Hand
    5 = R Hand
    6 = L Leg
    7 = R Leg
    
    Also handles display of progress on quesses.
    
    n = integer, values defined by program.
    word_progress is the current amount of word revealed.
    This function returns nothing.
    """
    
    imageparts = ("__________________      ", #0
                  "                 |      ", #1
                  "                 O      ", #2
                  "                 |      ", #3
                  "                /|      ", #4
                  "                /|\     ", #5
                  "                /       ", #6
                  "                / \     "  #7
                  )
    
    i = 0
    
    if n < 4:
        while n >= 0:
            print(imageparts[i])
            n = n - 1
            i = i + 1
    elif n < 6:
        while i < 3:
            print(imageparts[i])
            i = i + 1
        if n == 4:
            print(imageparts[4])
        else:
            print(imageparts[5])
    else:
        print(imageparts[0])
        print(imageparts[1])
        print(imageparts[2])
        print(imageparts[5])
        if n == 6:
            print(imageparts[6])
        else:
            print(imageparts[7])
    
    print("\n")
    
    state_list = []
    
    for letter in progress_list:
        if letter == "0":
            state_list.append("|_")
        else:
            state_list.append("|" + letter)
    
    state_list.append("|")
    print("".join(state_list))
    
    print("\n")
    

    

def wordpicker():
    """
    Picks a word from a list randomly.
    Takes no parameters.
    Returns the selected word.
    """
    wordlist = ["cat", "bird", "human"]
    random.seed()
    i = random.randrange(len(wordlist))
    return wordlist[i]
    
    
    
def hangman():
    """
    Initializes the game and runs the primary game loop.
    """    
    word = wordpicker()
    game_finished = False
    word_progress = "0" * len(word)
    progress_list = list(word_progress)
    word_list = list(word)
    turn = 1
    state = 0
    correct = 0
    
    print("Beginning of game.")
    
    while game_finished == False:
        
        draw_image(state, progress_list)
        print("Turn ", turn, ":")
        quess = input("Input a single letter: ")
        
        index = word.find(quess)
        
        if index == -1:
            state = state + 1
            print("You quessed wrong!")
        else:
            print("You quessed correctly!")
            correct = correct + 1
            word_list[index] = "0"
            progress_list[index] = quess
        
        if correct == len(word):
            print("Victory")
            game_finished = True
        elif state == 8:
            print("Defeat")
            game_finished = True
        else:
            turn = turn + 1
        
    
    print("End of game.")
    


hangman()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        