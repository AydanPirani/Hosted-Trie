class TrieNode:
    def __init__(self, char=None):
        self.value = char if char else "HEAD"
        self.children = {}


t = TrieNode()
v = t.value
c = t.children
print(t)
print(v)
print(c)