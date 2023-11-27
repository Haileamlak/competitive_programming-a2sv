class Solution {
public:
    string removeAdjacentDuplicates)string s){
        // string res = "";

        int len = s.length();
        int left = 0, right = 1;
        while(right < len){
            if(s[right] == s[left]){
                left--;
                right++;
            }
            else{
                s[left++] = s[right];
                right++;
            }
        }
        s[left + 1] = '\0';
        return s;
    }
};
