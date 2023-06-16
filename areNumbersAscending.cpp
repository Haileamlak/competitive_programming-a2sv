class Solution {
public:
    bool areNumbersAscending(string s) {
       stringstream strS (s);
       int num1 = 0;string iterate;
       while(strS>>iterate){
        if( iterate[0]<='9'){
            if(stoi(iterate) <= num1)
                return false;
            num1 = stoi(iterate);
        }
       }
       return true;
    }
};
