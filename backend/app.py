from flask import Flask, request
from trie import *
import threading

app = Flask(__name__)
trie = TrieNode()
lock = threading.Lock()

@app.route('/')
def hello():
    data = request.json
    return "Server is running!"

@app.route("/add", methods=["GET", "POST"])
def add():
    with lock:
        string = request.form["string"]
        trie.add(string)
        return f"The key \"{string}\" has been added to the trie!\n"

@app.route("/delete", methods=["GET", "POST"])
def delete():
    with lock:
        string = request.form["string"]
        trie.delete(string)
        return f"The key \"{string}\" has been removed from the trie!\n"

@app.route("/search", methods=["GET", "POST"])
def search():
    with lock:
        string = request.form["string"]
        in_trie = trie.search(string)
        return f"The key \"{string}\" was " +  ("" if in_trie else "not ") + "found in the existing trie!\n"

@app.route("/autocomplete", methods=["GET", "POST"])
def autocomplete():
    with lock:
        prefix = request.form["string"]
        words = trie.autocomplete(prefix)
        if len(words) < 1:
            return f"No autocomplete results for the prefix \"{prefix}\" were found in the trie!\n"
        else:
            return f"The prefix \"{prefix}\" has the following autocomplete results:\n{words}\n"

@app.route("/display", methods=["GET", "POST"])
def display():
    with lock:
        stringified_trie = trie.display()
        if len(stringified_trie.split()) == 0:
            stringified_trie = "\nNULL (Empty)\n"
        return f"The current state of the trie is as such:{stringified_trie}"

@app.route("/clear", methods=["GET", "POST"])
def clear():
    trie.clear()
    return "The trie has been reset!\n"

if __name__ == '__main__':
    app.run()