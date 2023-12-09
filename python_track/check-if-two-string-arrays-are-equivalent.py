class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str_word1 = ""
        for word in word1:
            str_word1 += word

        str_word2 = ""
        for word in word2:
            str_word2 += word
        
        return str_word1 == str_word2