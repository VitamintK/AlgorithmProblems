#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

// int wcd(pair<int,int> A, pair<int, int> B){

// }

// (6,10) (9,10) (15,2), (3,2)

// 3 10 || 3 2
// 3 10
// 5 2
// - 2




int main(){
	std::ios::sync_with_stdio(false);
	//vector<int> primes;
	int n;
	cin >> n;
	//int sl = 123456;
	//vector<int> sieve(sl);
	vector<int> as(n);
	vector<int> bs(n);

	for(int i = 0; i < n; i++){
		cin >> as[i] >> bs[i];
	}

	//for(int i = 2; i < sl; i++){
	//	if(sieve[i] == 0){
	//		primes.push_back(i);
	//		for(int j = i; j < sl; j+=i){
	//			sieve[j] = i;
	//		}
	//	}
	//}

	vector<int> primes;
	int c = as[0];
	for(int i = 2; i < 1+sqrt(c); i++){
		while(c%i == 0){
			primes.push_back(i);
			c/=i;
		}
	}
	if(c != 1){
		primes.push_back(c);
	}

	c = bs[0];
	for(int i = 2; i < 1+sqrt(c); i++){
		while(c%i == 0){
			primes.push_back(i);
			c/=i;
		}
	}
	if(c != 1){
		primes.push_back(c);
	}



	for(int i = 0; i < primes.size(); i++){
		bool flag = true;
		for(int j = 0; j < n; j++){
			if((as[j]%primes[i] != 0) && (bs[j]%primes[i] != 0)){
				flag = false;
				break;
			}
		}
		if(flag == true){
			cout << primes[i] << endl;
			return 0;
		}
	}
	cout << -1 << endl;
	
	return 0;
}