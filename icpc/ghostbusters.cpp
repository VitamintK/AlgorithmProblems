#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<ll> xs; //xs[i] stores the x coordinate of the ith ghostbuster
vector<ll> ys; //ys[i] stores the y coordinate of the ith ghostbuster
int n;

bool check(ll length){
	//perform 2SAT solving (guide here: http://www.geeksforgeeks.org/2-satisfiability-2-sat-problem/ )
	map<ll, vector<ll>> digraph; // digraph is the Implication Graph.
	//digraph[i] stores the edges coming out of the node for ghostbuster i
	//digraph[-i] stores the edges coming out of the node for NOT ghostbuster i

	//we'll say that a ghostbuster i being vertical is represented as the x_i literal being TRUE
	//and ghostbuster i being horizontal is represented as the x_i literal being FALSE.
	//(This is to build the CNF that represents this problem, but only represent it implicitly as the implication digraph.)
	//See the geeksforgeeks guide to see how the CNF maps to a implication graph.
	for(ll i = 0; i < n; i++){
		for(ll j = 0; j < i; j++){
			if(ys[i] == ys[j] && abs(xs[i] - xs[j]) <= length*2){
				//i and j are on the same horizontal line.  if both are horizontal, they will collide.
				//thus, at least one must be vertical. We say this as (x_i V x_j) where V is the boolean OR.
				//again, remember that x_i being true means that ghostbuster i is vertical.
				digraph[-j].push_back(i); //if j is horizontal, then i must be vertical.
				digraph[-i].push_back(j); //if i is horizontal, then j must be vertical.
			}

			if(xs[i] == xs[j] && abs(ys[i] - ys[j]) <= length*2){
				//i and j are on the same vertical line and within colliding distance.
				//Thus, at least one must be horizontal.
				//The boolean expression that expresses that is (~x_i V ~x_j).  Remember, ~x_i means that ghostbuster i is horizontal.
				digraph[j].push_back(-i); //if j is vertical, then i must be horizontal.
				digraph[i].push_back(-j); //if i is vertical, then j must be horizontal.  Because of the implication.
			}
		}
	}
	//Ok, now we're done building the implication graph.  
	//Now we do Tarjan's algorithm to find if there's a strongly connected component.
	//If x_i and -x_i are in the same strongly connected component, then there's no solution.
	//https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm#The_algorithm_in_pseudocode
	ll index = 0;
	vector<ll> S;
	vector<ll> indices(n, -1);
	vector<ll> lowlink(n, -1);
	for(ll i = 0; i < n; i++){
		if(indices[i] == -1){
			indices[i] = index;
			lowlink[i] = index;
			index++;
			S.push_back(i);
		}
	}
}


int main(){
	std::ios::sync_with_stdio(false);
	cin >> n;
	for(int i = 0; i < n; i++){
		ll x, y;
		cin >> x >> y;
		xs.push_back(x);
		ys.push_back(y);
	}

	ll L = 0;
	ll R = 8234567;
	while(R - L > 0){
		//binary search to find the biggest length for which we can arrange ghostbusters with no stream-crossing
		ll mid = (R - L)/2;
		//check returns true if we can make an arrangement with length mid with no stream-crossing. false if we can't.
		int ok = check(mid);
	}
	return 0;
}