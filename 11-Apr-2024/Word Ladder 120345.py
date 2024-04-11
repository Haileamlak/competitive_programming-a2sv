# Problem: Word Ladder - https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        possible = set(wordList)
        
        if endWord not in possible:
            return 0

        visited = set([beginWord])
        queue = deque([beginWord])
        count = 1
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == endWord:
                    return count

                next_word = list(curr)
                for j in range(len(next_word)):
                    temp = next_word[j]

                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        next_word[j] = ch
                        word = ''.join(next_word)
                        if word not in visited and word in possible:
                            visited.add(word)
                            queue.append(word)

                    next_word[j] = temp

            count += 1
        
        return 0