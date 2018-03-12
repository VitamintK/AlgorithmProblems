//using stanford ACM notebook
#include <bits/stdc++.h>
#include <string>
#include <memory.h>
#define MAXE 100001
#define MAXV 100001
#define ll long long
#define ull unsigned long long

struct edge{int e, nxt;};
int V, E;
edge e[MAXE], er[MAXE];
int sp[MAXV], spr[MAXV];
int group_cnt, group_num[MAXV];
bool v[MAXV];
int stk[MAXV];
void fill_forward(int x)
{
  int i;
  v[x]=true;
  for(i=sp[x];i;i=e[i].nxt) if(!v[e[i].e]) fill_forward(e[i].e);
  stk[++stk[0]]=x;
}
void fill_backward(int x)
{
  int i;
  v[x]=false;
  group_num[x]=group_cnt;
  for(i=spr[x];i;i=er[i].nxt) if(v[er[i].e]) fill_backward(er[i].e);
}
void add_edge(int v1, int v2) //add edge v1->v2
{
	//cout << "HI" << endl;
	//cout << v1 << " " << v2 << endl;
  e [++E].e=v2; e [E].nxt=sp [v1]; sp [v1]=E;
  er[  E].e=v1; er[E].nxt=spr[v2]; spr[v2]=E;
}
void SCC()
{
  int i;
  stk[0]=0;
  memset(v, false, sizeof(v));
  for(i=1;i<=V;i++) if(!v[i]) fill_forward(i);
  group_cnt=0;
  for(i=stk[0];i>=1;i--) if(v[stk[i]]){group_cnt++; fill_backward(stk[i]);}
}


using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n, m, h;
	cin >> n >> m >> h;
	V = n;
	//E=0;
	vector<int> us(123456);
	for(int i = 1; i <= n; i++){
		cin >> us[i];
	}
	vector<int> c1s(n+1);
	vector<int> c2s(n+1);
	for(int i = 0; i < m; i++){
		cin >> c1s[i] >> c2s[i];
		//c1s[i]--;
		//c2s[i]--;
		if(us[c2s[i]] == (us[c1s[i]]+1)%h){
			//cout << "uh" << endl;
			add_edge(c1s[i], c2s[i]);
		}
		if(us[c1s[i]] == (us[c2s[i]]+1)%h){
			add_edge(c2s[i], c1s[i]);
		}
	}
	SCC();
	int ans = 0;
	//cout << " at least " << endl;
	vector<vector<int>> grups(group_cnt+1);
	int argmax = -1;
	for(int i = 1; i <= n; i++){
		//cout << group_num[i] << endl;
		//sizes[group_num[i]]++;
		grups[group_num[i]].push_back(i);
		if ((int)grups[group_num[i]].size() > ans){
			ans = (int)grups[group_num[i]].size();
			argmax = group_num[i];
		}

	}

	//solution is ALMOST complete.
	//instead of just finding the biggest SCC (which is more than obviously wrong)
	//we need to find the smallest SCC which is a leaf in the metagraph (which is a DAG)
	//equivalently, need to find the smallest SCC which has no outgoing edges.

	cout << ans << endl;
	for(int i = 0; i < grups[argmax].size(); i++){
		cout << grups[argmax][i] << " ";
	}
	cout << endl;
	return 0;
}