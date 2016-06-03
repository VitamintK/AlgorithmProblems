#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

char conv[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_'};

int c_to_i(char c){
	return distance(conv, find(conv, conv+63, c));
}

long long popcount(int p){
	long long cnt = 1;
	for(int i = 0; i < 6; i++){
		if((p&1)==0){
			cnt*=3;
		}
		p = (p >> 1);
	}
	return cnt;
}

int main(){
	string k;
	cin >> k;
	long long ans = 1;
	for(char x : k){
		ans *=popcount(c_to_i(x));
		ans%=1000000007;
	}
	ans+= 1000000007;
	cout << ans%1000000007;
	return 0;
}