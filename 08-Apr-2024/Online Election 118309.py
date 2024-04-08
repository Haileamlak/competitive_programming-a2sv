# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leaders = []

        count = defaultdict(int)
        curr_max = -1
        for person in self.persons:
            count[person] += 1
            if count[person] >= count[curr_max]:
                curr_max = person
            
            self.leaders.append(curr_max)

    def q(self, t: int) -> int:
        index = bisect_left(self.times, t)
        if index < len(self.times) and t == self.times[index]:
            return self.leaders[index]
        
        return self.leaders[index - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)