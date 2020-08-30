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

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >>T;
    for(int t = 0; t < T; t++){
        int n;
        double p;
        cin >> n;
        cin >> p;
        double q = 1-p;
        vector<vector<double>> DP(n, vector<double>(n, 0));
        for(double more = 0; more < n; more++) {
            for(double less=0; less < n; less++) {
                if (less == 0 && more == 0){
                    DP[less][more] = 0;
                    continue;
                }
                if (less + more >= n) {
                    break;
                }
                double pl = 0;
                double pm = 0;
                // keeping track of die for debugging purposes, to check the three add up to 1
                double die = 0;
                double m = less+more+1;
                double all = (m*(m-1))/2;
                double pandf = less/all;
                pl += p*pandf;
                die += q*pandf;
                double pandnf = more/all;
                pm += q*pandnf;
                die += p*pandnf;
                double landl = less*(less-1)/(2*all);
                double mandm = more*(more-1)/(2*all);
                pl += landl;
                pm += mandm;
                double landm = (more*less)/(all);
                pl += landm * p;
                pm += landm * q;
                // cout << "debug " << less << " " << more << " " << die+pl+pm << endl;
                // cout << "   " << die << ";" << pl << ";" << pm  << endl;
                // cout << "      " << pandf << " " << landm << endl;
                double ev = 0;
                if (less > 0) {
                    ev += pl * (DP[less-1][more]);
                }
                if (more > 0){
                    ev += pm *( DP[less][more-1]);
                }
                DP[less][more] = ev + 1;
            }
        }
        cout << "Case #" << t+1 << ":" << endl;
        for(int i = 0; i < n; i++){
            cout << std::setprecision(9) << DP[i][n-i-1] << endl;
        }
    }
	return 0;
}