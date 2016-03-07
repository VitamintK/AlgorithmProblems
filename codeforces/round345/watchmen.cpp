//goddamn this is naive
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>
using namespace std;
int main(){
	long n;
	scanf("%ld", &n);
	//vector<int> rows;
	//vector<int> cols;
	//rows.resize(1000000000);
	//cols.resize(1000000000);
	map<long, long> rows;
	map<long, long> cols;
	map<pair<long, long>, long> has;
	long x;
	long y;
	long long ans = 0;
	for(long i = 0; i<n; i++){
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