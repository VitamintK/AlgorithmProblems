#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

// functions used to comunicate with the interactor (the other program)
// use this to get the position of the other player.
// after using it you must do your own move
// TL;DR GetBlack() GetBlack() is invalid
int GetBlack() {
    int black_king_node;
    cin >> black_king_node;
    return black_king_node;
}

// use this to set your own move
void SetWhite(int node) {
    cout << node << endl;
}

int n, m;
vector<vector<int> > edges;
vector<vector<vector< bool> > > history;

void ReadGraph() {
    cin >> n >> m;
    edges.resize(n);
    for(int i = 0; i < n; i++){
        history.push_back(vector<vector<bool>>(n, vector<bool>(2, 0)));
    }
    for (int i = 0; i < m; i += 1) {
        int a, b;
        cin >> a >> b;
        edges[a-1].push_back(b-1);
        edges[b-1].push_back(a-1);
    }
}

map<pair<int, pair<int, int>>, int> memo;

int min_value(pair<int, int> state, int depth);

int max_value(pair<int, int> state, int depth){
    if(depth > 200){
        return 123456789;
    }
    if(state.first == state.second && state.first != -1){
        cout << "we won " << endl;
        return 0;
    }
    if(state.first != -1 && state.second != -1){
        if(memo.count(make_pair(1, state)) > 0){
            return memo[make_pair(1, state)];
        }
        if(history[state.first][state.second][1] == 1){
            cout << state.first << " " << state.second << " here again" << endl;
            return 123456789;
        }
        history[state.first][state.second][1] = 1;
    }
    if(state.second == -1){
        int best_value = -123456789;
        for(int i = 0; i < n; i++){
            int v = min_value(make_pair(state.first, i), depth + 1);
            best_value = max(best_value, v);
        }
        return best_value + 1;
    }
    int best_value = -123456789;
    for(int i = 0; i < edges[state.second].size(); i++){
        int v = min_value(make_pair(state.first, edges[state.second][i]), depth + 1);
        best_value = max(best_value, v);
    }
    int v = min_value(state, depth + 1);
    best_value = max(best_value, v);
    history[state.first][state.second][1] = 0;
    memo[make_pair(1, state)] = best_value + 1;
    return best_value + 1;
}

int min_value(pair<int, int> state, int depth){
    if(state.first == state.second && state.first != -1){
        return 0;
    }
    if(memo.count( make_pair(0, state)) > 0){
        return memo[make_pair(0, state)];
    }
    //if(history[state.first][state.second][0] == 1){
    //    return 123456789;
    //}
    history[state.first][state.second][0] = 1;
    int best_value = 123456789;
    for(int i = 0; i < edges[state.first].size(); i++){
        int v = max_value(make_pair(edges[state.first][i], state.second), depth+1);
        best_value = min(best_value, v);
    }
    history[state.first][state.second][0] = 0;
    memo[make_pair(0, state)] = best_value + 1;
    return best_value + 1;
}

int minimax(pair<int, int> state){
    //state: cop, robber

    int best_value = 1234567890;
    int best_index;
    if(state.first == -1){
        for(int i = 0; i < n; i++){
            int v = max_value(make_pair(i, state.second), 0);
                cout << i << " " << v << endl;

            if(v < best_value){
                best_value = v;
                best_index = i;
                cout << 116 << endl;
                cout << best_value << " " << best_index << endl;
            }
        }
    } else {
        for(int i = 0; i < edges[state.first].size(); i++){
            int v = max_value(make_pair(edges[state.first][i], state.second), 0);
            if(v < best_value){
                best_value = v;
                best_index = edges[state.first][i];
                cout << 124 << endl;
            }
        }
    }
    cout << best_value << "  " << best_index << "." << endl;
    return best_index;
}

int main() {
    // use this to pass the first example
    ReadGraph();
    // vector<vector<int> > all_pairs(n, vector<int>(n, 12345678));
    // for(int i = 0; i < n; i++){
    //             all_pairs[i][i] = 0;
    // }
    // for(int i =0; i < n; i++){
    //     for(int j = 0; j < edges[i].size(); j++){
    //         all_pairs[i][j] = 1;
    //     }
    // }
    // for(int k = 0; k < n; k++){
    //     for(int i = 0; i < n; i++){
    //         for(int j = 0; j < n; j++){
    //             if(all_pairs[i][j] > all_pairs[i][k] + all_pairs[k][j]){
    //                 all_pairs[i][j] = all_pairs[i][k] + all_pairs[i][k];
    //             }
    //         }
    //     }
    // }
    // //find starting point
    // int min_max_len = 123456789;
    // int min_max_len_ind;
    // for(int cand = 0; cand < n; cand++){
    //     int max_len = 0;
    //     for(int to = 0; to < n; to++){
    //         max_len = max(max_len, all_pairs[cand][to]);
    //     }
    //     if(max_len < min_max_len){
    //         min_max_len = max_len;
    //         min_max_len_ind = cand;
    //     }
    // }
    int robber = -1;
    //for(int i = 0; i < n; i++){
     //   cop = minimax(make_pair(i, robber), 0, false);
    //    cout << i << ": " << cop << endl;
    //    if(cop < best){
    //        best = cop;
    //        best_i = i;
   //     }
    //}
    int cop = minimax(make_pair(-1, -1));
    SetWhite(cop);
    while(robber = GetBlack()){
        cop = minimax(make_pair(cop, robber));
        SetWhite(cop);
    }
    return 0;
}

