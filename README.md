# Hosted-Trie
The final take-home project, made for Slingshot's Fellowship program.

# REST Endpoints/CURL Testing
/add
Takes in a passed dictionary of the form {"string":"word"}, adds word to the trie.
```
CURL -X POST -F "string=word" aydanpirani.pythonanywhere.com/add
```
/delete
Takes in a passed dictionary of the form {"string":"word"}, deletes word from the trie (if it exists).
```
CURL -X POST -F "string=word" aydanpirani.pythonanywhere.com/delete
```
/search
Takes in a passed dictionary of the form {"string":"word"}, checks if the word exists within the given trie.
```
CURL -X POST -F "string=word" aydanpirani.pythonanywhere.com/search
```
/autocomplete
Takes in a passed dictionary of the form {"string":"prefix"}, returns all existing words in the trie with the given prefix (if they exist).
```
CURL -X POST -F "string=prefix" aydanpirani.pythonanywhere.com/autocomplete
```
/display
Prints the currenntly-existing trie to the user's console.
```
CURL -X GET aydanpirani.pythonanywhere.com/display
```
/clear
Completely resets the state of the trie.
```
CURL -X GET aydanpirani.pythonanywhere.com/clear
```
