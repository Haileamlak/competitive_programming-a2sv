

int max_sum(vector<int> nums, int k){
    
    int maxSum = -1;
    for(int i = 0;i < nums.size();i++){
    
        for(int j = i+1;j < nums.size();j++){
            if(nums[i] + nums[j] < k)
                maxSum = max(maxSum, nums[i] + nums[j]);
        }
    }
    
    return maxSum;
}
// def max_sum(nums, k):
//     maxSum = -1;
//     for i in range(len(nums)):
//         for j in range(len(nums)):
//             if nums[i] + nums[k] < k:
//                 maxSum = max(maxSum, nums[i] + nums[j])
                
//     return maxSum




// S(n) = O(log n)
// T(n = O(nlogn)
int maxSumOptimized(vector<int>nums, int k){
    int num_size = nums.size();//O(1)
    sort(nums.begin(), nums.end()) // T(n) = O(nlogn)
    
    int maxSum = -1;
    for(int left = 0, right = num_size - 1;left < right;){// O(N)
     
        if(nums[left] + nums[right] >= k)
            right--;
        else{
            maxSum = max(maxSum, nums[left] + nums[right])
            left++;
        }                                            
    }
    return maxSum;
}
         
// S(n) = O(n) and T(n) = O(nlogn)
// def maxSumOptimized(nums, k):
//     nums.sort();
//     maxSum = -1
//     left = 0
//     right = len(nums) - 1
//     while(left < right):
//         if (nums[left] + nums[right] >= k):
//             right -= 1
//         else: 
//             maxSum = max(maxSum, nums[left] + nums[right])
//             left += 1
        
//     return maxSum
    

