
# # def func(x):
# #     return x**2

# # my_list = [1, 3, -4, 6, 7]
# # my_list.sort(reverse=False)
# my_list = {x**2 for x in range(10) if  x % 2}
# print(my_list)

original_dict = {'key1': ['value1'], 'key2': 'value2'}
shallow_copied_dict = original_dict.copy()
original_dict['key1'].append('value3')
original_dict['key2'] = "value4"
print(shallow_copied_dict)