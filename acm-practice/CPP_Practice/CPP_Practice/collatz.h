#include<iostream>
int collatz(int x){
	std::cout << x << std::endl;
	if (x == 1){
		return 0;
	}
	if (x % 2 == 0){
		return collatz(x / 2) + 1;
	}
	else {
		return collatz(3 * x + 1) + 1;
	}
}
void collatz_start(){
	int x;
	std::cin >> x;
	std::cout << collatz(x);
}
