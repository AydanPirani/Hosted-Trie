from trie import *

trie = TrieNode()

def test_add():
    # add1
    trie.clear()
    trie.add("git")
    assert trie.display() == "\ng\n-i\n--t*\n", "Test case add1 failed."
    # add2
    trie.add("github")
    assert trie.display() == "\ng\n-i\n--t*\n---h\n----u\n-----b*\n", "Test case add2 failed."
    # add3
    trie.add("slingshot")
    assert trie.display() == "\ng\n-i\n--t*\n---h\n----u\n-----b*\ns\n-l\n--i\n---n\n----g\n-----s\n------h\n-------o\n--------t*\n", \
        "Test case add3 failed."
    trie.clear()

def test_delete():
    # delete1
    trie.clear()
    trie.add("git")
    trie.delete("git")
    assert trie.display() == "\n", "Test case delete1 failed."
    # delete2
    trie.clear()
    trie.add("git")
    trie.add("github")
    trie.delete("git")
    assert trie.display() == "\ng\n-i\n--t\n---h\n----u\n-----b*\n", "Test case delete2 failed."
    # delete3
    trie.clear()
    trie.add("git")
    trie.add("github")
    trie.delete("github")
    assert trie.display() == "\ng\n-i\n--t*\n", "Test case delete3 failed."
    trie.clear()

def test_search():
    trie.clear()
    trie.add("git")
    # search1
    assert trie.search("git"), "Test case search1 failed."
    # search2
    trie.add("git")
    assert trie.search("gi") == False, "Test case search2 failed."
    trie.clear()

def test_autocomplete():
    trie.clear()
    trie.add("git")
    trie.add("github")
    # autocomplete1
    assert trie.autocomplete("gi") == ["git", "github"], "Test case autocomplete1 failed."
    # autocomplete2
    assert trie.autocomplete("gith") == ["github"], "Test case autocomplete2 failed."
    # autocomplete3
    assert trie.autocomplete("git") == ["git", "github"], "Test case autocomplete3 failed."
    # autocomplete4
    assert trie.autocomplete("slingshot") == [], "Test case autocomplete4 failed."
    trie.clear()

def test_display():
    trie.clear()
    # display1
    assert trie.display() == "\n", "Test case display1 failed."
    # display2
    trie.add("git")
    trie.add("github")
    assert trie.display() == "\ng\n-i\n--t*\n---h\n----u\n-----b*\n", "Test case display2 failed."
    # display3
    trie.add("slingshot")
    assert trie.display() == "\ng\n-i\n--t*\n---h\n----u\n-----b*\ns\n-l\n--i\n---n\n----g\n-----s\n------h\n-------o\n--------t*\n", \
        "Test case display3 failed."
    print(repr(trie.display()))

if __name__ == "__main__":
    test_add()
    test_delete()
    test_search()
    test_autocomplete()
    test_display()
    print("All test cases passed!")