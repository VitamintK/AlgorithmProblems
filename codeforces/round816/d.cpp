// g++ -std=c++17 x.cpp && ./a.out
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

int main(){
	std::ios::sync_with_stdio(false);	
    int M = 30;
    int n,q;
    cin >> n >> q;
    vector<vector<int>> ans(n, vector<int>(M, -1));
    vector<vector<vector<int>>> edges(n, vector<vector<int>>(M));

    for (int l=0; l<q; l++){
        int i,j,x;
        cin >> i >> j >> x;
        i--;
        j--;
        for(int k=0; k < M; k++){
            int one= x&1;
            x/=2;
            if(j==i){
                ans[i][k] = one;
                continue;
            }
            if(one){
                edges[i][k].push_back(j);
                edges[j][k].push_back(i);
            } else {
                ans[i][k] = 0;
                ans[j][k] = 0;
            }
        }
    }
    for(int i=0; i<ans.size();i++){
        for(int k=0; k < M; k++){
            if (ans[i][k]==0){
                for (int m=0; m < edges[i][k].size(); m++){
                    ans[edges[i][k][m]][k] = 1;
                }
            }
        }
    }
    for(int i=0;i<ans.size();i++){
        int x =0;
        int p = 1;
        for(int k = 0; k < M; k++){
            if(ans[i][k]==1){
                x |= p;
            } else if(ans[i][k] == -1){
                for(int m=0; m < edges[i][k].size(); m++){
                    ans[edges[i][k][m]][k] = 1;
                }
            }
            p <<= 1;
        }
        cout << x << " ";
    }
    cout << endl;


	return 0;
}
