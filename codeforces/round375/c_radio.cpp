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

using namespace std;


int main(){
	long long n, m;
	cin >> n >> m;
	long long band;
	long long plist[10000];
	long long plays = n/m;
	map<int, int> played;
	for(long long i = 0; i < n; i++){
		cin >> band;
		plist[i] = band;
		played[band]++;
	}

}