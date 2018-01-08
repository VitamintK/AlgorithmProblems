#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
	if(n > 33){
		cout << m << endl;
	} else {
		cout << (m%(pow(2,n))) << endl;
	}
	return 0;
}