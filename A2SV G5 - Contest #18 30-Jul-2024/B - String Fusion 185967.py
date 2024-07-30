# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B


class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.count = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            i = ord(ch) - 97
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            
            curr = curr.children[i]
            curr.count += 1
        
    def update(self, word):
        res = 0
        curr = self.root
        for j in range(len(word) - 1, -1, -1):
            ch = word[j]
            i = ord(ch) - 97
            if not curr.children[i]:
                break

            curr = curr.children[i]
            res += (2 * curr.count)
            # print(ch)
        return res


n = int(input())
words = []
for _ in range(n):
    words.append(input())

trie = Trie()
length = 0
for word in words:
    trie.insert(word)
    length += len(word)

res = length * n
for word in words:
    res += n * len(word)
    res -= trie.update(word)

print(res)