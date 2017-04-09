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
int targhash;

int myhash(vector<vector<bool>> VV){
	int ans = 0;
	for(int i = 0; i < 5; i++){
		for(int j = 0; j < 5; j++){
			ans<<=1;
			ans|=(int)(VV[i][j]);
		}
	}
	return ans;
}
int countbits(int a){
	int ans = 0;
	while(a != 0){
		ans+= (a&1);
		a>>=1;
	}
	return ans;
}
vector<vector<bool>> rhash(int num){
	//cout << num << endl;
	vector<vector<bool>> ans(5, vector<bool>(5));
	//cout << ans[0].size() << endl;
	for(int i = 4; i >= 0; i--){
		for(int j = 4; j >= 0; j--){
			ans[i][j] = (num&1);
			//cout << ans[i][j] << " ";
			num>>=1;
		}//cout << endl;
	}
	return ans;
}

bool cust(pair<int, ll> a, pair<int, ll> b){
	int aa = countbits(a.first^targhash);
	int bb = countbits(b.first^targhash);
	return aa+a.second > bb+b.second;
}
int main(){
	ll t;
	cin >> t;
	
	char temp;
	for(ll i = 0; i < t; i++){
		vector<vector<bool>> og(5);
		vector<vector<bool>> target(5);
		for(ll row = 0; row < 5; row++){
			for(ll col = 0; col < 5; col++){
				cin >> temp;
				if(temp=='.'){
					og[row].push_back(false);
				} else {
					og[row].push_back(true);
				}
			}
			for(ll col = 0; col < 5; col++){
				cin >> temp;
				if(temp=='.'){
					target[row].push_back(false);
				} else {
					target[row].push_back(true);
				}
			}
		}
		targhash = myhash(target);
		//cout << targhash << " also " << myhash(rhash(targhash)) << endl;
		//actually do shit
		priority_queue<pair<int, ll>, vector<pair<int,ll>>, decltype(&cust)> q(cust);
		q.push(make_pair(myhash(og), 0));
		set<int> explored;
		//ll cur_count = 0;
		bool solnfound = false;
		while(!q.empty()){
			if(solnfound){
				break;
			}
			pair<int,ll> ex = q.top();
			//if(ex.second != cur_count){
			//	cur_count++;
		//		break;
		//	}
			if((countbits(ex.first)^targhash) == 1){
									solnfound = true;

			//cout << countbits(ex.first ^ targhash) << endl;
			//out << "the fuck" << endl;
		}
			//vector<vector<bool>> quilt = ex.first;
			q.pop();
			//cout << countbits()
			//cout << explored.size() << endl;
//cout << ex.second << endl;
	//		cout << ex.first << endl;
			if(ex.first == targhash){
									solnfound = true;

				cout << ex.second << endl;
				return 0;
				break;
			}
			//if(explored.count(ex.first)<1){
				explored.insert(ex.first);
				for(int size = 1; size <= 5; size++){
					for(int row = 0; row + size - 1 < 5; row++){
						for(int col = 0; col + size - 1 < 5; col++){
							//flip vertical
							bool temp;
//cout << "line 99" << endl;
							vector<vector<bool>> quilt = rhash(ex.first);
//cout << "line 100" << endl;
							for(int rowoff = 0; rowoff < size/2; rowoff++){
								for(int coloff = 0; coloff < size; coloff++){
									temp = quilt[row+rowoff][col+coloff];
									quilt[row+rowoff][col+coloff] = quilt[row+size-1-rowoff][col+coloff];
									quilt[row+size-1-rowoff][col+coloff] = temp;
								}
							}
							int m = myhash(quilt);
							if(explored.count(myhash(quilt))<1){
								explored.insert(m);
								if(myhash(quilt) == targhash){
									solnfound = true;

									cout << ex.second+1 << endl;
									while(!q.empty()){
										q.pop();
									}

									break;
								}
								//cout <<"pushing" << endl;
								q.push(make_pair(m, ex.second+1));
							}
							//flip horizontal
							//temp;
							quilt = rhash(ex.first);
//cout << "line 122" << endl;
							for(int coloff = 0; coloff < size/2; coloff++){
								for(int rowoff = 0; rowoff < size; rowoff++){
									temp = quilt[row+rowoff][col+coloff];
									quilt[row+rowoff][col+coloff] = quilt[row+rowoff][col+size-1-coloff];
									quilt[row+rowoff][col+size-1-coloff] = temp;
								}
							}
							m = myhash(quilt);
							if(explored.count(m)<1){
								explored.insert(m);
								//cout << explored.count(m) << endl;

								if(myhash(quilt) == targhash){
																		solnfound = true;

									cout << ex.second+1 << endl;
									while(!q.empty()){
										q.pop();
									}
									break;
								}
								//cout <<"pusing2" << endl;
								q.push(make_pair(m, ex.second+1));
							}
							//invert
							//bool temp;
							//if(size == 1){
							//	cout << "hey" << endl;
							//}
							quilt = rhash(ex.first);

							for(int coloff = 0; coloff < size; coloff++){
								for(int rowoff = 0; rowoff < size; rowoff++){
									//cout << quilt[row+rowoff][col+coloff] << " " ;
									quilt[row+rowoff][col+coloff] = (!quilt[row+rowoff][col+coloff]);
									//cout << quilt[row+rowoff][col+coloff] << endl ;
									//if(size == 1){
									//	cout <<"yea" << endl;
									//}
								}
							}
							m = myhash(quilt);
							if(explored.count(m)<1){
								//cout << countbits(m ^ targhash) << endl;
								explored.insert(m);
								q.push(make_pair(m, ex.second+1));

								if(myhash(quilt) == targhash){
									//cout <<"whasdfy" << endl;
									cout << ex.second+1 << endl;
									while(!q.empty()){
										q.pop();
									}
									solnfound = true;
									break;
								}
								//cout <<"pushing3" << endl;

							}
						}
					}
				}	
		}
		//
		
	}
}