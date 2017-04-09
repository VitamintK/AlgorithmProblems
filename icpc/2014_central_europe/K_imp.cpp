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

typedef pair<int, int> pii;
class Compare{
public:
	bool operator() (const pii &a, const pii &b){
		if (a.second == b.second)
			return a.first < b.first;
		return a.second < b.second;
	}
};

int a,b;
int main(){
	int T, N, K;
	cin >> T;
	for (int t = 0; t < T; t++){
		pair<int, int> data[150001];
		cin >> N >> K;
		for (int n = 0; n < N; n++){
			cin >> a >> b;
			data[n] = make_pair(a-b,b);
		}

		if (K >= N){
			cout << "0\n";
			continue;
		}

		stable_sort(data, data+N, Compare());
		for (int i = 0; i < N; i ++){
			cout << data[i].first << ' ' << data[i].second << '\n';
		}

		int total_cost = data[N-1].first;

		for (int i = N-K-1; i < N-1;i++){
			total_cost -= data[i].second;
		}
		cout << total_cost << '\n';
	}
	return 0;
}