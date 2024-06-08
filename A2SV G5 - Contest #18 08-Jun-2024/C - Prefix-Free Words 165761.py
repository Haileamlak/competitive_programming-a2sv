# Problem: C - Prefix-Free Words - https://codeforces.com/gym/526229/problem/C


class TrieNode:
    def __init__(self):
        self.ch = [None, None]
        self.is_end = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, length):
        stack, trie = [], self.root 
        word = []
        # finding a unique word representation with the given length
        for i in range(length):
            stack.append(trie) 
            if trie.ch[0] is None or not trie.ch[0].is_end:
                if trie.ch[0] is None:
                    trie.ch[0] = TrieNode()
                trie = trie.ch[0]
                word.append('0')
            elif trie.ch[1] is None or not trie.ch[1].is_end:
                if trie.ch[1] is None:
                    trie.ch[1] = TrieNode()
                trie = trie.ch[1]
                word.append('1')
            else:
                return False
        trie.is_end = True

        # backtrcking to update the is_end of the nodes if they don't have unoccopied child for the word represetnation
        while stack and stack[-1].ch[1] and stack[-1].ch[1].is_end:
            prev = stack.pop()
            prev.is_end = True

        return ''.join(word)

def main():
    n = int(input())    
    nums = sorted(zip(map(int, input().split()), range(n)))
    trie = Trie()
    words = [''] * n
    for num, indx in nums:
        word = trie.insert(num)
        if not word:
            print('NO')
            return
        words[indx] = word

    print('YES')
    for word in words:
        print(word)

if __name__ == '__main__':
    main()