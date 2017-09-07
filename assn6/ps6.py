# Problem Set 5: 6.00 Word Game
# Name: Bohdan Drahan 
# Collaborators: 
# Time: 12:00 
#

import random
import time
import string
import itertools

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 6 

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------
#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...

    #try:
    #    word = word.lower()
    #except ValueError: 
    #    print "Error. String expected"
    #    return None
    
    if n == len(word): #Bingo bonus +50 for using all letters
        score = 50
    else: score = 0
    
    if len(word) == 0: #Checking for empty words
        score = 0
        return score
    if not word.isalpha(): #check if all characters are letters
        print "Word has some extra symbols"
        return None

    w = word.lower()
    for letter in w:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    return score

def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value."""
    
    points_list = list() 
    for word in word_list:
        points_list.append(get_word_score(word,100))
    return dict(zip(word_list,points_list))

def get_word_rearrangements(word_list):
    d = dict()
    rearrang = list()
    for word in word_list:
        word_listed = list(word)
        word_listed.sort()
        word_rearrang = str('')
        for letter in word_listed:
            word_rearrang += str(letter)
        rearrang.append(word_rearrang)
    i = 0
    for word in word_list:
        i += 1


    return dict(zip(rearrang, word_list))


global word_list, points_dict, rearrange_dict
word_list = load_words() 
points_dict = get_words_to_points(word_list)
rearrange_dict = get_word_rearrangements(word_list)


#TEST
#get_word_rearrangements(word_list)


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    
    updatedHand = dict(hand) 

    if len(word) == 0:
        return hand
    if not word.isalpha(): #check if all characters are letters
        print "Word\"", word, "\" is not a word. It has extra characters"
        return hand

    for i in word:
        i = i.lower() #Making sure all the letters are lowercase
        updatedHand[i] = updatedHand.get(i, 0) - 1
        
    return updatedHand
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    if len(word) == 0:
        print "Word should be longer than 0 characters"
        return False 
    if not word.isalpha():
        print "Word should contain letters only"
        return False 
    word = word.lower()
    hand_copy = dict(hand) 
    for letter in word:
        if  hand_copy.get(letter, 0) - 1 < 0: #BUG!!!!! HAND B, E shouldn't let the word BEEBEE go.- FIXED!
            #Check if hand has all the letters in the word
            #print "This word contains letters that are not in given hand"
            return False  
        else: hand_copy[letter] -= 1
    if word in word_list:
        return True
    else:
        print"This word is not in the word list"
        return False
    

def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made with the
    given hand.
    Return '.' if no words can be made with the given hand.
    """
    word_exist = False
    for word in points_dict.keys():
        if is_valid_word(word, hand, word_list):
            if not word_exist:
                best_word =  word
                word_exist = True
            else:
                if points_dict[word] > points_dict[best_word]:
                    best_word = word
    if word_exist:
        return best_word
    else: return '.'

def pick_best_word_faster(hand, rearrange_dict):
    """The same as pick_best_word but faster(is it!?)"""
    word_exist = False
    hand_listed = list()
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand_listed.append(letter)
    #Create all combinations of hand, sort it and check is it in rearrange_dict

    word_exist = False
    for i in range(1, len(hand_listed) + 1):
        for subset in itertools.combinations(hand_listed, i):
            subset = list(subset)
            subset.sort()
            possible_word = str('')
            for letter in subset:
                possible_word += str(letter)
            if possible_word in rearrange_dict:
                if type(rearrange_dict[possible_word]) == 'list':
                    word = rearrange_dict[possible_word][0]
                else: word = rearrange_dict[possible_word]
                if not word_exist:
                    word_exist = True
                    best_word = word
                else: 
                    if get_word_score(word, 100) > get_word_score(best_word, 100):
                        best_word = word
    print word_exist
    if word_exist:
        return best_word
    else: return '.'

##TEST
#pbwf = pick_best_word_faster(deal_hand(10), rearrange_dict)
#print pbwf, get_word_score(pbwf,100)

    
    

def get_time_limit(points_dict, k = 0.5):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    x = 1 
    x = x * 10 - 10 + 10 * 10 / 10
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k
##TEST
#print get_time_limit(points_dict, 1)
   
    
#
# Problem #4: Playing a hand
#

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
#    def getScore(hand, totalScore, word_list): #Recursive function that helps count score  # I DONT LIKE RECURSIVE FUNCTION
#        while True:
#            if len(hand) == 0:
#                return 0
#            print "Your hand is: "
#            display_hand(hand)
#            start_time = time.time()
#            word = raw_input(" Please Enter your word. Enter dot('.') to finish: ")
#            if word == '.':
#                return 0
#            if is_valid_word(word, hand, word_list):
#                end_time = time.time()
#                time_spent = end_time - start_time
#                print "You spent {0:.2f} sec. on word '{1}'".format(time_spent, word)
#                wordScore = get_word_score(word,n) / time_spent
#                totalScore = totalScore + wordScore 
#                print "The word \"", word, "\" IS IN A LIST! Score = {0:.2f}".format(wordScore)
#                print "YOUR NEW SCORE IS: {0:.2f}".format(totalScore)
#                return wordScore + getScore(update_hand(hand, word),totalScore, word_list) 
#    
#    
#        return totalScore



    totalScore = 0
    ##GET TIME LIMIT FOR HUMAN(read as MEATBALL)
    #while True: #Get time limit 
    #    try:
    #        time_limit = float(raw_input("Enter TIME LIMIT in SEC.:"))
    #        break
    #    except:
    #        print "Try again"

    #GET TIME LIMIT FOR COMPUTER PLAYER
    time_limit = get_time_limit(points_dict)
    time_left = float(time_limit) 

    #score = getScore(hand,totalScore, word_list)
    n = len(hand)

    totalScore = 0
    display_hand(hand)
    new_hand = dict(hand)

    while len(new_hand) > 0:
        print "Your hand is: "
        display_hand(new_hand)
        start_time = time.time()
    
        #COMPUTER PLAYER
        print "PLease, mr. ROBOT, Enter your best word"         
        word = pick_best_word_faster(new_hand, rearrange_dict)
        print word
        
        #word = raw_input(" Please Enter your word. Enter dot('.') to finish: ") #human(read as meatball) player

        if word == '.':
            break

        if is_valid_word(word, new_hand, word_list):
            end_time = time.time()
            time_spent = end_time - start_time
            time_left = time_left - time_spent
            if time_left < 0: 
                print "You spent {0:.2f} sec. to provide an answer. \n Total time EXCEEDS {1:.0f} sec.".format(time_spent,time_limit)
                break

            print "You spent {0:.2f} sec. on word '{1}'".format(time_spent, word)
            print "You have {0:.2f} sec. remaining".format(time_left)
            wordScore = get_word_score(word,n) / time_spent
            totalScore = totalScore + wordScore 
            print "The word \"", word, "\" IS IN A LIST! Score = {0:.2f}".format(wordScore)
            print "YOUR NEW SCORE IS: {0:.2f}".format(totalScore)
            new_hand = update_hand(new_hand,word)        

    print "YOUR TOTAL SCORE IS: {0:.2f}".format(totalScore)


#play_hand(deal_hand(7),word_list) #TEST


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

