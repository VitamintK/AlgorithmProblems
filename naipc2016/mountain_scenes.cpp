#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

long long fact(long long f){
	if(f == 0){
		return 1;
	} else {
		return fact(f-1) * f;
	}
}

long long comb(long long n, long long k){
	if(k > n){
		return 0;
	}
	if(k *2 > n){
		k = n - k;
	}
	if(k == 0){
		return 1;
	}
	long long result = n;
	for(long long i = 2; i <=k; ++i){
		result *= (n -i + 1);
		result /= i;
	}
	return result;
}

int main(){
	cout << comb(190, 30) << endl;
	long long n, w, h;
	cin >> n >> w >> h;
	long long ans = 0;
	for(long i = 0; i <= n; i++){
		ans+= (comb(i + w -1, w-1)) - 1;
		if(i/w == 0){
			ans --;
		}
	}
	cout << ans;


	return 0;
}