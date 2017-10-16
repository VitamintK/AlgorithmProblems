#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
#include <stdlib.h> 
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int p;
    cin >> p;
    vector<int> rs;
    vector<int> cs;
    
    for(int i = 0; i <= p; i++){
        int r, c;
        cin >> r >> c;
        rs.push_back(r);
        cs.push_back(c);
    }
    vector<vector<double> > terrain(n, vector<double>(m));
    vector<vector<double> > elevation(n, vector<double>(m));
    //string value;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> terrain[i][j];
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> elevation[i][j];
        }
    }
    //cout << "done reading " << endl;
    double ans = 0;
    for(int i = 0; i < p; i++){
        //cout << i << endl;
        priority_queue<pair<double, pair<int, int>>> pq;
        set<pair<int, int>> visited;
        pq.push(make_pair(0.0,make_pair(rs[i], cs[i])));
        while(!pq.empty()){
            pair<double, pair<int, int>> explore = pq.top();
            pq.pop();
            int r = explore.second.first;
            int c = explore.second.second;
            double cost = explore.first;
            //cout << "49 " << r << " " << c << endl;
            if(visited.count(make_pair(r, c)) > 0){
                continue;
            }
            visited.insert(make_pair(r, c));
            if(r == rs[i+1] && c == cs[i+1]){
                //cout << "$" << cost << endl;
                ans += cost;
                break;
            }
            vector<int> dr = {-1, 0, 1, 0};
            vector<int> dc = {0, -1, 0, 1};
            //dr.push_back(-1)
            for(int k = 0; k < 4; k++){
                int new_r = dr[k] + r;
                int new_c = dc[k] + c;
                //cout << " new " << new_r << " " << new_c << endl;
                if(new_r < 0 || new_r >= n || new_c < 0 || new_c >= m ){
                    continue;
                }
                if(visited.count(make_pair(new_r, new_c)) < 1){
                    //cout << elevation[new_r][new_c] << " " << elevation[r][c] << " " << terrain[r][c] << " " << terrain[new_r][new_c] << endl;
                    //cout << (double)(exp(3.5 * (double(abs((elevation[new_r][new_c] - elevation[r][c])/10.0 + 0.05))) << endl;
                    double marg_cost = -exp(3.5 * abs((elevation[new_r][new_c] - elevation[r][c])/10.0 + 0.05)) * (terrain[r][c] + terrain[new_r][new_c])/2.0;
                    //cout << "marg cost " << marg_cost << endl;
                    pq.push(make_pair(cost + marg_cost, make_pair(new_r, new_c)));
                }
            }
        }
    }
    cout << ceil(-ans) << endl;
    return 0;
}