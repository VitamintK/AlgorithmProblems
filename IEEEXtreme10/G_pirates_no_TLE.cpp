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
#define ll long long
using namespace std;


/*4 12 2
OOOOO~~OOOOO
O~~OO~OO~~~O
OO~OO~~O~O~O
OOOOOO~OOOOO
2 2 3 11
4 7 3 9*/
int main(){
	ll n, m, q;
	cin >> n >> m >> q;
	ll yar[1001][1001];
	char a;
	//read in the map into yar
	for(ll row = 0; row < n; row++){
		for(ll col = 0; col < m; col++){
			//cin >> yar[row][col];
			cin >> a;
			if(a == 'O'){
				yar[row][col] = 1; //land are positive.
			} else {
				yar[row][col] = -1; //sea are negative.
			}
		}
	}
	//color each connected component in the map (positive number for lands, and negative numbers for seas)
	//starting at 2 and -2 respectively.  Using dfs for each yet uncolored cell in the map.
	ll lands = 1;
	ll seas = -1;
	for(ll row = 0; row < n; row++){
		for(ll col = 0; col < m; col++){
			if(yar[row][col] != 1 && yar[row][col] != -1){
				continue;
			}
			ll mycolor = yar[row][col];
			ll colorcolor;
			if(mycolor == 1){
				colorcolor = ++lands;
			} else {
				colorcolor = --seas;
			}
			vector<pair<ll, ll> > stak;
			stak.push_back(make_pair(row, col));
			while(!stak.empty()){
				pair<ll, ll> dw = stak.back();
				ll row = dw.first;
				ll col = dw.second;
				stak.pop_back();
				for(ll row_off = -1; row_off <= 1; row_off++){
					for(ll col_off = -1; col_off <= 1; col_off++){
						if(row + row_off >= 0 && row+row_off < n && col + col_off >= 0 && col + col_off < m){
	                            if(mycolor == yar[row+row_off][col+col_off]){
	                            	yar[row+row_off][col+col_off] = colorcolor;
	                                stak.push_back(make_pair(row+row_off, col+col_off));
	                            }
						}
					}
				}
			}
		}
	}
	 // for(ll i = 0; i < n; i++){
	 // 	for(ll j = 0; j < m; j++){
	 // 		cout << yar[i][j] << " ";
	 // 	} cout << endl;
	 // }

	//make a graph "edges" from the colored grid "yar"
	map<ll, vector<ll> > edges;
	for(ll row = 0; row < n; row++){
		for(ll col = 0; col < m; col++){
			for(ll row_off = -1; row_off <= 1; row_off++){
					for(ll col_off = -1; col_off <= 1; col_off++){
						if(row + row_off >= 0 && row+row_off < n && col + col_off >= 0 && col + col_off < m){
                            if(yar[row][col] != yar[row+row_off][col+col_off]){
                            	edges[yar[row][col]].push_back(yar[row+row_off][col+col_off]);
                            	edges[yar[row+row_off][col+col_off]].push_back(yar[row][col]);
                            }
						}
					}
				}
		}
	}
	//root the graph at the first sea -2 to turn it into a tree "parent" and "children".
	//also store depth of each node in "depths".
	vector<pair<ll, ll> > stk;
	stk.push_back(make_pair(-2, 0));
	map<ll, vector<ll> > children;
	map<ll, ll> parent;
	map<ll, ll> depths;
	parent[-2] = -1;
	while(!stk.empty()){
		pair<ll, ll> x = stk.back();
		ll ex = x.first;
		depths[ex] = x.second;
		//cout << x.first <<" " <<  x.second << endl;
		stk.pop_back();
		for(ll i = 0; i < edges[ex].size(); i++){
			if(parent[edges[ex][i]] == 0){
				parent[edges[ex][i]] = ex;
				//cout << "parent of " << edges[ex][i] << " is " << ex << endl;
				children[ex].push_back(edges[ex][i]);
				stk.push_back(make_pair(edges[ex][i], x.second+1));
			}
		}
	}
	//run a shitty but simple LCA (lowest common ancestor) algorithm and the answer is given by
	//ans = depth(start) + depth(end) - 2*depth(LCA(start, end))
	//but each crossing will be counted twice, so we divide by two.
	ll row1, col1, row2, col2;
	for(ll i = 0; i < q; i++){
		cin >> row1 >> col1 >> row2 >> col2;
		set<ll> path;
		ll s = yar[row1-1][col1-1];
		ll e = yar[row2-1][col2-1];
		ll ans = depths[s] + depths[e];
		while(s != -1){
			//cout << s << " " << parent[s] <<  endl;
			path.insert(s);
			s = parent[s];
		}

		while(path.count(e) < 1){
			//cout << "stuck here" << endl;
			e = parent[e];
		}
		//cout <<"im free!" << endl;
		ans -= 2*depths[e];
		cout << ans/2 << endl;
	}

}