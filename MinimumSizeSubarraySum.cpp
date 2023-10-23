/*
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 */


class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int sz = nums.size();
        int minLength = sz + 1;

        int sum = nums[0];
        int left = 0, right = 0;
        
        while(left < sz && right < sz ){
            if(minLength == 1)
                return 1;

            if(sum >= target){
                minLength = right - left + 1;
                sum -= nums[left++];
            }
            else if(right == sz - 1)
                break;
            else if(right - left + 1 == minLength){
                sum -= nums[left++];
                sum += nums[++right];
            }
            else 
                sum += nums[++right];

        }

        // if(sum >= target){
        //         minLength = right - left;
        //     }

        if(minLength == sz + 1)
            return 0;
        return minLength;

    }
};
