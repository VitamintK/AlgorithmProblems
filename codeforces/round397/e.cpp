#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	vector<vector<ll>> edges(n);
	for(ll i = 0; i < n-1; i++){
		ll u, v;
		cin >> u >> v;
		edges[u-1].push_back(v-1);
		edges[v-1].push_back(u-1);
	}
	//find a diameter of the tree.  then either one of the two leaves found is the root of the folded tree,
	//or the midpoint is a junction s.t. all of the leaves except possibly 1 are equidistant from it

//diameter: BFS from 0.
	queue<ll> q;
	set<ll> explored;
	q.push(0);
	explored.insert(0);
	ll ex;
	while(!q.empty()){
		ex = q.front();
		q.pop();
		for(ll i = 0; i < edges[ex].size(); i++){
			if(explored.count(edges[ex][i]) < 1){
				q.push(edges[ex][i]);
				explored.insert(edges[ex][i]);
			}
		}
	}
//BFS again
	//also root the tree at ex.
	vector<ll> parent(n);
	//
	pair<ll, ll> exx;
	ll exq, exr;
	queue<pair<ll, ll>> qq;
	qq.push(make_pair(0, ex));
	explored.clear();
	explored.insert(ex);
	while(!qq.empty()){
		exx = qq.front();
		exq = exx.second;
		exr = exx.first;
		qq.pop();
		for(ll i = 0; i < edges[exq].size(); i++){
			if(explored.count(edges[exq][i]) < 1){
				qq.push(make_pair(exr+1, edges[exq][i]));
				explored.insert(edges[exq][i]);
				parent[edges[exq][i]] = exq;
			}
		}
	}
	//cout << ex << " " << exr << " distance from " << exq << endl;
	//ex, exq are our leaves, and exr is the diameter length
	ll ans = -1;
//case 1: ex is root.
	ll leaf_distance = -1;
	vector<pair<ll, ll>> stack;
	stack.push_back(make_pair(0,ex));
	explored.clear();
	explored.insert(ex);

	bool chillin = true;
	while(!stack.empty()){
		pair<ll, ll> exz = stack.back();
		stack.pop_back();
		ll added = 0;
		for(ll i =0; i < edges[exz.second].size(); i++){
			if(explored.count(edges[exz.second][i]) < 1){
				stack.push_back(make_pair(exz.first+1, edges[exz.second][i]));
				explored.insert(edges[exz.second][i]);
				added++;
			}
		}
		if(added == 0){
			if(leaf_distance == -1){
				leaf_distance = exz.first;
			//	cout <<"82" << endl;
			} else if(leaf_distance != exz.first){
				chillin = false;
				//cout << "85" << endl;
			}
		}
	}
	if(chillin){
		ans = leaf_distance;
					//		cout << ans << " 90" << endl;

	}
//case 2: exq is root.
	leaf_distance = -1;
	stack.clear();
	stack.push_back(make_pair(0,exq));
	explored.clear();
		explored.insert(exq);

	chillin = true;
	while(!stack.empty()){
		pair<ll, ll> exz = stack.back();
		stack.pop_back();
		ll added = 0;
		for(ll i =0; i < edges[exz.second].size(); i++){
			if(explored.count(edges[exz.second][i]) < 1){
				stack.push_back(make_pair(exz.first+1, edges[exz.second][i]));
				explored.insert(edges[exz.second][i]);
				added++;
			}
		}
		if(added == 0){
			if(leaf_distance == -1){
				leaf_distance = exz.first;
			} else if(leaf_distance != exz.first){
				chillin = false;
			}
		}
	}
	if(chillin){
		if(ans == -1){
			ans = leaf_distance;
		} else{
			ans = min(ans, leaf_distance);
		}
							//cout << ans << " 125" << endl;

	}
//case 3: root is midway point.
	if(true){
		//find the midway point:
		ll mid = exq;
		for(ll i =0 ; i < exr/2; i++){
			mid = parent[mid];
		}
//cout << mid << endl;
		leaf_distance = -1;
		stack.clear();
		stack.push_back(make_pair(0,mid));
		explored.clear();
			explored.insert(mid);

		set<ll> leaf_values;
		//cout <<"123" << endl;
		while(!stack.empty()){
			pair<ll, ll> exz = stack.back();
			//cout << exz.second << endl;
			stack.pop_back();
			ll added = 0;
			for(ll i =0; i < edges[exz.second].size(); i++){
				if(explored.count(edges[exz.second][i]) < 1){
					stack.push_back(make_pair(exz.first+1, edges[exz.second][i]));
					explored.insert(edges[exz.second][i]);
					//cout << edges[exz.second][i] << endl;
					added++;
				}
			}
			if(added == 0){
				//if(leaf_distance == -1){
				//	leaf_distance = exz.first;
				//} else if(leaf_distance != exz.first){
			//		chillin = false;
			//	}
				leaf_values.insert(exz.first);
				//cout << exz.first <<"!" << endl;
			}
		}
		if(leaf_values.size() <= 2){
			ll aa = 0;
			for(auto i: leaf_values){
				aa+= i;
			}
			if(ans == -1){
				ans = aa;
			} else{
				ans = min(ans, aa);
			}
					//cout << ans << " 165" << endl;

		}
	}

	if(ans > -1){
		while(ans%2 == 0){
			ans/=2;
		}
	}

	cout << ans << endl;

	return 0;
}