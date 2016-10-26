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
	ll p;
	cin >> p;
	ll id;
	ll n;
	for(ll i = 0; i < p; i++){
		cin >> id >> n;
		cout << id << " " << n*(n+1)/2 << " " << (2*n)*(n+1)/2 - n<< " " << (2*n)*(n + 1)/2 << endl;
	}
}