
import math
from collections import Counter
t = int(input())
for _ in range(t):
   s = input()
  
   arr = []
   got = set()
   count = Counter(s)
   for i in s[::-1]:
       if i not in got:
           arr.append(i)
       got.add(i)
   arr.reverse()
   occur = []
   pos = 1
   for i in range(len(arr)):
       occur.append(count[arr[i]] / (i + 1))
   left = 0
   if math.ceil(sum(occur)) != int(sum(occur)):
       pos = 0
 
   if pos:
       ans = ""
       cur = s[:int(sum(occur))]
       j = 0
  
       while cur:
           ans += cur
           stk = ""
           for i in cur:
               if i != arr[j]:
                   stk += i
           cur = stk
           j += 1
       if ans != s:
           pos = 0
   if pos:
       print(s[:int(sum(occur))],"".join(arr))
   else:
       print(-1)