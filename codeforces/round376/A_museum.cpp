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
	string n;
	cin >> n;
	int rotations = 0;
	char letter = 'a';
	char thisl;
	for(int i = 0; i < n.length(); i++){
		thisl = n[i];
		int r = abs((thisl - 'a') - (letter - 'a'));
		rotations += min(r, 26 - r);
		letter = n[i];
	}
	cout << rotations << endl;
}