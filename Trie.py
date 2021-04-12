class TrieNode:
    def __init__(self, char=None):
        self.value = char if char else "HEAD"   # Value
        self.children = {}  # Children/child-nodes
        self.has_entry = False  # Whether or not this marks the end of a word

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

    # Points to delete from: intersection, last word 
    def delete(self, string):
        # Test if there is no string to delete
        if string == "":
            return

        current = self
        del_key, del_loc = string[0], self.children

        for i in range(len(string)):
            s = string[i]

            current = current.children
            # Check if the string exists
            if s not in current:
                return    

            # Gets the deletion point: last possible intersection or last possible non-current overlapping word
            if len(current[s].children) > 1 or (current[s].has_entry and s != string[-1]):
                del_loc = current[s].children
                del_key = string[i+1]

            current = current[s]

        # If more children exist, then change to false, else delete from del_loc
        if len(current.children) > 0:
            del_loc[del_key].has_entry = False
        else:
            del_loc.pop(del_key, None)        

    # Stack-based implementation to print everything in trie
    def display(self, depth = 0):
        if self.value == "HEAD":
            depth -= 1
        else:
            print("-"*depth + self.value + (" (T)" if self.has_entry else ""))
        # Recursively displays values for every node in the trie
        for char, node in self.children.items():
            node.display(depth+1)
        
        if depth == -1:
            print("\n")


t = TrieNode()
t.add("abcd")
t.add("giraffe")
t.add("git")
t.add("github")

t.display()
# t.delete("git")
# t.delete("github")
# t.delete("giraffe")
# t.delete("abcd")
# t.display()