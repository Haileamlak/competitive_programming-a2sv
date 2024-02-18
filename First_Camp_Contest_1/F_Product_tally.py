n = int(input())
nums = list(map(int, input().split()))

num_of_negative = 0
even_negatives = 0
odd_negatives = 0

ans_positive = 0
for i in range(n):
    if num_of_negative % 2 == 0:
        even_negatives += 1
    else:
        odd_negatives += 1

    if nums[i] < 0:
        num_of_negative += 1

    if num_of_negative % 2 == 0:
        ans_positive += even_negatives
    else:
        ans_positive += odd_negatives

total = n * (n + 1) // 2
print(total - ans_positive, ans_positive)