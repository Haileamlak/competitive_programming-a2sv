class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char= Counter()

        for ch in chars:
            char[ch] += 1

        count = 0
        for word in words:
            wordd = Counter()
            for ch in word:
                wordd[ch] += 1
            
            for ch, cnt in wordd.items():
                if cnt > char[ch]:
                    break
            else:
                count += len(word)
        
        return count