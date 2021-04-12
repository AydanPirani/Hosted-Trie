class TrieNode:
    def __init__(self, char=None):
        self.value = char if char else "HEAD" #Value
        self.children = {} #Children/child-nodes
        self.has_entry = False #Whether or not this marks the end of a word

    def add(self, string):
        current = self
        # Iterate through every character, and add it if it exists
        for s in string:
            current = current.children
            if s not in current:
                current[s] = TrieNode(s)
            current = current[s]
        # Clarifies that a word ends here (for the autocomplete/remove feature)
        current.has_entry = True

t = TrieNode()
t.add("abcd")
t.add("giraffe")
v = t.value
c = t.children
print(t)
print(v)
print(c)
