#include<iostream>

using namespace std;

int main(){
	
	return 0;
}

bool areSuccessiveNumbersConsecutive(stack<int> nums){
	bool evenConsecutive = true;
	bool oddConsecutive = true;
	
	int num1, num2;
	while(!nums.empty()){
		num1 = nums.top();
		nums.pop();
		if(!nums.empty())
			num2 = nums.top();
		else
			break;

		if(max(num1, num2) - min(num1, num2) != 1)
			evenConsecutive = false;
		
		
		
		
	}
}