class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int sz = nums.size();
        int minimal =  sz + 1;
        int sum = 0;

        int i = 0, j = 0;
        while(j <= sz ){
            if(sum >= target){
                minimal = min(minimal, j - i);
                sum -= nums[i++];
            }
            else{
                if(j == sz)
                    j++;
                else
                    sum += nums[j++];
            }
        }

        return (minimal == sz + 1? 0 : minimal);
    }
};
