import random
from rich.console import Console

console = Console(width = 40,color_system = 'windows')
def get_words() :
    '''Open text file and return a list of 5 letter words '''
    with open("words.txt","r") as my_words :
        data = my_words.read()
        word_list = data.split("\n")
        my_words.close()
    return word_list

def pick_word(word_list) :
    '''Picks a random word
    takes in a list of words and returns a randomly selcted one'''
    word_index = random.randint(0,len(word_list)-1)
    my_word = word_list[word_index]
    word = my_word.upper()
    return word

        
def get_word(guess) :
    '''Gets 5 letter input of the word guessed
    takes in the the number of thimes the user has guessed'''
    while True :
        var = None
        guessed_word = input(f"Guess {guess} : ")
        for i in guessed_word :
            if i.isdigit() == True :
                var = False
                break
            elif i.isalpha() == True :
                var = True
                
            
        if len(guessed_word) > 5 or len(guessed_word) < 5 :
            print("Your word should be 5 letters long")
            continue
        elif var == False :
            print("Please enter a word.")
            continue
        elif var == True :
            break
    return guessed_word.upper()


def check_word(word,guessed_word) :
    '''Checks user guess against the randomly selcted word'''
    correct_letter = '-'
    incorrect_letter = '-'
    misplaced_letter = '-'
    for i in guessed_word :
        if i in word :
            if list(guessed_word).index(i) == list(word).index(i) :
                correct_letter = f"{correct_letter}, {i}"
            else :
                misplaced_letter = f"{misplaced_letter}, {i}"
        else :
            incorrect_letter = f"{incorrect_letter}, {i}"
    if guessed_word == word :
        print("Correct!")
        return True
    else :
        correct_letter = correct_letter.strip('-')
        incorrect_letter = incorrect_letter.strip('-')
        misplaced_letter = misplaced_letter.strip('-')
        return False,correct_letter,incorrect_letter,misplaced_letter




if __name__ == "__main__" :
    guess = 0
    words_guessed=["_____","_____","_____","_____","_____","_____",]
    word_list = get_words()
    console.clear()
    word = pick_word(word_list)
    alpha = []
    correct = []
    missed = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    console.rule(f"[bold red]:leafy_green: My Wordle Game:leafy_green:[/]\n")
    print('~~ Welcome to a wordle game attempt coded using python ~~')
    print('GREEN : CORRECT LETTERS')
    print('YELLOW : MISPLACED LETTERS')
    index = 0
    for i in words_guessed:
        print(i, end='\n')
    print(alphabet)
    while guess < 6 :
        guess += 1
        guessed_word = get_word(guess)
        words_guessed[index]=(guessed_word)
        index += 1
        console.clear()
        console.rule(f"[bold red]:leafy_green: My Wordle Game:leafy_green:[/]\n")
        check=check_word(word,guessed_word)
        for i in check[2]:
            i=i.upper()
            alpha.append(i)
        for i in check[1]:
            i=i.upper()
            correct.append(i)
        for i in check[3]:
            i=i.upper()
            missed.append(i)
        for i in words_guessed:
            for j in i:
                if j in correct:
                    console.print(f'[green]{j}[/green]',end='')
                elif j in alpha:
                    print(f'{j}',end='')
                elif j in missed:
                    console.print(f'[yellow]{j}[/yellow]',end='')
                else:
                    print(f"{j}",end='')
            print(" ")
        for i in alphabet:
            if i in alpha:
                console.print(f'[purple]{i}[/purple]',end='')
            else:
                print(f'{i}',end='')
        print(" ")
        if check[0] == True :
            print("You won!")
            break

    else:
        print("You lost!")
        print(f"The word was : {word}")
    
        
    
wordList = [
    "Above", "Acute", "Alive", "Alone", "Angry",
     "Aware", "Awful", "Basic", "Black", "Blind",
      "Brave", "Brief", "Broad", "Brown", "Cheap",
       "Chief", "Civil", "Clean", "Clear", "Close",
        "Crazy", "Daily", "Dirty", "Early", "Empty",
         "Equal", "Exact", "Extra", "Faint", "False",
          "Fifth", "Final", "First", "Fresh", "Front",
           "Funny", "Giant", "Grand", "Great", "Green",
            "Gross", "Happy", "Harsh", "Heavy", "Human",
             "Ideal", "Inner", "Joint", "Large", "Legal",
              "Level", "Light", "Local", "Loose", "Lucky",
               "Magic", "Major", "Minor", "Moral", "Naked",
                "Nasty", "Naval", "Other", "Outer", "Plain",
                 "Prime", "Prior", "Proud", "Quick", "Quiet",
                  "Rapid", "Ready", "Right", "Roman", "Rough",
                   "Round", "Royal", "Rural", "Sharp", "Sheer",
                    "Short", "Silly", "Sixth", "Small", "Smart",
                     "Solid", "Sorry", "Spare", "Steep", "Still",
                      "Super", "Sweet", "Thick", "Third", "Tight",
                       "Total", "Tough", "Upper", "Upset", "Urban",
                        "Usual", "Vague", "Valid", "Vital", "White",
                         "Whole", "Wrong", "Young", "Adult", "Agent",
                          "Anger", "Apple", "Award", "Basis", "Beach",
                           "Birth", "Block", "Blood", "Board", "Brain", 
                           "Bread", "Break", "Brown", "Buyer", "Cause",
                            "Chain", "Chair", "Chest", "Chief", "Child",
                             "China", "Claim", "Class", "Clock", "Coach",
                              "Coast", "Court", "Cover", "Cream", "Crime",
                               "Cross", "Crowd", "Crown", "Cycle", "Dance",
                                "Death", "Depth", "Doubt", "Draft", "Drama",
                                 "Dream", "Dress", "Drink", "Drive", "Earth",
                                  "Enemy", "Entry", "Error", "Event", "Faith",
                                   "Fault", "Field", "Fight", "Final", "Floor",
                                    "Focus", "Force", "Frame", "Frank", "Front",
                                     "Fruit", "Glass", "Grant", "Grass", "Green",
                                      "Group", "Guide", "Heart", "Henry", "Horse",
                                       "Hotel", "House", "Image", "Index", "Input",
                                        "Issue", "Japan", "Jones", "Judge", "Knife",
                                         "Laura", "Layer", "Level", "Lewis", "Light",
                                          "Limit", "Lunch", "Major", "March", "Match",
                                           "Metal", "Model", "Money", "Month", "Motor",
                                            "Mouth", "Music", "Night", "Noise", "North",
                                             "Novel", "Nurse", "Offer", "Order", "Other",
                                              "Owner", "Panel", "Paper", "Party", "Peace",
                                               "Peter", "Phase", "Phone", "Piece", "Pilot",
                                                "Pitch", "Place", "Plane", "Plant", "Plate",
                                                 "Point", "Pound", "Power", "Press", "Price",
                                                  "Pride", "Prize", "Proof", "Queen", "Radio",
                                                   "Range", "Ratio", "Reply", "Right", "River",
                                                    "Round", "Route", "Rugby", "Scale", "Scene",
                                                     "Scope", "Score", "Sense", "Shape", "Share",
                                                      "Sheep", "Sheet", "Shift", "Shirt", "Shock",
                                                       "Sight", "Simon", "Skill", "Sleep", "Smile",
                                                        "Smith", "Smoke", "Sound", "South", "Space",
                                                         "Speed", "Spite", "Sport", "Squad", "Staff",
                                                          "Stage", "Start", "State", "Steam", "Steel",
                                                           "Stock", "Stone", "Store", "Study", "Stuff",
                                                            "Style", "Sugar", "Table", "Taste", "Terry",
                                                             "Theme", "Thing", "Title", "Total", "Touch",
                                                              "Tower", "Track", "Trade", "Train", "Trend",
                                                               "Trial", "Trust", "Truth", "Uncle", "Union",
                                                                "Unity", "Value", "Video", "Visit", "Voice",
                                                                 "Waste", "Watch", "Water", "While", "White",
                                                                  "Whole", "Woman", "World", "Youth", "There",
                                                                   "Where", "Which", "Whose", "Whoso", "Yours",
                                                                    "Adopt", "Agree", "Allow", "Alter", "Apply",
                                                                     "Argue", "Arise", "Avoid", "Begin", "Blame",
                                                                      "Break", "Bring", "Build", "Burst", "Carry",
                                                                       "Catch", "Cause", "Check", "Claim", "Clean",
                                                                        "Clear", "Climb", "Close", "Count", "Cover",
                                                                         "Cross", "Dance", "Doubt", "Drink", "Drive",
                                                                          "Enjoy", "Enter", "Exist", "Fight", "Focus",
                                                                           "Force", "Guess", "Imply", "Issue", "Judge",
                                                                            "Laugh", "Learn", "Leave", "Let’s", "Limit",
                                                                             "Marry", "Match", "Occur", "Offer", "Order",
                                                                              "Phone", "Place", "Point", "Press", "Prove",
                                                                               "Raise", "Reach", "Refer", "Relax", "Serve",
                                                                                "Shall", "Share", "Shift", "Shoot", "Sleep",
                                                                                 "Solve", "Sound", "Speak", "Spend", "Split",
                                                                                  "Stand", "Start", "State", "Stick", "Study",
                                                                                   "Teach", "Thank", "Think", "Throw", "Touch",
                                                                                    "Train", "Treat", "Trust", "Visit", "Voice",
                                                                                     "Waste", "Watch", "Worry", "Would", "Write",
                                                                                      "Afore", "After", "Bothe", "Other", "Since",
                                                                                       "Slash", "Until", "Where", "While", "Abaft",
                                                                                        "Aboon", "About", "Above", "Accel", "Adown",
                                                                                         "Afoot", "Afore", "Afoul", "After", "Again",
                                                                                          "Agape", "Agogo", "Agone", "Ahead", "Ahull",
                                                                                           "Alife", "Alike", "Aline", "Aloft", "Alone",
                                                                                            "Along"]

        