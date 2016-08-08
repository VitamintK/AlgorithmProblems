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
#include <unordered_map>

using namespace std;

int main(){
	//http://web.mit.edu/sp.268/www/nim.pdf
	long long n;
	cin >> n;
	long long a;
	int ans = 0;
	for(long long i = 0; i < n; i++){
		cin >> a;
		ans ^= (a+1)%2;
		cout << 2-ans << endl;
	}
}