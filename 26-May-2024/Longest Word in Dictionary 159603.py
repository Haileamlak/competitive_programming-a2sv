# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.is_end = True
    
    def insert_and_update_answer(self, word, ans):
        curr = self.root
        can_be_built = True
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            
            can_be_built = can_be_built and curr.is_end
            curr = curr.children[index]
        
        curr.is_end = True

        if can_be_built and (len(word) > len(ans) or (len(word) == len(ans) and word < ans)):
            ans = word
        
        return ans

class Solution:
    def longestWord(self, words: List[str]) -> str:
        dictionary = Trie()
        words.sort(key = lambda word : len(word))

        ans = ''
        for word in words:
            ans = dictionary.insert_and_update_answer(word, ans)
        
        return ans