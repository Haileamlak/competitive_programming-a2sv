# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from heapq import heappop, heappush

heap = []
ops = []
n = int(input())
for _ in range(n):
    operation_num = input().split()
    operation = operation_num[0]
    num = int(operation_num[1]) if operation != 'removeMin' else 0

    if operation == 'insert':
        heappush(heap, num)
        ops.append(f'insert {num}')
    
    elif operation == 'getMin':
        while heap and heap[0] < num:
            ops.append('removeMin')
            heappop(heap)
        
        if not heap or heap[0] > num:
            ops.append(f'insert {num}')
            heappush(heap, num)
        
        ops.append(f'getMin {num}')

    else:
        if not heap:
            ops.append(f'insert {num}')
        
        else:
            heappop(heap)
        
        ops.append('removeMin')
    
print(len(ops))
for op in ops:
    print(op)