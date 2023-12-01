class Solution:   
    def areSorted(self, str1, str2, order):
        if str2 == '' and str1 == '':
            return True
        if str2 == '' and str1 != '':
            return False
        elif str1 == '' and str2 != '':
            return True
        elif order.find(str1[0]) > order.find(str2[0]):
            return False
        elif order.find(str1[0]) == order.find(str2[0]):
            return self.areSorted(str1[1:], str2[1:], order)
        else:
            return True
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            if not self.areSorted(words[i], words[i + 1], order):
                return False
        
        return True


