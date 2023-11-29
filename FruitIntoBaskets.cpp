class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int sz = fruits.size();
        int maxFruit = 0;
        int fruit1 = fruits[0], fruit1index = 0;
        int fruit2 = -1, fruit2index = -1;

        int i = 1;
        for(;i < sz;i++){
            if(fruits[i] != fruits[i - 1]){
                fruit2 = fruits[i];
                fruit2index = i;
                break;
            }
            else
                fruit1index++;
        }

        int length = i;
        if(length >= sz)
            return length;
        
        for(;i < sz;i++){
            if(fruits[i] == fruit1){
                fruit1index = i;
            }
            else if(fruits[i] == fruit2){
                fruit2index = i;
            }
            else if(fruits[i - 1] == fruit1){
                maxFruit = max(maxFruit, length);
                length = fruit1index - fruit2index;
                fruit2 = fruits[i];
                fruit2index = i;
            }
            else /*if(fruits[i - 1] == fruit2)*/{
                maxFruit = max(length, maxFruit);
                length = fruit2index - fruit1index;
                fruit1 = fruits[i];
                fruit1index = i;
            }
            
            length++;
        }
        maxFruit = max(length, maxFruit);
        return maxFruit;
    }
};
