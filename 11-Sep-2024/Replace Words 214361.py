# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for letter in word:
            i = ord(letter) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            
            curr = curr.children[i]

        curr.is_end = True

    def find_root(self, word):
        curr = self.root
        answer = []
        for index, letter in enumerate(word):
            i = ord(letter) - ord('a')
            if not curr.children[i]:
                return len(word)
            
            curr = curr.children[i]

            if curr.is_end:
                return index + 1
        
        return len(word)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie_dictionary = Trie()
        for word in dictionary:
            trie_dictionary.insert(word)
        
        answer = []
        for successor in sentence.split(' '):
            index = trie_dictionary.find_root(successor)
            answer.append(successor[:index])
        
        return ' '.join(answer)