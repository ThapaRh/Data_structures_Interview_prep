"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""

#TC= O(N) SC=O(N)

class Trie:
    def __init__(self):
        self.children={}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.root=Trie()
        

    def addWord(self, word: str) -> None:
        node= self.root
        for w in word:
            if w not in node.children:
                node.children[w]=Trie()
            node=node.children[w]
        node.word=True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            node = root
            for i in range(j,len(word)):
                c=word[i]
                if c !=".":
                    if c not in node.children:
                        return False
                    node=node.children[c]
                else:
                    for v in node.children.values():
                        if dfs(i+1,v):
                            return True
                    return False
            return node.word
        return dfs(0,self.root)a