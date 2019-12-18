# Flashcards
a python program to generate flashcards in command line

## Clone this repository

```shell
git clone git@github.com:anyu0/flashcards.git
```

## Prepare a dictionary
* Go to the working directory

```shell
cd ./flashcards
```

* Make a plain text file under the ./unprocessed/directory 

```shell
vi ./unprocessed/filename
```

* It should be written in the following format

```
hint; answer
...
```

* Generate a dictionary by entering

```shell
python3 mkdict.py filename
```

## Use an existing dictionary 

* Make a deck of flashcards by entering

```shell
python3 generate.py ./processed/filename
```

## (Optional) Quick move to the flashcards directory
* append the following line in your shell config

 ```shell
 alias flashcard="cd path/to/flashcards"
 ```


