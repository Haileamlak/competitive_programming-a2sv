class Solution:
    def average(self, salary: List[int]) -> float:
        sum = salary[0]
        min = salary[0]
        max = salary[0]
        for i in range(1, len(salary)):
            sum += salary[i]
            if salary[i] > max:
                max = salary[i]
            elif salary[i] < min:
                min = salary[i]
        
        return (sum - min - max) / (len(salary) - 2)