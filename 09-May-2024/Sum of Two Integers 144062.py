# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Caution: This is not my code. I'm not responsible for anything that could happen to you because of this code.
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a




        # def get_sum(a, b):
        #     res = 0
        #     carry = 0
        #     for i in range(32):
        #         aa, bb = a & (1 << i), b & (1 << i)

        #         sum1 = aa ^ bb
        #         carry1 = aa & bb

        #         sum2 = sum1 ^ carry
        #         carry2 = sum1 & carry


        #         res |= (sum2 << i)

        #         carry = carry1 | carry2
            
        #     return res

#         # def get_sum(a, b):
#         #     while a != 0:
#         #         c = a & b
#         #         b = b ^ a
#         #         c <<= 1
#         #         a = c
            
#         #     return b
        
#         # print(bin(a), bin(~a),int(bin(~a), 2), a)
#         # x = bin()
#         # # if a > b:
#         # #     a, b = b, a

#         # if a < 0 and b < 0:
#         #     return int('-0b' + get_sum(int(bin(~a)[3:]), int(bin(~b)[3:]))[2:], 2)

#         # elif a < 0:
#         #     return get_sum(~abs(a), b)
        
        # return get_sum(a, b)
