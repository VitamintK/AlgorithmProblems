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

int minimax(pair<int, int> state, int depth, int maximizingPlayer){
//state: cop, robber
    if (memo.count(make_pair(maximizingPlayer, state)) > 0){
        return memo[make_pair(maximizingPlayer, state)];
    }
    cout << state.first << " " << state.second << endl;
    int best_value;
    //cout << "41 " << endl;
     if(state.first == state.second && state.first!= -1 && state.second != -1){
         //WE WIN!
        cout << "we win " << state.first << " " << state.second << " " << maximizingPlayer << endl;
        history[state.first][state.second][maximizingPlayer] = 0;
        //cout << "uh" << endl;
        return depth;
     }
     //cout << " HI" << endl;
     if(state.first != -1 && state.second != -1){
        if(history[state.first][state.second][maximizingPlayer] == 1){
         //we looped.  return inf.
            history[state.first][state.second][maximizingPlayer] = 0;
            memo[make_pair(maximizingPlayer, state)] = 123456789;
            return 123456789;
        }
        history[state.first][state.second][maximizingPlayer] = 1;
    }
     //cout << 1 << endl;
    if(maximizingPlayer){
        //cout << "maximizing PLyaer " << maximizingPlayer << endl;
        //robber
        best_value = -123456789;
        //cout << " 59" << endl;
        if(state.second != -1){
            for(int i = 0; i < edges[state.second].size(); i++){
                int v = minimax(make_pair(state.first, edges[state.second][i]), depth+1, false);
                best_value = max(best_value, v);
            }
            int v = minimax(state, depth+1, false); //stand in place
            best_value = max(best_value, v);
        } else {
            //cout << " 68" << endl;
            for(int i = 0; i < n; i++){
                int v = minimax(make_pair(state.first, i), depth+1, false);
                best_value = max(best_value, v);
            }
        }
    } else {
        // minimizing player
        //cout << "minimizing player" << endl;
        best_value = 123456789;
        if(state.first != -1){
            for(int i = 0; i < edges[state.first].size(); i++){
                int v = minimax(make_pair(edges[state.first][i], state.second), depth+1, true);
                best_value = min(best_value, v);
            }
        } else {
            for(int i = 0; i < n; i++){
                cout << " 97 " << i << endl;
                int v = minimax(make_pair(i, state.second), depth+1, true);
                best_value = min(best_value, v);
            }
        }
    }
    if(state.first != -1 && state.second != -1){
        history[state.first][state.second][maximizingPlayer] = 0;
    }
    memo[make_pair(maximizingPlayer, state)] = best_value;
    return best_value;
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
    int cop = -1;
    int robber = -1;
    int best = 1000000000;
    int best_i;
    for(int i = 0; i < n; i++){
        cop = minimax(make_pair(i, robber), 0, false);
        cout << i << ": " << cop << endl;
        if(cop < best){
            best = cop;
            best_i = i;
        }
    }
    SetWhite(best_i+1);
    while(robber = GetBlack()){
        cop = minimax(make_pair(cop, robber), 0, false);
        SetWhite(cop);
    }
    return 0;
}

