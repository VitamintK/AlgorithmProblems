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

long double eps = 0.000000001;
long double dfs(long double c, long double m, long double p, long double v) { 
    long double ans = p;
    long double d;
    if (c > eps) {
        if (c > v) {
            d = v;
        } else {
            d = c;
        }
        if (m > eps) {
            ans += c * (dfs(c-d, m+d/2.0, p+d/2.0, v) + 1);
        } else {
            ans += c * (dfs(c-d, m, p+d, v) + 1);
        }
    }
    if (m > eps) {
        if (m > v){
            d = v;
        } else {
            d = m;
        }
        if (c > eps) {
            ans += m * (dfs(c+d/2.0, m-d, p+d/2.0, v) + 1);
        } else {
            ans += m * (dfs(c, m-d, p+d, v) + 1);
        }
    }
    return ans;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >> T;
    for(int t = 0; t < T; t++){
        long double c,m,p,v;
        cin >> c >> m >> p >> v;
        cout << dfs(c,m,p,v) << endl;
    }
    
	return 0;
}