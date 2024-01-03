class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()

        chemistry = 0
        left = 0
        right = len(skill) - 1

        skl = skill[0] + skill[-1]
        while left < right:
            if skill[left] + skill[right] != skl:
                return -1
            
            chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1

        return chemistry