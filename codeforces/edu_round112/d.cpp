// n, m = map(int, input().split())
// s = input()
// errs = []
// lss = ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
// for i in range(len(lss)):
//     err = []
//     # err[i] contains the num of errs up to and including i
//     cum = 0
//     ls = lss[i]
//     for j in range(n):
//         l = j%3
//         if s[j] != ls[l]:
//             cum +=1
//         err.append(cum)
//     errs.append(err)
// for i in range(m):
//     l, r = map(int, input().split())
//     l-=1
//     r-=1
//     ans = n+1
//     for j in range(len(errs)):
//         lefterrs = 0 if l==0 else errs[j][l-1]
//         ans = min(ans, errs[j][r]-lefterrs)
//     print(ans)
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
	int n, m;
	cin >> n >> m;
    string s;
    cin >> s;
    vector<vector<int> > errs;
    vector<string> lss{"abc", "acb", "bac", "bca", "cba", "cab"};
    for(int i = 0; i < lss.size(); i++){
        vector<int> err;
        int cum = 0;
        for(int j = 0; j < n; j++){
            int l = j%3;
            if(s[j] != lss[i][l]){
                cum += 1;
            }
            err.push_back(cum);
        }
        errs.push_back(err);
    }
    int l, r;
    for (int i = 0; i < m; i++){
        cin >> l >> r;
        l--; r--;
        int ans = n+1;
        for(int j = 0; j < errs.size(); j++){
            int lefterrs = (l==0) ? 0 : errs[j][l-1];
            ans = min(ans, errs[j][r]-lefterrs);
        }
        cout << ans << endl;
    }
    
	return 0;
}