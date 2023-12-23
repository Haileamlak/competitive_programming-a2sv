class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        for (size_t i = 0; i < nums.size(); i++)
        {
            int lsum = 0, rsum = 0;
            for (size_t j = 0; j < i; j++)
            {
                lsum += nums[j];
            }
            for (size_t j = i+1; j < nums.size(); j++)
            {
                rsum += nums[j];
            }
            if(lsum == rsum)
                return i;
        }
        return -1;
    }
};
