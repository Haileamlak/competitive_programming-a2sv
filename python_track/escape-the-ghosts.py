class Solution:
    def distance_to_target(self, ghost, target):
        return abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])

    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        me_to_target = self.distance_to_target([0, 0], target)
        for ghost in ghosts:
            print(self.distance_to_target(ghost, target))
            print(me_to_target)
            if self.distance_to_target(ghost, target) <= me_to_target:
                return False

        return True
