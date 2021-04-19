// doesn't work.  I had the right idea in my head but fucked up implementing it.  the maps are sorted by the value of the number, not by how often
// they appear.  Still need the recursive tree that calculates the strict majority of all power-of-two ranges.
#include <iostream> 
#include <string> 
#include <set> 
#include <map> 
#include <stack> 
#include <queue> 
#include <vector> 
#include <utility> 
#include <iomanip> 
#include <sstream> 
#include <bitset> 
#include <cstdlib> 
#include <iterator> 
#include <algorithm> 
#include <cmath>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<vector<map<int, int> > > tiers;


void get(vector<map<int, int>*> &ans, int l, int r){
    if (l > r){
        return;
    }
    int level = 0;
    int span = 1;
    int n = l;
    while(n%2 == 0 && r+1-l >= span*2){
        level++;
        span *= 2;
        n/=2;
    }
    ans.push_back(&tiers[level][n]);
    get(ans, l+span, r);
}


int main(){
	std::ios::sync_with_stdio(false);
	int n, q;
	cin >> n >> q;
    vector<int> as(n);
    vector<map<int, int> > maps(n);
    for(int i = 0; i < n; i++){
        cin >> as[i];
        maps[i][as[i]]++;
    }
    tiers.push_back(maps);
    while(tiers[tiers.size() - 1].size() > 1){
        auto tier = tiers[tiers.size()-1];
        vector<map<int, int> > new_tier;
        for(int i = 0; i < tier.size()/2; i++) {
            map<int, int> new_map;
            for (auto it = tier[i*2].begin(); it != tier[i*2].end(); it++){
                new_map[it->first] += it->second;
            }
            for (auto it = tier[i*2+1].begin(); it != tier[i*2+1].end(); it++){
                new_map[it->first] += it->second;
            }
            new_tier.push_back(new_map);
        }
        tiers.push_back(new_tier);
    }
    for(int i = 0; i < q; i++){
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        vector<map<int, int>*> maps;
        get(maps, l, r);
        int maj = -1;
        for(int j = 0; j < maps.size(); j++){
            auto m = maps[j];
            int b = m->rbegin()->first;
            
            int count = 0;
            for(int k = 0; k < maps.size(); k++){
                count += (*maps[k])[b];
            }
            if (count > (r-l+1+1)/2) {
                int tot = r-l+1;
                int nt = r-l+1-count;
                maj = 1;
                cout << count - nt << endl;
                break;
            }
        }
        if (maj == -1) {
            cout << 1 << endl;
        }
    }
	return 0;
}