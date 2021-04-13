class TrieNode:
    def __init__(self, char=None):
        self.value = char if char else ""   # Value
        self.children = {}  # Children/child-nodes
        self.has_entry = False  # Whether or not this marks the end of a word

    def add(self, string):
        string = string.lower()
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

        string = string.lower()

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
            current.has_entry = False
        else:
            del_loc.pop(del_key, None)        

    # Search if the string has been entered in the structure
    def search(self, string):
        string = string.lower()
        current = self
        for s in string:
            current = current.children
            if s not in current:
                return False
            
            current = current[s]

        return current.has_entry

    # Return all potential "autocompletes" with given prefix
    def autocomplete(self, string):
        current = self
        for s in string:
            current = current.children
            if s not in current:
                return []
            current = current[s]
        
        if len(string) > 0:
            string = string[:-1]

        stack, words = [(current, string)], []
        while len(stack) > 0:
            node, word = stack.pop()
            word += node.value
            # Might seem like O(N^2), but is a DFS, thus O(N)
            for child in node.children: 
                stack.append((node.children[child], word))  
            if node.has_entry:
                words.append(word)
              
        return words
        
    # Stack-based implementation to print everything in trie
    def display(self, depth = 0, stub = ""):
        if self.value == "":
            depth -= 1
            stub += "\n"
        else:
            stub = ("-"*depth + self.value + ("*" if self.has_entry else "")+"\n")
        # Recursively displays values for every node in the trie
        for char, node in self.children.items():
            stub += node.display(depth+1, stub)
        return stub

    # Internal method for debugging purposes
    def clear(self):
        self.children = {}
        self.value = ""
        self.has_entry = False
        return