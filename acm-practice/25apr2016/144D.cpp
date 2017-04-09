#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;
//http://codeforces.com/problemset/problem/144/D 
//a shortest paths problem
struct Edge{
	int v , next,w;
	/* data */
};
Edge e[Maxm];
int head[Maxn];
void add(int u,int v,w){
	e[++ecnt].v = v ; e[cent].w=w; e[ecnt].next = head[u]; head[u] = ecnt;
}
vector<int> e[Maxn];
int main(){
	long n, m, s;
	long v, u, w;
	cin >> n >> m >> s;
	for(long i = 0; i < m; i++){
		cin >> v >> u >> w;
		e[u].push_back(v);
		e[v].push_back(u);
	}

	for (int i=head[u];i;i= e[i].next){

	}
	return 0;
}