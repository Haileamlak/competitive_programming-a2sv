class Solution {
public:
    //total water is trapped into the bars
    int trap(vector<int>& height) {
        int l = 0,r = height.size() - 1;
        int lmax = INT_MIN, rmax = INT_MIN,
        water = 0;
        while(l<r){
            lmax = max(lmax, height[l]);
            rmax = max(rmax, height[r]);
            water += (lmax < rmax)? lmax - height[l++] : rmax - height[r--];
        }
        return water ; 
    }
};
