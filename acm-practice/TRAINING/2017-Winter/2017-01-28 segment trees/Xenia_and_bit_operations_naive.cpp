#include <bits/stdc++.h>
#include <string>

#define ll long long
using namespace std;

vector<ll> t(1<<20);

void build(ll root, ll n, ll depth){
	if(root >= n){
		return;
	}
	build(root*2, n, depth-1);
	build(root*2+1, n, depth-1);
	if(depth%2 == 0){
		t[root] = t[root*2] | t[root*2 + 1];
	} else {
		t[root] = t[root*2] ^ t[root*2 + 1];
	}
}

void update(ll index, ll depth){
	if(depth%2 == 0){
		t[index] = t[index*2] | t[index*2 + 1];
	} else {
		t[index] = t[index*2] ^ t[index*2 + 1];
	}
	if(index != 1){
		update(index/2, depth+1);
	}
}

int main(){
	std::ios::sync_with_stdio(false);
	//making a segment tree from scratch for the first time
	ll n, m;
	cin >> n >> m;
	for(ll i = 0; i < pow(2,n); i++){
		cin >> t[pow(2,n)+i];
	}
	build(1, pow(2,n), n - 1);
	//for(ll i = 0; i < pow(2,n+1); i++){
	//	cout << t[i] << " ";
	//} cout << endl;
	for(ll i = 0; i < m; i++){
		ll a, b;
		cin >> a >> b;
		t[pow(2,n) + a - 1] = b;
		update((pow(2,n) + a - 1)/2, 0);
		cout << t[1] << endl;
		//for(ll i = 0; i < pow(2,n+1); i++){
		//	cout << t[i] << " ";
		//} cout << endl;
	}
	return 0;
}