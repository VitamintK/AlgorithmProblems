#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
using namespace std;


int main(){
	int n, a, b;
	cin >> n >> a >> b;
	cout << (n-1 + a-1)%b + 1;
	return 0;
}