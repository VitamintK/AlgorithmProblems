#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
//from halim
class SegmentTree{
private: vector<ll> st, A;
	ll n;
	ll left(ll p) {return p << 1;}
	ll right(ll p) {return (p<<1)+1;}
	void build(ll p, ll L, ll R){
		if(L == R){
			st[p] = L;
		} else {
			build(left(p), L, (L+R)/2);
			build(right(p), (L+R)/2+1, R);
			ll p1 = st[left(p)];
			ll p2 = st[right(p)];
			st[p] = (A[p1] <= A[p2]) ? p1 : p2;
		}
	}

	ll rmq(ll p, ll L, ll R, ll i, ll j){
		if(i > R || j < L) return -1;
		if(L >= i && R <= j){

			return st[p];
		}

		ll p1 = rmq(left(p), L, (L+R)/2, i, j);
		ll p2 = rmq(right(p), (L+R)/2+1, R, i, j);

		if(p1 == -1) return p2;
		if(p2 == -1) return p1;
		return (A[p1] <= A[p2]) ? p1: p2;
	}

public:
	SegmentTree(const vector<ll> &_A){
		A = _A;
		n = (ll)A.size();
		cout << n << endl;
		st.assign(4*n, 0);
		build(1, 0, n-1);
		for(int i = 0; i < 4*n; i++){
			cout << st[i] << " ";
		} cout << endl;
	}
	ll rmq(ll i, ll j){ return rmq(1,0,n-1,i,j);}
};

int main(){
	std::ios::sync_with_stdio(false);
	 int n, q;
	 cin >> n >> q;
	vector<ll> v(n);
	for(int i = 0; i < n; i++){
		cin >> v[i];
	}
	SegmentTree st(v);
	for(int j = 0; j < q; j++){
		ll V, l, r;
		cin >> V >> l >> r;
		cout << st.rmq(l, r) << endl;
		cout << V%(v[st.rmq(l-1,r-1)]) << endl;
	}
// 	ll arr[] = { 18, 17, 13, 19, 15, 11, 20 }; // the original array
// vector<ll> A(arr, arr + 7);
// SegmentTree st(A);
// printf("RMQ(1, 3) = %d\n", st.rmq(1, 3)); // answer = index 2
// printf("RMQ(4, 6) = %d\n", st.rmq(4, 6)); // answer = index 
	return 0;
}