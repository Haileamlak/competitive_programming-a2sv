def make_beautiful(nums, left, right):
    if left == right:
        return (True, nums[left], nums[right], 0)
    
    mid = (left + right) // 2
    left = make_beautiful(nums, left, mid )
    right = make_beautiful(nums, mid + 1, right)

    res = -1
    if left[2] < right[1]:
        res = 0
    elif right[2] < left[1]:
        res = 1

    isBeautiful = left[0] and right[0] and (res > -1)

    return (isBeautiful, min(left[1], right[1]), max(left[2], right[2]), res + left[3] + right[3])


for _ in range(int(input())):
    m = int(input())
    nums = list(map(int, input().split()))

    res = make_beautiful(nums, 0, m - 1)
    if not res[0]:
        print(-1)
    else:
        print(res[3])