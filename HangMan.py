import random
from datetime import datetime
import time
import math
name = ""
leaderboards = []
count_mistakes = 0
level = 0
used = []
drinks = ["coca cola", "tea", "milk", "coffee", "beer", "orange juice", "water"]
cities = ["london", "madrid", "barcelona", "new york", "paris", "jerusalem", "tel aviv"]
country = ["israel", "united states", "spain", "france", "england", "germany", "russia"]
food = ["burger", "pizza", "popcorn", "salad", "cake", "chocolate", "dounat"]
sport = ["tennis", "footbal", "soccer", "basketball", "swimming", "boxing", "running"]
workSubjects = ["doctor", "engeneer", "teacher", "police officer", "artist", "bussiness man", "driver"]
fameousPeople = ["barak obama", "bill gates", "marthin luther king", "marilyn monroe", "nelson mandela",
                 "muhammad ali", "michael jordan"]
animals = ["dog", "cat", "crocodile", "lion", "eagle", "rabbit", "cow"]
cloths = ["shirt", "jeans", "sweatshirt", "coat", "gloves", "skirt", "hat"]
bodyParts = ["leg", "head", "arm", "chest", "nose", "ear", "back"]
topics = {"Country": country, "Food": food, "Sport": sport, "Work Subjects": workSubjects,
          "Fameous Peapole": fameousPeople, "Animals": animals, "Cloths": cloths, "Body Parts": bodyParts,
          "Drinks": drinks, "Cities": cities}

def add_to_leaderboardes (score): #insert the score to the leaderboards
    leaderboards.append(score)
    for i in range(len(leaderboards) - 1, 0, -1):
        delta = str (leaderboards[i][2] - leaderboards[i-1][2])
        if delta [0] == '-' or leaderboards[i][1] > leaderboards[i-1][1]:
            temp = leaderboards[i-1]
            leaderboards[i-1] = leaderboards[i]
            leaderboards[i] = temp
        else:
            break

def let_in_word(letters, guess): #if the letter is in the string or in the list
    if guess in letters:
        return True
    return False

#ascii body print functions:

def printLevel0():
    print "  _____________  "
    print " |               "
    print " |               "
    print " |               "

def printLevel1():
    print "  _____________  "
    print " |     #__#      "
    print " |    /^  ^\     "
    print " |    \ __ /     "

def printLevel2():
    print "  _____________  "
    print " |     #__#      "
    print " |    /^  ^\     "
    print " |    \ __ /     "
    print " |      ||       "
    print " |      ||       "

def printLevel3():
    print "  _____________  "
    print " |     #__#      "
    print " |    /^  ^\     "
    print " |    \ __ /     "
    print " |      ||       "
    print " |      ||       "
    print " |      ||       "
    print " |      ||       "

def printLevel4():
    print "  _____________ "
    print " |     #__#     "
    print " |    /^  ^\    "
    print " |    \ __ / /  "
    print " |      ||  /   "
    print " |      || /    "
    print " |      ||      "
    print " |      ||      "

def printLevel5():
    print "  _____________ "
    print " |     #__#     "
    print " |    /^  ^\    "
    print " |  \ \ __ / /  "
    print " |   \  ||  /   "
    print " |    \ || /    "
    print " |      ||      "
    print " |      ||      "
def printLevel6():
    print "  _____________ "
    print " |     #__#     "
    print " | *  /^  ^\  * "
    print " |  \ \ __ / /  "
    print " |   \  ||  /   "
    print " |    \ || /    "
    print " |      ||      "
    print " |      ||      "

def printLevel7():
    print "  _____________ "
    print " |     #__#     "
    print " | *  /^  ^\  * "
    print " |  \ \ __ / /  "
    print " |   \  ||  /   "
    print " |    \ || /    "
    print " |      ||      "
    print " |      ||      "
    print " |        \     "
    print " |         \    "
    print " |          \   "

def printLevel8():
    print "  _____________ "
    print " |     #__#     "
    print " | *  /^  ^\  * "
    print " |  \ \ __ / /  "
    print " |   \  ||  /   "
    print " |    \ || /    "
    print " |      ||      "
    print " |      ||      "
    print " |        \     "
    print " |         \    "
    print " |          \_  "

def printLevel9():
    print "  _____________ "
    print " |     #__#     "
    print " | *  /^  ^\  * "
    print " |  \ \ __ / /  "
    print " |   \  ||  /   "
    print " |    \ || /    "
    print " |      ||      "
    print " |      ||      "
    print " |     /  \     "
    print " |    /    \    "
    print " |   /      \_  "

def printLevel10():
    print "  _____________ "
    print " |     #__#     "
    print " | *  /^  ^\  * "
    print " |  \ \ __ / /  "
    print " |   \  ||  /   "
    print " |    \ || /    "
    print " |      ||      "
    print " |      ||      "
    print " |     /  \     "
    print " |    /    \    "
    print " |  _/      \_  "

body =  {1: {0: printLevel0, 1: printLevel1, 2: printLevel2, 3: printLevel3, 4: printLevel4, 5: printLevel5,
             6: printLevel6, 7: printLevel7, 8: printLevel8, 9: printLevel9, 10: printLevel10},
         2: {0: printLevel0, 1: printLevel1, 2: printLevel2, 3: printLevel3, 4: printLevel4, 5: printLevel5,
             6: printLevel6, 7: printLevel8, 8: printLevel10},
         3: {0: printLevel0, 1: printLevel1, 2: printLevel3, 3: printLevel4, 4: printLevel6,
             5: printLevel8, 6: printLevel10}}

mistakes = {1: 10, 2: 8, 3: 6} #how many mistakes can the player do in every level

def choseWord(): #randoms a topic and a word
    topic_idx = random.randint(0, 9)
    word_idx = random.randint(0, 6)
    topic = topics.keys()[topic_idx]
    chosenWord = topics[topic][word_idx]
    return (topic, chosenWord)

def playerSee(word): #returns a list in the len of the word which contains only # and space to show to the player
    s = ''
    for i in word:
        if i == ' ':
            s += ' '
        else:
            s += '*'
    return s

def inputCheck(letter): #input check that the letter is in the abc and not used yet
    while not letter.isalpha() or letter in used:
        letter = raw_input("Wrong input, please enter another one: ")
    used.append(letter)
    return letter

def win(hidden): #if the player won
    if '*' not in hidden:
        return True
    return False

def loss(): #if the player lost
    if count_mistakes == mistakes[level]:
        return True
    return False

def finished(hidden): #check if the game is finished- win or loss
    if not loss() and not win(hidden):
        return False
    return True

def move(hidden, letToGuess, letter, word): #shows to the player if he guessed right the whole places of the letter
    global count_mistakes
    show = let_in_word(letToGuess, letter)
    hidden = list(hidden)
    word = list(word)
    if show:
        letToGuess.remove(letter)
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
    else:
        print "you guessed wrong"
        count_mistakes += 1
    hidden = ''.join(hidden)
    return (hidden, letToGuess) #returns a tuple of the changes

def run():
    start = datetime.now()
    global used
    global count_mistakes
    used = []
    count_mistakes = 0
    word = choseWord()  # The randomed topic name and world
    print "The topic chosen by computer is \033[1m %s " % (word[0])
    print "\033[0;0m"
    word = word[1]  # change the word to the randomed only word- the chosen word
    print "The computer chose for you a word to guess"
    hiddenWord = playerSee(word)  # The hidden word the player will see
    letToGuess = list(word)  # a list of the letters of the word

    while ' ' in letToGuess[:]:  # delete spaces in the list so the player wont have to guess space
        letToGuess.remove(' ')
    letToGuess = list(set(letToGuess))  # using a set function the remove the repetitions

    while not finished(hiddenWord):  # the game is still going
        body[level][count_mistakes]()
        print "\nThe word you have already found out: ", hiddenWord
        print "The letters you have already used: ", used
        letter = raw_input("Please enter your letter guess: ")
        letter = inputCheck(letter)
        turn = move(hiddenWord, letToGuess, letter, word)
        hiddenWord = turn[0]
        letToGuess = turn[1]

    if win(hiddenWord):
        end = datetime.now()
        print "Congratluations, You have won the game and you are going to the leaderboard!"
        #print "The word was %s" % (word)
        print "The word was \033[1m '%s'" % (word)
        print "\033[0;0m"
        score = (name, level, end-start) # creates a tuple of the score
        add_to_leaderboardes(score)

    if loss():
        body[level][count_mistakes]()
        print "\nGame Over, You've lost and you aren't going into the leaderboard."
        print "The word was \033[1m '%s'" % (word)
        print "\033[0;0m"

def main():
    print "\033[1m          ================================"
    print "          | Welcome to the HangMan game  |"
    print "          ================================  \033[0;0m"
    print "\n \033[1m    Menu"
    print "---------------\033[0;0m"
    print "\033[1m 1 \033[0;0m to start a new game"
    print "\033[1m 2 \033[0;0m to take a look on the leaderboard"
    print "\033[1m any other key \033[0;0m to exit"
    directive = raw_input()
    while directive in ('1', '2'):
        if directive == '1':
            global name
            name = raw_input("Please enter your name: ")
            global level
            level = raw_input("Please enter the level you want to play in- 1 to 3: ")
            while level not in ("1", "2", "3", "4"): #input check of the level input
                level = raw_input("Please enter the level you want to play in- 1 to 3: ")
            level = int(level)
            print "\033[1m You choose level %d" % (level)
            print "\033[0;0m"
            run()
        else: #print of the leaderboards
            print "\033[1m {0: <10} {1: <5} {2: >13}".format( "Name", "Level", "Time")
            print "=============================== \033[0;0m"
            for i in leaderboards:
                print "{0: <10} | {1: <5} | {2: >13}".format(i[0], i[1], i[2])
        print "\n \033[1m    Menu"
        print "---------------\033[0;0m"
        print "\033[1m 1 \033[0;0m to start a new game"
        print "\033[1m 2 \033[0;0m to take a look on the leaderboard"
        print "\033[1m any other key \033[0;0m to exit"
        directive = raw_input()

if __name__ == "__main__":
    main()
