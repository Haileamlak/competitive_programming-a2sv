//Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int len = nums.size();
        for (int i = 0; i < len; i++)
        {
            if(nums[i] != i)
                return i;
        } 
        return len;  
    }
};
