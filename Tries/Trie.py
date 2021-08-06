'''
TRIE SAMPLE
Created by Pierre Lingat 
Date: 05/08/21
'''
ALPHABET_SIZE = 26

class Node:

    # node for the trie
    def __init__(self):
        # there are 26 letters in the alphabet, duplicates shouldn't exist
        self.children = [None]*26

        # represents the end of the word, True if node is
        self.isEnd = False


class Trie:

    # Trie data structure
    def  __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return Node()

    # this was found on geeksforgeeks 
    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
         
        return ord(ch)-ord('a')
 
    def insert(self, word):

        trie = self.root
        wordLength = len(word)
        for ch in range(wordLength):
            index = self._charToIndex(word[ch])

            if not trie.children[index]:
                trie.children[index] = Node()
            trie = trie.children[index]

        trie.isEnd = True

    def search(self, word):
        trie = self.root
        wordLength = len(word)

        for ch in range(wordLength):
            index = self._charToIndex(word[ch])
            if not trie.children[index]:
                return False
            trie = trie.children[index]
        return trie.isEnd



def displayTrie(trieNode, word, index):
    if index != -1:
        word = word + chr(ord('a') + index)

    if(trieNode.isEnd):
        print(word)
        word = ""
  
    for child in range(len(trieNode.children)):
        if(trieNode.children[child] != None):
            displayTrie(trieNode.children[child], word, child)
        


def main():
 
    # Input keys (use only 'a' through 'z' and lower case)
    words = ["hello", "how", "alone", "biscuit", "the", "these"]
    output = ["Not present in trie",
              "Present in trie"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for word in words:
        t.insert(word)

    print("Trie: ")
    displayTrie(t.root, "", -1)

    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
 
if __name__ == '__main__':
    main()