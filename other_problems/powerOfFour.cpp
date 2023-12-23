class Solution {
public:
    bool isPowerOfFour(int n) {
        if(pow(-2,31)>n||n>pow(2,31)-1)
        exit(1);
        if(n<=0)
        return false;
        return (log(n)/log(4))==round(log(n)/log(4));
    }
};
