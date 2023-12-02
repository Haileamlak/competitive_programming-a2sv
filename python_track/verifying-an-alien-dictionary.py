class Solution:   
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            if not self.areSorted(words[i], words[i + 1], order):
                return False
        
        return True

    def areSorted(self, str1, str2, order):
        if str1 == '':
            return True
        if str2 == '':
            return False
        if order.find(str1[0]) > order.find(str2[0]):
            return False
        if order.find(str1[0]) == order.find(str2[0]):
            return self.areSorted(str1[1:], str2[1:], order)
        return True
            


