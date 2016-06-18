#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <map>
#include <set>
using namespace std;

int main(){
	long long n, m;
	cin >> n >> m;
	long long ans = 0;
	for(int i = 0; i < 5; i++){
	   ans+=((n/5)+(n%5 >= i) - (i == 0))*((m/5) + (m%5 >= (5-i)) - (1 == 0));
	}
	cout << ans;
	return 0;
}
