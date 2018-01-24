#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	cout << sqrt(-16) << endl;
	cout << (double)(sqrt(-16)) << endl;
	cout << (int)(sqrt(-16)) << endl;
	ll n = 677329;
	if((double)(sqrt(n)) == (int)(sqrt(n))){
		cout << "it is equal" << endl;
	}
	return 0;
}