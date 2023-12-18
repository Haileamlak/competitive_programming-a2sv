
# # def func(x):
# #     return x**2

# # my_list = [1, 3, -4, 6, 7]
# # my_list.sort(reverse=False)
# my_list = {x**2 for x in range(10) if  x % 2}
# print(my_list)

# original_dict = {'key1': ['value1'], 'key2': 'value2'}
# shallow_copied_dict = original_dict.copy()
# original_dict['key1'].append('value3')
# original_dict['key2'] = "value4"
# print(shallow_copied_dict)

word = ["A", "A", "B"]
count = 0
b = 0
i = len(word) - 1
while i >= 0:
    if word[i] == 'B':
        b += 1
    else:
        count += b
        b = 0
        word[i] = 'B'
        i += 1
    
    i -= 1

print(count)
