#include <bits/stdc++.h>
#include <string>
//UNFINISHED :(
#define ll long long
#define ull unsigned long long
using namespace std;
vector<pair<int, pair<int, int>>> mice;

double distance(int m1, int m2){
	int x1 = mice[m1+1].second.first;
	int x2 = mice[m2+1].second.first;
	int y1 = mice[m1+1].second.second;
	int y2 = mice[m2+1].second.second;
	return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

int main(){
	std::ios::sync_with_stdio(false);
	int n;
	cin >> n;
	int x, y, s;
	mice.push_back(make_pair(-1, make_pair(0, 0)));
	//t, x, y
	for(int i =0; i < n; i++){
		cin >> x >> y >> s;
		mice.push_back(make_pair(s, make_pair(x,y)));
	}
	double m;
	cin >> m;
	double eps = 1e-5;
	double r = 1234567890987;
	double l = 0;
	while(r - l > eps){
		cout << l << ' ' << r <<'\n';
		double mid = l + (r-l)/2; //mid is our starting velocity

		priority_queue<pair<int, pair<int, int> > > pq;
		pq = priority_queue<pair<int, pair<int, int> > >();
		//mouse id, (bitmask of eaten mice, time of arrival)
		pq.push(make_pair(0, make_pair(0, 0)));
		bool worked = false;
		set<pair<int, int>> explored;
		explored.clear();
		//mouse_id, bitmask of eaten mice
		cout << "outer loop" << endl;
		while(!pq.empty()){
			pair<int, pair<int, int>> ex = pq.top();
			int mouse_id = ex.first;
			int eaten = ex.second.first;
			int t = ex.second.second;
			pq.pop();
			cout << mouse_id << endl;
			if(t > mice[mouse_id+1].first || explored.count(make_pair(mouse_id, eaten)) > 0){
				continue;
			}

			explored.insert(make_pair(mouse_id, eaten));

			if(eaten == (1 << (n+1)) - 1 ){
				//cout << mouse_id << endl;
				worked = true;
				break;
			}
			//figure out how many mice have been eaten
			int num_eaten = __builtin_popcount(eaten);
			//cout << num_eaten << endl;
			for(int i = 0; i < n; i++){
				if(!(eaten & (1 << i))){
					//we haven't eaten mouse i yet
					if(explored.count(make_pair(i, (eaten | (1 << mouse_id)))) < 1){
						pq.push(make_pair(i, make_pair(eaten | (1 << mouse_id), t + distance(mouse_id, i)/(mid*pow(m, num_eaten)))));
					}
				}
			}
		}
		if(worked){
			r = mid;
		} else {
			l = mid;
		}
		cout << l << " " << r << endl;
	}
	cout << (r+l)/2 << endl;
	//__builtin_popcount();
	return 0;
}