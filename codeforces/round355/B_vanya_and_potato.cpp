#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
using namespace std;

//why is this problem so hard for me?????
int main(){
	long long n, h, k;
	cin >> n >> h >> k;
	long long a;
	long long h_buff =0;
	long long ans = 0;
	for(int i = 0; i < n; i++){
		cin >> a;
		if(h_buff+a > h){
			ans+=h_buff/k;
			h_buff = h_buff%k;
		}
		if(h_buff + a > h){
			ans++;
			h_buff = 0;
		}
		h_buff+=a;
		//ans%=100000
	}
	ans+= (h_buff + k - 1)/k;
	cout << ans;
	return 0;
}