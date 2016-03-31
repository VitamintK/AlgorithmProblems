#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

struct {
        bool operator()(pair<string, int> i, pair<string, int> j){
	return (i.second > j.second);
}
} gt;

int main(){
	long n, m;
	cin >> n >> m;
	vector<int> v(m);
	vector<int> participants(m);
	vector<vector<pair<string, int> > > scores(m+1);
	string s;
	long region;
	int score;
	//cout << "here" << endl;
	for(long i = 0; i < n; i++){
		cin >> s >> region >> score;
		scores[region].push_back(make_pair(s, score));
		//cout << "Here" << endl;
	}
	//cout << "here" << endl;
	for(long i = 1; i < m+1; i++){
		sort(scores[i].begin(), scores[i].end(), gt);
	}
	//cout << scores[1][0].first << endl << scores[1][1].first << endl << scores[1][2].first << endl;
	for(long i = 1; i < m+1; i++){
		if(scores[i].size() > 2 && scores[i][2].second == scores[i][1].second){
			cout << "?" << endl;
		} else {
			cout << scores[i][0].first << " " << scores[i][1].first << endl;
		}
	}

	return 0;
}