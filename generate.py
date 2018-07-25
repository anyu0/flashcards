#!/usr/local/bin/python
import os
import sys
import random
import parser

opts = {
    'alternate' : False,
    'shuffle'   : False,
    'nocolor'   : False,
    'invert'    : False
}

class Color:
    def __init__(self):
        self.c1   = '\033[92m'
        self.c2   = '\033[94m'
        self.c3   = '\033[96m'
        self.end  = '\033[0m '
    def disable(self):
        self.c1  = ''
        self.c2  = ''
        self.c3  = ''
        self.end = ' '

decks = []
files = []

def usage():
    print("""usage: flashcard: [-h] [-s] [-a] [-i] file1 [file2]
        -h    Show this help
        -s    Shuffle the deck
        -a    Alternate the first side of the card to be shown, randomly
        -n    No color in output
        -i    Invert the order of sides of the card to be shown""")

# Returns the number of lines in file f.
def line_count(f):
    with open(f) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

# Get the options and filenames
def parse_args(args):
    end_args = False
    for a in args:
        end_args = end_args or a == '--'
        if not end_args and a.startswith('-'):
            if a == '-a':
                opts['alternate'] = True
                continue
            if a == '-s':
                opts['shuffle'] = True
                continue
            if a == '-n':
                opts['nocolor'] = True
                continue
            if a == '-i':
                opts['invert'] = True
                continue
            if a == '-h':
                usage()
                sys.exit()
            else:
                usage()
                sys.exit()
        else:
            if a != '--':
                files.append(a)
    if len(files)==0:
        usage()
        sys.exit()

def read_decks(args):
    if len(args)==1:
        f = open(args)
        try:
            st = f.read()
            deck = eval(st)
        except:
            print("flashcard: dictionary file contains errors")
            sys.exit()
        decks.append(list(deck.keys()))
        decks.append(list(deck.values()))
        # deck[0] = key/hint && deck[1] = value/answer
        return len(deck.keys())

def flashcards(unused):
    while len(unused) != 0:
        c = unused[0]
        if opts['shuffle']:
            c = random.choice(unused)
        flip = False
        if opts['invert']:
            flip = True
        if opts['alternate']:
            flip = random.choice([0, 1])
        try:
            popcards(flip)
        except (KeyboardInterrupt, EOFError):
            sys.exit()
        unused.remove(c)

def popcards(flip):
    t = Color()
    if opts['nocolor']:
        t.disable()
    hint = int(flip)
    ans = int(not flip)
    print(t.c1+"Q:"+t.end+decks[hint][c])
    ans = input(t.c2+"A: "+t.end)
    if ans == '--':
        sys.exit()
    print(t.c3+"    "+str(decks[ans][c])+t.end)

def main(args):
    t = Color()
    parse_args(args)
    num_words = read_decks(files)
    print(t.c3+"There are {} words in the deck.".format(str(num_words))+t.end)
    unused = list(range(0, num_words))
    flashcards(unused)

if __name__ == '__main__':
    main(sys.argv[1:])
