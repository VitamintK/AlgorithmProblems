#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;


int main(){
	long long n, m;
	long long toy;
	cin >> n >> m;
	long long toyi = 1;
	long long cost = 0;
	vector<long long> v;
	vector<long long> toys;
	for(long i = 0; i < n; i++){
		cin >> toy;
	    toys.push_back(toy);	
	}
	sort(toys.begin(), toys.end());
	for(long i = 0; i < n; i++){
		toy = toys[i];
		while(cost+toyi <= m && toyi < toy){
			v.push_back(toyi);
			cost+=toyi;
			toyi++;
		}
		toyi = max(toyi+1, toy+1);
	}
	//cout << toyi << endl;
	while(cost+toyi <= m && toyi < 1000000001){
			v.push_back(toyi);
			cost+=toyi;
			toyi++;
		}
	cout << v.size() << endl;
	for(long long i = 0; i < v.size(); i++){ //size is unsigned int, not long long?
	    cout << v[i] << " ";
	}
	return 0;
}