#include <iostream>
#include <vector>
using namespace std;
int main(){
	int n;
	
	cin >> n;
	int o;
	int currenta = 0;
	int currentb = 0;
	for(int i = 0; i < n; i++){
		cin >> o;
		currenta |= o;
	}
	for(int i = 0; i < n; i++){
		cin >> o;
		currentb |= o;
	}



	cout << currenta+currentb;

	return 0;
}