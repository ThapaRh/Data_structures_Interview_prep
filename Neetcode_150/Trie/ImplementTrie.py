"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""
# insert:  TC=O(N)  SC=O(N)
#search and startswith TC=-O(N)  SC=O(1)

class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfnode=False
class Trie:

    def __init__(self):
        self.root=TrieNode()        

    def insert(self, word: str) -> None:
        child=self.root
        for w in word:
            if w not in child.children:
                newNode=TrieNode()
                child.children[w]=newNode
            child=child.children[w]
        child.endOfnode=True

    def search(self, word: str) -> bool:
        cur=self.root
        for w in word:
            if w not in cur.children:
                return False
            cur=cur.children[w]
        return cur.endOfnode
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur=cur.children[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)