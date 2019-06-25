#include <vector>
#include <string>
#include <iostream>

#define ll long long
#define ull unsigned long long
using namespace std;



int main() {
    std::ios::sync_with_stdio(false);

    vector<int>testcase = {1,2,3,8,99};

    int T, n, m;
    cin >> T >> n >> m;
    // T = testcase.size();
    // n = 365;
    // m = 100;
    vector<int> TESTS = {18, 17, 16, 15, 14, 13, 11};
    for(int t = 0; t < T; t++){
        vector<vector<int>> dps = vector<vector<int>>(n, vector<int>(m+1));
        vector<vector<int>> inputs = vector<vector<int>>(n, vector<int>(18));
        vector<int> offsets = vector<int>(n);
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < 18; j++){
                cout << TESTS[i%7];
                if(j != 17) {
                    cout << " ";
                }
            }
            cout << endl;

            int offset = 0;
            for(int j = 0; j < 18; j++) {
                int a;
                cin >> a;
                inputs[i][j] = a;
                offset += a;
            }
            offsets[i] = offset;
        }
        int ans;
        for(int j = 1; j <= m; j++){
            int invalid = 0;
            for(int i = 0; i < n; i++){
                if (j%TESTS[i%7] != offsets[i]%TESTS[i%7]){
                    invalid = 1;
                }
            }
            if(invalid == 0){
                ans = j;
                break;
            }
        }

        cout << ans << endl;
        int good;
        cin >> good;
        if(good == -1) {
            exit(0);
        }

    }
}