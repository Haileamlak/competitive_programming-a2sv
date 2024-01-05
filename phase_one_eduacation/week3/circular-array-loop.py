class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def getNext(i, direction, nums):
            if direction != (nums[i] > 0):
                return -1
            
            index = (i + nums[i]) % len(nums)
            if index < 0:
                index += len(nums)
            
            if index == i:
                return -1
            
            return index

        for i in range(len(nums)):
            slow = fast = i
            direction = nums[i] > 0
            while(True):
                slow = getNext(slow, direction, nums)
                if slow == -1:
                    break
                
                fast = getNext(fast, direction, nums)
                if fast == -1:
                    break

                fast = getNext(fast, direction, nums)
                if fast == -1:
                    break
                
                if slow == fast:
                    return True

        return False                 


        # def isCycle(i):
        #     seen = {}
        #     isPos = True
        #     while True:
        #         if i in seen:
        #             if nums[i] != abs(nums[i]):
        #                 isPos = False
        #             break
        #         else:
        #             seen[i] = nums[i]
        #             i += nums[i]
        #             i %= len(nums)
            
        #     if len(seen) == 1:
        #         return False
        #     else:
        #         for i in seen:
        #             if isPos:
        #                 if seen[i] < 0:
        #                     return False
        #             else:
        #                 if seen[i] > 0:
        #                     return False
        #     return True
            
        # for i in range(len(nums)):
        #     if isCycle(i):
        #         return True
        
        # return False
