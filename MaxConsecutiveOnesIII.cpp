class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int left = 0, right = 0;
        int maxLength = 0;
        int length = 0;

        for(;right < nums.size();right++){
            if(nums[right])
                length++;
            
            if((right - left + 1) - length > k){
                if(nums[left++])
                    length--;
            }
            else{
                maxLength = max(maxLength, (right - left + 1));
            }
        }
        
        return maxLength;
    }
};
