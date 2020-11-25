import nltk
from nltk.corpus import words as words
import time


'''
def isvowel(letter):
    if letter in ['a','e','i','o','u','y']:
        return True
    else:
        return False
#def threeconsonants(stringinput):

def trippling(chars):
    return chars + chars + chars

def threeletter(chars, string):
    map()

def works(input):
    print(english_vocab)
    if(len(input) < 7):
        return False
    letters = ['y', 'b', 'i', 'a', 'l', 'u', 'n']
    for i in input:
        if i in letters:
            letters.remove(i)
    if (len(letters)==0):
        if input in english_vocab:
            print(input)
            return True
    else:
        return False

def build(stringput):
    letters = ['b', 'i', 'a', 'l', 'u', 'n','y']
    if (len(stringput) == 10 or "yy" in stringput or "aa"in stringput or "ii" in stringput or "uu" in stringput):
        return
    #print(stringput)
    if(works(stringput)):
         print(stringput)
    for i in letters:
        build(stringput + i)
#
#
#Maybe i'm coming at this the wrong way.
#build("")
'''
#No longer necessary, but useful!
#def split(word):
#    return [char for char in word]

#make sure the string is only made up of characters from input
def removelist(input,string):
    #print(string)
    strcpy = string
    for i in input:
        strcpy = strcpy.replace(i,"")
    #print(strcpy)
    if len(strcpy) > 0:
        return False
    else:
        print(string)
        return True

#run through the corpus, check if the word uses all letters from input.
def parsethrough(input):
    english_vocab = [w.lower() for w in words.words()]
    for i in english_vocab:
        found = True
        for j in input:
            if j not in i:
                found = False
        if found and removelist(input, i):
            #check other letter possiblity
            print(i)
            return True

#So it turns out wordnet does not contain every word in the english language.


#run parsethrough on input, which runs through the whole corpus
k = time.time()
input = ['e', 'c', 'r', 'h', 'v', 'n', 'o']
#print(words.words())
parsethrough(input)
print("Time elapsed is:",time.time() - k)

