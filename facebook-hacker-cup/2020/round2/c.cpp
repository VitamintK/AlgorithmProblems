#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <iomanip>

#define ll long long
#define ull unsigned long long
using namespace std;

ll MOD = 1000000007;

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >>T;
    for(int t = 0; t < T; t++){
        ll n, m, e, k;
        ll ax, bx, cx, ay, by, cy, ai, bi, ci, aw, bw, cw;
        cin >> n >> m >> e >> k;
        vector<ll> xs(n, 0);
        vector<ll> ys(n, 0);
        vector<ll> is(e, 0);
        vector<ll> ws(e, 0);
        for(int i = 0; i < k; i++) {
            cin >> xs[i];
        }
        cin >> ax >> bx >> cx;
        for(int i = 0; i < k; i++) {
            cin >> ys[i];
        }
        cin >> ay >> by >> cy;
        for(int i = 0; i < k; i++) {
            cin >> is[i];
        }
        cin >> ai >> bi >> ci;
        for(int i = 0; i < k; i++) {
            cin >> ws[i];
        }
        cin >> aw >> bw >> cw;
        for(int i = k, k < n; i++){
            xs[i] = (ax*xs[i-2] + bx * xs[i-1] + cx)%m;
        }
        for(int i = k, k < n; i++){
            ys[i] = (ay*ys[i-2] + by * ys[i-1] + cy)%m;
        }
        for(int i = k, k < e; i++){
            is[i] = (ai*is[i-2] + bi * is[i-1] + ci)%(n*m+n);
        }
        for(int i = k, k < e; i++){
            ws[i] = (aw*ws[i-2] + bw * ws[i-1] + cw)%(1000000000);
        }
        multiset<ll> voltage;
        vector<multiset<ll>> bst0s;
        vector<multiset<ll>> bst1s;
        vector<int> zeroorone(n*m, 0); // for each edge, are they in bst1s or bst2s?
        vector<int> whichbst(n, 0); // for each circle, is bst1 or bst2 bigger?  (might not need this actually probably don't)
        vector<int> edgeweights(n*m+n, 1);
        ll total = n*m + n;
        ll circlemaxsum = n*m;
        ll ans = 1;
        // partition edges into bst1 or bst2
        for(int circle = 0; circle < n; circle++) {
            int ee = xs[circle];
            while(true) {
                zeroorone[circle*m + ee] = 0;
                bst0s[circle].insert(1);
                if ((ee+1)%m == ys[circle]) {
                    break;
                }
                ee = (ee+1)%m;
            }
            ee = ys[circle];
            while(e != xs[circle]) {
                zeroorone[circle*m + ee] = 1;
                bts1s[circle].insert(1);
                ee = (ee+1)%m;
            }
            // decide which is bigger and send the smaller one to voltage
            whichbst[circle] = 0;
            if (!bst1s[circle].empty()) {
                voltage.insert(*bst1s[circle].rbegin());
            }
        }
        // insert the meta edges
        for(int i = 0; i < n; i++) {
            voltage.insert(1);
        }
        // process changes
        for(int i = 0; i < e; i++) {
            int edge = is[i];
            int weight = ws[i];
            if (edge >= n*m) {
                // meta edge
                total -= edgeweights[edge];
                voltage.erase(edgeweights[edge]);
                edgeweights[edge] = weight;
                voltage.add(weight);
            } else {
                // circle edge
                int circle = edge/m;
                total -= edgeweights[edge];
                circlemaxsum -= edgeweights[edge];
                if (whichbst(circle) == 0)
                voltage.erase()
            }
        }
        // TODO: finish writing this code
    }
	return 0;
}