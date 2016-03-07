//goddamn this is naive
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>
using namespace std;
int main(){
	int n;
	scanf("%d", &n);
	//vector<int> rows;
	//vector<int> cols;
	//rows.resize(1000000000);
	//cols.resize(1000000000);
	map<long, int> rows;
	map<long, int> cols;
	map<pair<long, long>, int> has;
	long x;
	long y;
	int ans = 0;
	for(int i = 0; i<n; i++){
		scanf("%ld %ld", &x, &y);
		ans+=cols[x];
		ans+=rows[y];
		if(has.count(pair<long, long>(x,y)) > 0){
		    ans-=has[pair<long, long>(x,y)];
		}
		has[make_pair(x,y)]++;
		rows[y]++;
		cols[x]++;
	}
	//cout << has[make_pair(1,1)] << endl;
	cout << ans;
	return 0;
}