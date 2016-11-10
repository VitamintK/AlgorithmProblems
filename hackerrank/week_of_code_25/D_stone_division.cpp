#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <utility>
#define ll long long
using namespace std;

map<ll, ll> nimbers;
vector<ll> Ss;


ll get_nimber(ll stones){
	//memoize or die
	if(nimbers.count(stones) > 0){
		return nimbers[stones];
	}
	//in the sprague-grundy graph thing:
	//if mexcands[i] = 1, then there is some descendant with SG(descendant) = i
	ll mexcands[10] = {0};
	for(int i = 0; i < Ss.size(); i++){
		if(stones%Ss[i] == 0){
			//if we can split the stones evenly into Ss[i] parts
			if(Ss[i]%2 == 0){
				//if, after splitting, we'll have an even number of piles
				//SG(descendant) = SG(pilesize) XOR SG(pilesize) XOR ... an even number of times = 0
				mexcands[0] = 1;
			} else {
				//if, after splitting, there'll be an odd number of piles,
				//SG(descendant) = SG(pilesize) XOR SG(pilesize) XOR ... an odd number of times = SG(pilesize)
				mexcands[get_nimber(stones/Ss[i])] = 1;
			}
		}
	}
	//return mex of descendant values;
	for(ll i = 0; i < 10; i++){
		if(mexcands[i] == 0){
			return i;
		}
	}
	return 10;
}

int main(){
	ll n, m;
	cin >> n >> m;
	Ss.resize(m);
	for(ll i = 0; i < m; i++){
		cin >> Ss[i];
	}
	sort(Ss.begin(), Ss.end());
	cout << ((get_nimber(n)==0)?"Second":"First") << endl;
}