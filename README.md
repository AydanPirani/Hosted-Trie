# Hosted-Trie
A project I built, consisting of a CLI and backend-hosted trie. This project had two parts: a cloud-based server (found in the backend folder) and a CLI (found in the trie-cli folder). The backend was a Flask-based Python app, hosted on PythonAnywhere at [aydanpirani.pythonanywhere.com/](aydanpirani.pythonanywhere.com) (note that this is no longer hosted). Every time the user accesses the CLI and performs an operation, the CLI sends a HTTP request to the Flask server, and globally modifies the trie in-place (or returns the stringified values in the trie, depending on the operation performed).

### Table of Contents
[CLI Installation and Usage](#cli-installation-and-usage)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Installation](#installation)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Usage](#usage)  
[REST Endpoints/CURL Testing](#rest-endpointscurl-testing)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/add](#add)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/delete](#delete)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/search](#search)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/autocomplete](#autocomplete)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/display](#display)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [/clear](#clear)

# CLI Installation and Usage
## Installation  
The CLI can be installed via the NPM registry, hence NodeJS must be installed as a prerequisite. The recommended method of installation is as a global NPM package, with the following commands:
```
# Installs the CLI command
$ sudo npm install -g @aydan/trie-cli

# Uninstalls the CLI command
$ sudo npm uninstall -g @aydan/trie-cli
```

## Usage  
The CLI be run with and without arguments.

### Without Arguments
The user will be prompted to select an operation and a string (if needed). The following command can be used:
```
$ trie-cli
```

### With Arguments
To run the CLI with arguments, the following format is used, where OPERATION is replaced by one of the following: ["add", "delete", "search", "autocomplete", "display"]. "Display" is the only standalone command in the context of arguments - all other arguments require an additional parameter STRING, which is required to perform the operation. If there is no second argument provided, the user will be prompted to enter a valid string.
```
# All non-display operations
$ trie-cli OPERATION STRING

# Display operation
$ trie-cli display
```
# REST Endpoints/CURL Testing
Trie tests can be found within backend/tests.py - this file can be run to test the validness of the trie data structure. Global tests can be run with the following CURL commands: 
### /add
Takes in a passed dictionary of the form {"string":"word"}, adds word to the trie.
```
$ curl -X POST -F "string=word" aydanpirani.pythonanywhere.com/add
```
### /delete
Takes in a passed dictionary of the form {"string":"word"}, deletes word from the trie (if it exists).
```
$ curl -X POST -F "string=word" aydanpirani.pythonanywhere.com/delete
```
### /search
Takes in a passed dictionary of the form {"string":"word"}, checks if the word exists within the given trie.
```
$ curl -X POST -F "string=word" aydanpirani.pythonanywhere.com/search
```
### /autocomplete
Takes in a passed dictionary of the form {"string":"prefix"}, returns all existing words in the trie with the given prefix (if they exist).
```
$ curl -X POST -F "string=prefix" aydanpirani.pythonanywhere.com/autocomplete
```
### /display
Prints the currently-existing trie to the user's console.
```
$ curl -X GET aydanpirani.pythonanywhere.com/display
```
### /clear
Completely resets the state of the trie (for debugging purposes). Use only if you are certain you want to delete the trie.
```
$ curl -X GET aydanpirani.pythonanywhere.com/clear
```
