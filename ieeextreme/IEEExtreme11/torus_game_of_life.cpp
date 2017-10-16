#include <iostream>
#include <vector>
#include <map>
#define ll long long
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    ll C;
    cin >> C;
    vector<vector<int> > grid(n, vector<int>(m));
    vector<vector<int> > old_grid(n, vector<int>(m));
    map<string, ll> last_seen;
    char x;
    for(int i = 0 ; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> x;
            if(x == '*'){
                old_grid[i][j] = 1;
            } else {
                old_grid[i][j] = 0;
            }
        }
    }

    int seen_loop = false;
    //cout << " Here " << endl;
    for(ll i = 0; i < C; i++){
        //ll hashr = 0;
        string hashr = "";
        for(int r = 0 ; r < n; r++){
        for(int c = 0; c < m; c++){
            int alive_neighbors = 0;
            //cout << r << " " << c << endl;
            for(int dr = -1; dr <= 1; dr++){
                for(int dc = -1; dc <= 1; dc++){
                    if(dc == 0 && dr == 0){
                        continue;
                    }
                    //                    cout << dr << " " << dc << endl;

                    int new_r = (r + dr + n)%n;
                    int new_c = (c + dc + m)%m;
                    //cout << new_r << " " << new_c << endl;
                    alive_neighbors += old_grid[new_r][new_c];
                }
            }
            //cout << " Hey' << " << endl;
            if(old_grid[r][c]){
                if(alive_neighbors == 2 || alive_neighbors == 3){
                    grid[r][c] = 1;
                } else {
                    grid[r][c] = 0;
                }
            } else {
                if(alive_neighbors==3){
                    grid[r][c] = 1;
                } else {
                    grid[r][c] = 0;
                }
            }
            //hashr ^= grid[r][c] + 0x9e3779b9 + (hashr << 6) + (hashr >> 2);
            //hashr |= ;
            if(grid[r][c] == 0){
                hashr += "0";
            } else {
                hashr += "1";
            }
        }
        }
        if(last_seen.count(hashr) > 0 && !seen_loop){
            //i = last_seen[hashr] + (i - last_seen[hashr]) * ((C - last_seen[hashr])/(i-last_seen[hashr])) - 1;
            i = C - 1- ((C - 1 - i)%(i - last_seen[hashr]));
            seen_loop = true;
        }
        last_seen[hashr] = i;
        old_grid = grid;
    }
    for(int r = 0; r < n;  r++){
        for(int c = 0; c < m; c++){
            if(old_grid[r][c]){
                cout << "*";
            } else {
                cout << "-";
            }
        } cout << endl;
    }
}