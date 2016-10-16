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
//LMAO THRE'S NO WAY THIS IS THIS EASY
using namespace std;
int main(){
	long long n;
	cin >> n;
	long long a;
	long long ans = 0;
	for(long long i = 0; i < n; i++){
		cin >> a;
		ans+=a;
	}
	ans-= a;
	long long A = (ans - (ans + a));
	long long B = (ans + a);
	cout << max(A, B) << endl;
}