import random
#Global Variables
all_dice = [0, 0, 0, 0, 0]
saved_lines = []
scorevari = 0
scored_numbers = []

#Rolls and saves dice, controls the main flow\/\/\ of the game
def main():
    roll_dice()
    save_lines()
    roll_dice()
    save_lines()
    roll_dice()
    score()
    empty_saves()

#rolls the non-saved dice
def roll_dice():
    global all_dice
    #rolls five times if the line numbers are not in saved lines
    for dice_num in range(5):
        #adds 1 to the dice number, becuase the int starts at zero and ends at 4, but thats not correct for the game
        if (dice_num + 1) in saved_lines:
            print("line " + str(dice_num + 1) + ", you saved a " + str(all_dice[dice_num]))
        else:
            roll = random.randint(1, 6)
            all_dice[dice_num] = roll
            print("line " + str(dice_num + 1) + ", you rolled a " + str(roll))

#lets you save the lines with instructions and also lets you stop and roll the next dice
def save_lines():
    global saved_lines
    save = input("What line number would you like to save/unsave? (Type 'stop' if you are done.)")
    #makes it so when you type stop, it rolls the nest dice, unless your on your last roll
    while save != "stop":
        #converts save from a string to an int because we need it to be a number, or else the code will explode
        save = int(save)
        #lets you unsave any line if save is in saved_lines
        if save in saved_lines:
            saved_lines.remove(save)
            print("you unsaved line, " + str(save))
        #if save is not in saved_lines, save the line
        else:
            saved_lines.append(save)
            print("You saved line, " + str(save))
        save = input("What line number would you like to save/unsave? (Type 'stop' if you are done.)")

def empty_saves():
   saved_lines.clear()


#makes the score
def score():
    global scorevari
    global all_dice
    #lets you choose which dice number you would like to score for
    print("You have already scored for " + str(scored_numbers))
    score_input = input("Which number would you like to score for? ")
    score_input = int(score_input)
    while score_input in scored_numbers:
        score_input = input("You already scored for that number, pick another one!")
        score_input = int(score_input)
    scored_numbers.append(score_input)

    #gives you the score of the dice
    for i in all_dice:
        if i == score_input:
            scorevari = scorevari + score_input
    
    #keeps track of the score
    print("you score is... " + str(scorevari))

    #other rounds
for i in range(6):
    main()







#main()