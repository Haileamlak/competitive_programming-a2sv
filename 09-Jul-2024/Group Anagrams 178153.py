# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)

        for string in strs:
            temp[str(sorted(string))].append(string)
        
        return [temp[key] for key in temp.keys()]