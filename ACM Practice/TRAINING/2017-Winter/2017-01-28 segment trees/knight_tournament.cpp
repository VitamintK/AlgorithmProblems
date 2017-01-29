#include <bits/stdc++.h>
#include <string>

#define ll long long
using namespace std;

vector<set<ll>> t(1000000);
vector<ll> ans(1000000);
void ins(ll index, ll l, ll r, ll pos){
	//we'll just use this to construct our initial segment tree.
	//index is the physical index into the segment tree array (t)	(physical index ~ segment tree array t)
	//l is the left bound of the segment that t[index] represents.  (an abstract idea ~ segment tree) (inclusive)
	//r is the right bound of the segment that t[index] represents. (an abstract idea ~ segment tree) (exclusive)
	//pos is the place we want to update. (an abstract idea ~ segment tree) (although it corresponds to t[n + pos])
	//-strike this ---val is the value that we want to update to.
	if(pos < l || pos > r) return;
	if(l == r){
		//t[index] = val;
		t[index] = set<ll>({pos});
	}
	ll mid = (l+r)/2;
	ins(index*2, 	l, mid, pos);
	ins(index*2 + 1,mid, r, pos);
	//do the segment tree operation
	t[index] = set<ll>();
	t[index].insert(t[index*2].begin(), t[index*2].end());
	t[index].insert(t[index*2 + 1].begin(), t[index*2 + 1].end()); 
}

void del(ll index, ll l, ll r, ll pos){
	//we'll use this to kill off knights
	//index is the physical index into the segment tree array (t)	(physical index ~ segment tree array t)
	//l is the left bound of the segment that t[index] represents.  (an abstract idea ~ segment tree) (inclusive)
	//r is the right bound of the segment that t[index] represents. (an abstract idea ~ segment tree) (exclusive)
	//pos is the place we want to update. (an abstract idea ~ segment tree) (although it corresponds to t[n + pos])
	//val is the value that we want to update to.
	if(pos < l || pos > r) return;
	if(l == r){
		//t[index] = val;
		t[index] = set<ll>();
	}
	ll mid = (l+r)/2;
	ins(index*2, 	l, mid, pos);
	ins(index*2 + 1,mid, r, pos);
	//do the segment tree operation
	t[index].erase(pos); 
}

set<ll>* query(ll p, ll l, ll r, ll i, ll j){
	if(i > r || j < l) return -1; //segment outside
	if(l >= i && r <= j) return t[p];
	set<ll>* p1 = query(p*2, l, (l+r)/2, i, j);
	set<ll>* p2 = query(p*2 + 1, (l+r)/2 + 1, r, i, j);
	if(p1 == -1) return p2;
	if(p2 == -1) return p1;
	set<ll> a;
	a.insert(p2.begin(), p2.end());
	a.insert(p1.begin(), p1.end());
	return a;
}

int main(){
	std::ios::sync_with_stdio(false);
	
	ll n, m;
	cin >> n >> m;
	for(ll i = 0; i < n; i++){
		ins(1, 1, n, i);
	}
	for(ll i = 0; i < m; i++){
		ll l, r, x;
		cin >> l >> r >> x;
		for(auto k : query(1, 1, n-1, l, r)){
			
		}
	}
	return 0;
}