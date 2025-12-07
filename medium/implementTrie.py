#create the node that your tree uses
class TrieNode:
  #each has a dict of letters and a boolean indicating the end of the word 
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:
 # initialize the root of the tree
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word: # loop through the word 
            if c not in curr.children: # if the character doesn't appear in the children dict, it's added 
                curr.children[c] = TrieNode() #the character is added to children,
            curr = curr.children[c]
        curr.endOfWord = True #after every character is added, we set the boolean in the last character node to false, ending the word.
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word: # simalar to the precious method the word iterated though but 
            if c not in curr.children:
                return False #return if the character doesn't appear in the children dict 
            curr = curr.children[c]
        return curr.endOfWord # if all the characters appear, proving the word exists. The attribute endofword is checked, and if true, the word exists; otherwise, the prefix does

        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix: # nearly identical to the search except we return true instead of checking the attribute endofword because we are just looking for the prefix
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        
