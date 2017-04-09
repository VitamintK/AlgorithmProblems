//Problem is from http://codeforces.com/problemset/problem/538/b

#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>

int main(){
	int a;
	int length_of_a;
	int max_digit = 0;
	std::cin >> a;
	length_of_a = floor(log10((double)a)) + 1;
	float* digits = new float[length_of_a];
	int digit;
	for (int i = 0; i < length_of_a; i++){
		digit = (a % int(std::pow((double)10, (i + 1))))/std::pow((double)10, i);
		//std::cout << "digit is " << digit << std::endl;
		digits[i] = digit;
		a = a - digit;
		max_digit = std::max(max_digit, digit);
	}

	std::cout << max_digit << std::endl;
	for (int i = 0; i < max_digit; i++){
		std::string addend = "";
		bool non_zero_encountered = false;
		for (int j = length_of_a-1; j >= 0; j--){
			if (digits[j] == 0){
				if (non_zero_encountered){
					addend = addend + "0" ;
				}
			}
			else {
				non_zero_encountered = true;
				addend = addend + "1";
				digits[j] = digits[j] - 1;
			}
		}
		std::cout << addend << " ";
	}

	std::cin >> a;
	return 0;
}