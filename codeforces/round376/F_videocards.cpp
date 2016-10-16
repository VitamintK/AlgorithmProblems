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
	long long n;
	long long as[200001];
	cin >> n;
	long long maxim = 0;
	for(long long i = 0; i < n; i++){
		cin >> as[i];
		maxim = max(maxim, as[i]);
	}
	for(long long i = 0; i < n; i++){
		if(as[i] == maxim){
			as[i] = 0;
			break;
		}
	}
	vector<long long> factors;
	for(long long i = 0; i < maxim; i++){
		if()
	}
}