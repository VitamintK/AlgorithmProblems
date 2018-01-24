#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	int k;
	cin >> n >> k;
	//cout << k << endl;
	map<int, int> esketit;
	ll i = 0;

	// while((1<<i) <= n && i < 66){
	// 	if((1<<i) & n){
	// 		esketit[i] = 1;
	// 		cout << i << endl;
	// 	}
	// 	i++;
	// }
	while(n){
		if(n%2 == 1){
			esketit[i] = 1;
		}
		n/=2;
		i++;
	}
	if(k < esketit.size()){
		//cout << k << " " << esketit.size() << endl;
		cout << "No" << endl;
		return 0;
	}
	int count = esketit.size();
	for(int i = 66; i > -66 && count < k; i--){
		//cout << i << " " << esketit[i] << endl;
		if(esketit[i] <= k-count){
			split = esketit[i];
		//int split = min(esketit[i], k-count);
			esketit[i] -= split;
			esketit[i-1]+= split*2;
			count += split;
		}
	}
	

	cout << "Yes" << endl;
	for(int i = 66; i > -66; i--){
		for(int j = 0; j < esketit[i]; j++){
			cout << i << " ";
		}
	}
	cout << endl;
	return 0;
}