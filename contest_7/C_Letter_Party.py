n, k = map(int, input().split())

word = input()

def helper(s, k):
    res = 0
    left = 0
    unique = 0
    for right in range(len(word)):
        if word[right] != s:
            unique += 1

        while left < len(word) and unique > k:
            if word[left] != s:
                unique -= 1
            left += 1
        
        res = max(res, right - left + 1)

    return res
    
print(max(helper('a', k), helper('b', k)))