# Problem Set 5: Ghost
# Name: Bohdan Drahan 
# Time: 5:00
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

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

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

print "aa" in wordlist
def ghost():
    """ goast game """
    
    print "WELCOME TO GHOST GAME!"
    player = 1
    word = "" 
    gameIsNotFinished = True
    while gameIsNotFinished:
        print player
        print "CURRENT WORD IS: ",word
        print "Player",player,"'s turn. Player",player," says letter:"
        while True:
            letter = raw_input("ENTER YOUR LETTER: ")
            if letter == '.':
                return
            if len(letter) > 1:
                print "Enter just one letter, no more no more no more no more"
            elif not letter.isalpha():
                print "Enter a letter, not any symbol"
            letter = letter.upper()
            break   
        word = word + letter
        beginWordExist = False 
        for each in wordlist:
            if len(each) >= len(word):
                if word == each.upper()[:len(word)]:
                    beginWordExist = True
        if beginWordExist == False:
            print "Player", player, " LOST! There are NO words begin whith '", word, "'"
            looser = player
            return looser
        print word
        if len(word) > 3:
            for everyWord in wordlist:
                if word == everyWord.upper():
                    print "Player", player, " LOST! '", word,"' is A WORD!" 
                    looser = player
                    return looser
        if player == 1:
            player = 2
        else: player = 1
        
                
                    

           
    
    

               

ghost()
