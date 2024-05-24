# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            
            curr = curr.children[index]
        
        curr.is_end = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    def _search(self, word, curr):
        if not word:
            return curr.is_end
        
        for i, letter in enumerate(word):
            if letter == '.':
                for child in curr.children:
                    if child and self._search(word[i + 1:], child):
                        return True
                
                return False

            if not curr.children[ord(letter) - ord('a')]:
                return False
            
            curr = curr.children[ord(letter) - ord('a')]

        return curr.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)