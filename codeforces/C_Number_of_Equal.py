n, m = map(int, input().split())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

top = 0
bottom = 0
res = 0
while (top < n and bottom < m):
    if (nums1[top] == nums2[bottom]):
        top += 1
        bottom += 1
        i = j = 1;
        while (top < n and nums1[top] == nums1[top - 1]):
            i += 1
            top += 1
        while (bottom < m and nums2[bottom] == nums2[bottom - 1]):
            j+= 1
            bottom += 1
        res += i * j

    elif (nums1[top] < nums2[bottom]):
        top += 1
    else:
        bottom += 1

print(res)