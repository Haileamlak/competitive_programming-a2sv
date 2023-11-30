class Solution {
public:
    bool isPalindrome(int x) {
        string strX = to_string(x);
        for(int start=0,end = strX.length()-1;end>start;start++,end--)
            if(strX[start]!=strX[end])
                return false;
        return true;
    }
};