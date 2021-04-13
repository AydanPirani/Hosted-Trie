# Hosted-Trie
The final take-home project, made for Slingshot's Fellowship program.

### Table of Contents
[REST Endpoints/CURL Testing](#rest-endpointscurl-testing)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/add](#add)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/delete](#delete)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/search](#search)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/autocomplete](#autocomplete)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/display](#display)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/clear](#clear)

# REST Endpoints/CURL Testing
### /add
Takes in a passed dictionary of the form {"string":"word"}, adds word to the trie.
```
CURL -X POST -F "string=word" aydanpirani.pythonanywhere.com/add
```
### /delete
Takes in a passed dictionary of the form {"string":"word"}, deletes word from the trie (if it exists).
```
CURL -X POST -F "string=word" aydanpirani.pythonanywhere.com/delete
```
### /search
Takes in a passed dictionary of the form {"string":"word"}, checks if the word exists within the given trie.
```
CURL -X POST -F "string=word" aydanpirani.pythonanywhere.com/search
```
### /autocomplete
Takes in a passed dictionary of the form {"string":"prefix"}, returns all existing words in the trie with the given prefix (if they exist).
```
CURL -X POST -F "string=prefix" aydanpirani.pythonanywhere.com/autocomplete
```
### /display
Prints the currently-existing trie to the user's console.
```
CURL -X GET aydanpirani.pythonanywhere.com/display
```
### /clear
Completely resets the state of the trie (for debugging purposes). Use only if you are certain you want to delete the trie.
```
CURL -X GET aydanpirani.pythonanywhere.com/clear
```
