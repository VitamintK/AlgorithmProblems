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

int main(){
	std::ios::sync_with_stdio(false);
	ll n, k;
	cin >> n >> k;
	ll ex = n;
	for(ll i = pow(2,n); i > 0; i/=2){
		if(k%i == 0){
			cout << ex+1 << endl;
			return 0;
		}
		ex--;
	}
	return 0;
}