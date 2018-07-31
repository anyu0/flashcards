# Flashcards
a python program to generate flashcards from .txt files in command line

## Prepare a dictionary
* Write a .txt file under the directory ./unprocessed/ in the following format
```
hint; answer
...
```

* Generate a dictionary by typing in the command line

```shell
python3 mkdict ./unprocessed/filename.txt
```

## Use an existing dictionary 

* Make a deck of flashcards by entering

```shell
python3 flashcard ./processed/filename.txt
```

