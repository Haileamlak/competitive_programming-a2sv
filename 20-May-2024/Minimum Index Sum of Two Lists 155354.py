# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_index = [len(list1), len(list2)]
        for i in range(len(list1)):
            if list1[i] in list2:
                index = list2.index(list1[i])
            else:
                index = -1
            if index > -1:
                index_sum = i + index
                if index_sum < least_index[0] + least_index[1]:
                    least_index = [i, index]
                elif index_sum == least_index[0] + least_index[1]:
                    least_index.append(i)
                    least_index.append(index)

        return [list1[least_index[i]] for i in range(0, len(least_index), 2)]
