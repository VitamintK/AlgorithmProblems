#include <bits/stdc++.h>

#define REP(i,a,b) for(int i = (a); i < b; i++)
typedef long long ll;
using namespace std;
int main(){
	int N, C, P;
	stack<int> stk;
	int cur = 1;
	cin >> N >> C >> P;
	
	map<int, int> m;
	m[1]++;
	
	REP(i, 0, C){
		int command;
		cin >> command;
		cur += command;
		
		if (cur > N) cur %= N;
		
		else if (cur == 0) cur = N;
		m[cur]++;
	}
	
	cout << m[P] << '\n';
}
