#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>

#define ll long long
#define ull unsigned long long
using namespace std;

// DOESN'T WORK: MEMORY LIMIT BECAUSE IT CAN CREATE
// N^2 = 3000*3000 INTERVALS

struct event {
            int pos;
            int start;
            int end;
            int typ;
        };

bool compare(const event &a, const event &b) {
    if (a.pos == b.pos) {
        if (b.typ) {
            return false;
        }
        if (a.typ) {
            return true;
        }
        return a.end > b.end;
    }
    return a.pos < b.pos;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >>T;
    for(int t = 0; t < T; t++){
        int n;
        cin >> n;
        vector<int> as(n);
        for(int i = 0; i < n; i++){
            cin >> as[i];
        }
        // vector<pair<int, int> > intervals;
        
        vector<event> events;
        events.clear();
        for (int i = 0; i < n ;i++){
            for (int j = i+1; j < n; j++){
                if (as[i] == as[j]) {
                    // intervals.push_back(make_pair(i, j));
                    events.push_back((event){i, i, j, 0});
                    events.push_back((event){j,i,j,1});
                }
            }
        }
        sort(events.begin(), events.end(), compare);
        set<pair<int, int>> sweep; // end, then beginning
        int ans = 0;
        for (event e: events) {
            if (e.typ) {
                sweep.erase(make_pair(e.end, e.start));
            } else {
                auto d = sweep.lower_bound(make_pair(e.end, 0));
                int dist = distance(sweep.begin(), d);
                ans += dist;
                // cout << e.start << " " << e.end << " " << dist << endl;
                sweep.insert(make_pair(e.end, e.start));
            }
        }
        cout << ans << endl;
    }
	return 0;
}