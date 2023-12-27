class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(names)):
            temp_height = heights[i]
            temp_name = names[i]
            j = i
            while j >= 1 and temp_height > heights[j - 1]:
                heights[j] = heights[j - 1]
                names[j] = names[j - 1]
                j -= 1

            heights[j] = temp_height
            names[j] = temp_name

        return names