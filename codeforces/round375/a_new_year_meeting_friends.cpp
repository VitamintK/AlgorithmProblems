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
	int x, y, z;
	cin >> x >> y >> z;
	int ans = 300;
	for(int i = 0; i <=100; i++){
		ans = min(ans, abs(x - i) + abs(y - i) + abs(z - i));
	}
	cout << ans<< endl;
}