class Solution {
public:
    int fib(int n) {
        if(0>n||n>30)
        exit(2);
        if(n==0||n==1)
        return n;
        return fib(n-1)+fib(n-2);
    }
};
