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
int m;
//shoulda been minimax problem but this is incomplete.
vector<vector<pair<char, pair<int, int> > > > all_state(vector<pair<char, pair<int, int> > >fp, 
	vector<pair<char, pair<int, int> > >sp){
	vector<vector<pair<char, pair<int, int> > > > all_states;
	for(int i = 0; i < fp.size(); i++){
		if(fp[i].first == 'Q'){
			for(int off = -3; off <= 3; off++){
				vector<pair<char, pair<int, int> > > = fp;
				if(fp[i].second.first + off >= 0 && fp[i].second.first + off < 4 && fp[i].second.second + off >= 0
					&& fp[i].second.first + off < 4){
					fp[i].second.first = fp[i].second.first + off;
					fp[i].second.second = fp[i].second.second+ off;
					all_states.push_back(fp);
				}
			}
			for(int off = -3, off <= 3; off++){
				vector<pair<char, pair<int, int> > > = fp;
				if(fp[i].second.first - off >= 0 && fp[i].second.first - off < 4 && fp[i].second.second + off >= 0
					&& fp[i].second.first + off < 4){
					fp[i].second.first = fp[i].second.first - off;
					fp[i].second.second = fp[i].second.second+ off;
					all_states.push_back(fp);
				}
			}
			for(int col = 0; col < 4; col++){
				vector<pair<char, pair<int, int> > > = fp;
					fp[i].second.second = col;
					all_states.push_back(fp);
				
			}
			for(int row = 0; row < 4; row++){
				vector<pair<char, pair<int, int> > > = fp;
					fp[i].second.first = row;
					all_states.push_back(fp);
				
			}
		} else if(fp[i].first == 'N'){
			pair<int, int> moves[8] = {make_pair(-2, 1),make_pair(-2, -1),make_pair(-1, 2),make_pair(-1, -2),
				make_pair(2, 1),make_pair(2, -1),make_pair(1, 2),make_pair(1, -2)};
			for(int j = 0; j < 8; j++){
				vector<pair<char, pair<int, int> > > = fp;
				int newrow = fp[i].second.first + moves[j].first;
				int newcol = fp[i].second.second + moves[j].second;
				if(newrow >= 0 && newrow < 4 && newcol >= 0 && newcol < 4){
					fp[i].second.first = newrow;
					fp[i].second.second = newcol;
					all_states.push_back(fp);
				}
			}
		} else if(fp[i].first == 'B'){
			for(int off = -3; off <= 3; off++){
				vector<pair<char, pair<int, int> > > = fp;
				if(fp[i].second.first + off >= 0 && fp[i].second.first + off < 4 && fp[i].second.second + off >= 0
					&& fp[i].second.first + off < 4){
					fp[i].second.first = fp[i].second.first + off;
					fp[i].second.second = fp[i].second.second+ off;
					all_states.push_back(fp);
				}
			}
			for(int off = -3, off <= 3; off++){
				vector<pair<char, pair<int, int> > > = fp;
				if(fp[i].second.first - off >= 0 && fp[i].second.first - off < 4 && fp[i].second.second + off >= 0
					&& fp[i].second.first + off < 4){
					fp[i].second.first = fp[i].second.first - off;
					fp[i].second.second = fp[i].second.second+ off;
					all_states.push_back(fp);
				}
			}
		} else if(fp[i].first == 'R'){
			for(int col = 0; col < 4; col++){
				vector<pair<char, pair<int, int> > > = fp;
					fp[i].second.second = col;
					all_states.push_back(fp);
				
			}
			for(int row = 0; row < 4; row++){
				vector<pair<char, pair<int, int> > > = fp;
					fp[i].second.first = row;
					all_states.push_back(fp);
				
			}
		}
	}
	for(int i = 0; i < all_states.size(); i++){
		for(int f = 0; f < all_states[i].size(); f++){
			for(int s = 0; s < sp.size(); s++){
				if(all_states[i][f].second == sp[s].second){
					
				}
			}
			for(int f2 = 0; f2 < all_states[i].size(); f2++){

			}
		}
	}
	return all_states;
}

bool check(wp, bp){
	for(int i = 0; i < wp.size(); i++){
		for(int j = 0; j < )
	}
}

bool minimax(int depth, vector<pair<char, pair<int, int> > > wp, vector<pair<char, pair<int, int> > > bp, bool maximilian){
	if(depth == m){

	}
	for(all possible moves){
		minimax(depth+1, nwp, nbp);
	}
}

int main(){
	int g;
	int w, b;
	cin >> g;
	for(int i = 0; i < g; i++){
		cin >> w >> b >> m;
		vector<pair<char, pair<int, int> > > wp;
		vector<pair<char, pair<int, int> > > bp;
		char t;
		int c, r;
		for(int j = 0; j < w; j++){
			cin >> t >> c >> r;
			wp.push_back(make_pair(t,make_pair(r,c)));

		}
		for(int j = 0; j < b; j++){
			cin >> t >> c >> r;
			bp.push_back(make_pair(t,make_pair(r,c)));
		}
		minimax(0, wp, bp);
	}
	
}