#include<bits/stdc++.h>

using namespace std;

vector<vector<int> > has(501);
vector<vector<int> > is(501);
//vector<vector<vector<int> > > DP(vector<int>(2, vector<int>(501, vector<int>(501, -1))));
int DP[2][501][501];
void dfs(int i, int p, int has_flag, int ROOT){
    for(int n = 0; n < is[i].size(); n++){
        if(is[i][n] == p){
            continue;
        }
        if(DP[has_flag][ROOT][is[i][n]] == 0){
            DP[has_flag][ROOT][is[i][n]] = 1;
            dfs(is[i][n], i, has_flag, ROOT);
        }
    }
    for(int n = 0; n < has[i].size(); n++){
        if(has[i][n] == p){
            continue;
        }
        if(DP[1][ROOT][has[i][n]] == 0){
            DP[1][ROOT][has[i][n]] = 1;
            dfs(has[i][n], i, 1, ROOT);
        }
    }
}

int main(){
    int n, m;
    cin >> n >> m;
    map<string, int> classmap;
    int classes = 0;
    for(int i = 0; i < n; i++){
        string a, b, c;
        cin >> a >> b >> c;
        if(classmap.count(a) < 1){
            classmap[a] = classes;
            classes++;
        }
        if(classmap.count(c) < 1){
            classmap[c] = classes;
            classes++;
        }
        if(b == "is-a"){
            is[classmap[a]].push_back(classmap[c]);
        } else {
            has[classmap[a]].push_back(classmap[c]);
        }
    }

    for(int i = 0; i < classes; i++){
        DP[0][i][i] = 1;
        dfs(i, i, 0, i);
    }
    
    for(int i = 0; i < m; i++){
        string a ,b, c;
        cin >> a >> b >> c;
        if(b == "is-a"){
            cout << "Query " << i+1 << ": " <<  (DP[0][classmap[a]][classmap[c]]? "true" : "false") << endl;
        } else {
            cout << "Query " << i+1 << ": " << (DP[1][classmap[a]][classmap[c]]? "true": "false") << endl;
        }
    }
    return 0;
}