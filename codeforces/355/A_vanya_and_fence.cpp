#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
using namespace std;


int main(){
	int n, h;
	cin >> n >> h;
	int a;
	int ans = 0;
	for(int i = 0; i < n; i++){
		cin >> a;
		ans+= (a>h)?2: 1;
	}
	cout << ans;
}