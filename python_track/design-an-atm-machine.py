# class ATM:

#     def __init__(self):
#         self.notes = [0 for _ in range(5)]

#     def deposit(self, banknotesCount: List[int]) -> None:
#         for i in range(5):
#             self.notes[i] += banknotesCount[i]

#     def withdraw(self, amount: int) -> List[int]:
#         temp = [20, 50, 100, 200, 500]
#         for i in range(4, -1, -1):
#             n = amount // temp[i]
#             if n > self.notes[i]:
#                 temp[i] = 0
#             else:
#                 amount %= temp[i]
#                 temp[i] = n
        
#         if amount:
#             return [-1]
#         for i in range(5):
#             self.notes[i] -= temp[i]
        
#         return temp

# # Your ATM object will be instantiated and called as such:
# # obj = ATM()
# # obj.deposit(banknotesCount)
# # param_2 = obj.withdraw(amount)
class ATM:
    def __init__(self):
        self.ans = [20,50,100,200,500]
        self.res = [0]*5
        
    def deposit(self, banknotesCount):
        for i in range(5):
            self.res[i] += banknotesCount[i]

    def withdraw(self, amount):
        result = [0]*5
        
        for i in range(4,-1,-1):
            n = min(self.res[i],amount//self.ans[i])
            amount -= self.ans[i]*n
            result[i] += n
            
        if amount == 0:
            self.res = [self.res[i] - result[i] for i in range(5)]
            
        return result if amount == 0 else [-1]