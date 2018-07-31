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

files = []
dictionary = {}
deck = []

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

def read_deck(args):
    if len(args)==1:
        f = open(args[0])
        try:
            st = f.read()
            global dictionary
            dictionary = eval(st)
        except:
            print("flashcard: dictionary file contains errors")
            sys.exit()
        return len(dictionary.keys())

def flashcards(deck):
    while len(deck) != 0:
        nxt = deck[0]
        if opts['shuffle']:
            nxt = random.choice(deck)
        flip = False
        if opts['invert']:
            flip = True
        if opts['alternate']:
            flip = random.choice([0, 1])
        try:
            showcards(nxt,flip)
        except (KeyboardInterrupt, EOFError):
            sys.exit()
        deck.remove(nxt)

def showcards(nxt,flip):
    t = Color()
    global deck
    global dictionary
    if opts['nocolor']:
        t.disable()
    card = [nxt,dictionary[nxt]]
    hint = card[int(flip)]
    response = card[int(not flip)]
    print(t.c1+"Q:"+t.end+ hint)
    ans = input(t.c2+"A:"+t.end)
    if ans == '--':
        sys.exit()
    print(t.c3+"   "+ response +t.end)

def main(args):
    t = Color()
    parse_args(args)
    num_words = read_deck(files)
    print(t.c3+"There are {} words in the deck.".format(str(num_words))+t.end)
    global deck
    deck = list(dictionary.keys())
    flashcards(deck)

if __name__ == '__main__':
    main(sys.argv[1:])
