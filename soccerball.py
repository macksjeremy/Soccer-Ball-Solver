import nltk

def works(input):
    if(len(input) < 7):
        return False
    letters = ['y', 'b', 'i', 'a', 'l', 'u', 'n']
    for i in input:
        if i in letters:
            letters.remove(i)
    if (len(letters)==0):
        english_vocab = set(w.lower() for w in nltk.corpus.words.words())
        if input in english_vocab:
            print(input)
            return True
    else:
        return False

def build(stringput):
    letters = ['b', 'i', 'a', 'l', 'u', 'n','y']
    print(stringput)
    if(works(stringput)):
        print(stringput)
    if (len(stringput) == 8 or "yy" in stringput or "aa"in stringput or "ii" in stringput or "uu" in stringput):
            return
    for i in letters:
        build(stringput + i)



build("")

