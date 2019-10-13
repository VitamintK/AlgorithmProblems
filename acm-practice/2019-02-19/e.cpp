// T = int(input())

// for t in range(T):
//     m, s = map(int, input().split())
//     coins = []
//     for i in range(m):
//         a, b = map(int, input().split())
//         coins.append((a,b))

//     ans = None
//     DP = [[None for i in range(s+1)] for j in range(s+1)]
//     DP[0][0] = 0
//     for r in range(len(DP)):
//         if ans:
//             break
//         for c in range(len(DP[0])):
//             if ans or r*r+c*c>s*s:
//                 break
//             for dr, dc in coins:
//                 if dr > r or dc > c:
//                     continue
//                 if DP[r-dr][c-dc] is None:
//                     continue
//                 if DP[r][c] is None:
//                     DP[r][c] = DP[r-dr][c-dc]+1
//                 else:
//                     DP[r][c] = min(DP[r][c], DP[r-dr][c-dc]+1)
//                 if r*r+c*c==s*s and ans is None:
//                     ans = DP[r][c]
//     if ans is None:
//         print("not possible")
//     else:
//         print(ans)
//     if t < T-1:
//         input()

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++){
        int m, s;
        cin >> m >> s;
        vector<pair<int, int>> coins;
        for(int i = 0; i < m; i++){
            int a, b;
            cin >> a >> b;
            coins.push_back(make_pair(a, b));
        }

        int ans = 12345678;
        vector<vector<int> > DP(s+1,vector<int>(s+1, -1));
        DP[0][0] = 0;

        for(int r = 0; r < DP.size(); r++){
            for(int c = 0; c < DP[0].size(); c++){
                for(int i = 0; i < coins.size(); i++){
                    int dr = coins[i].first;
                    int dc = coins[i].second;
                    if(dr > r || dc > c){
                        continue;
                    }
                    if(DP[r-dr][c-dc] == -1){
                        continue;
                    }
                    if(DP[r][c] == -1){
                        DP[r][c] = DP[r-dr][c-dc]+1;
                    } else {
                        DP[r][c] = min(DP[r][c], DP[r-dr][c-dc]+1);
                    }
                    if(r*r+c*c==s*s){
                        ans = min(ans, DP[r][c]);
                    }
                }
            }
        }
        if (ans == 12345678){
            cout << "not possible" << endl;
        } else {
            cout << ans << endl;
        }

    }
    return 0;
}

