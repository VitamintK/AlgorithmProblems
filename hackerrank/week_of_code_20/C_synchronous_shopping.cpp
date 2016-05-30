
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

struct edge{
    int cost;
    int to;
};

struct path{
    int cost_so_far;
    int node_to_explore;
     int fish_purchased;
    set<pair<int,int> > nodes_explored;
};

inline bool operator<(const path& lhs, const path& rhs)
{
  return lhs.cost_so_far < rhs.cost_so_far || (lhs.cost_so_far == rhs.cost_so_far && lhs.node_to_explore < rhs.node_to_explore) ||
      (lhs.cost_so_far == rhs.cost_so_far && lhs.node_to_explore == rhs.node_to_explore && lhs.fish_purchased < rhs.fish_purchased) || (lhs.cost_so_far == rhs.cost_so_far && lhs.node_to_explore == rhs.node_to_explore && lhs.fish_purchased == rhs.fish_purchased && lhs.nodes_explored != rhs.nodes_explored);
}

long fish[1024];
 int fish_sold_at[1000] = {0};
int n, m, k;
long shortest[1001][1024];

long djikstra(vector<vector<edge>> &graph, int from, int to){
    //for(int i = 0; i < n+1; i++){
        //cout << i << ": ";
    //    for(int j = 0; j < graph[i].size(); j++){
        //    cout << graph[i][j].to << " ";
    //    }
        //cout << endl;
    //}
    set<path*> *exploring = new set<path*>;
    set<int> explored;
    path tmp{0, 1, fish_sold_at[1], set<pair<int, int> >()};
    exploring->insert(&tmp);
    path explore;
    while(!exploring->empty()){
        explore = **(exploring->begin());
        //cout << " deleting: " << exploring.size() << "->";
        exploring->erase(exploring->begin());
        //cout << exploring.size() << endl;
        if(shortest[explore.node_to_explore][explore.fish_purchased] <= explore.cost_so_far){
            continue;
        } else {
            shortest[explore.node_to_explore][explore.fish_purchased] = explore.cost_so_far;
        }
        for(const edge &ed: graph[explore.node_to_explore]){
            //cout << explore.node_to_explore << "->" << ed.to << endl;
          //  if(shortest[ed.to][explore.fish_purchased|fish_sold_at[explore.node_to_explore]] <= ed.cost+explore.cost_so_far){
          //      continue;
          //  } else {
          //      shortest[ed.to][explore.fish_purchased|fish_sold_at[explore.node_to_explore]] = ed.cost+explore.cost_so_far;
          //  }
            //cout <<"nodes explored: ";
            //for(pair<int,int> kk : explore.nodes_explored){
            //    cout << kk.first << "->" << kk.second << ", ";
            //}
            //cout << endl;
            if(explore.nodes_explored.count(pair<int, int>(explore.node_to_explore, ed.to)) < 1){
                //cout <<"\tgood" << endl;
                //if we have not yet traversed this edge in this direction, then do so.
                if(ed.to == n){
                    //reached N!
                    //cout <<"Here! ";
                    //if(fish[explore.fish_purchased|fish_sold_at[ed.to]|fish_sold_at[explore.node_to_explore]] == 10000000000){
                        //cout <<"here" << endl;
                        fish[explore.fish_purchased|fish_sold_at[ed.to]|fish_sold_at[explore.node_to_explore]] = min((long)explore.cost_so_far + ed.cost, fish[explore.fish_purchased|fish_sold_at[ed.to]|fish_sold_at[explore.node_to_explore]]);
                    //} 
                    //continue;
                }
               
                    path *newp = new path{explore.cost_so_far + ed.cost, ed.to, explore.fish_purchased | fish_sold_at[explore.node_to_explore],
                         set<pair<int,int> >(explore.nodes_explored)};
                    newp->nodes_explored.insert(make_pair(explore.node_to_explore, ed.to));
                    //cout << "  " << exploring->size() << " ";
                    exploring->insert(newp);
                    //cout << exploring->size() << " " << &newp << endl;
                
            }
        }
    }
    //cout << k << endl;
    //cout << (1 << k) << endl;
    long mint = 10000000000;
    for(int i = 0; i < (1 << k); i++){
        for(int j = 0; j < (1 << k); j++){
            if((j | i) == ((1<<k)-1)){
                //cout <<"!!!!!! " << i << " " << j << " because " << (j|i) << endl;
                mint = min(mint, max(fish[j], fish[i]));
            }
        }
        //cout << i << " " << fish[i] << endl;

    }
    if(m == 0){
        cout << 0;
        return 0;
    }
    if(mint == 10000000000){
        while(true){}
    }
    cout << mint;

    return 0;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    for(int i = 0; i < 1024; i++){
        fish[i] = 10000000000;
    }
    for(int i = 0; i < 1001; i++){
        for(int j = 0; j < 1024; j++){
            shortest[i][j] = 10000000000;
        }
    }
    cin >> n >> m >> k;
    //cout << k << endl;
    vector<vector<edge> > grph(n+1);
    int fish_type;
    //int node_num;
    int t;
    for(int i = 0; i < n; i++){
        cin >> t;
        for(int j = 0; j < t; j++){
            cin >> fish_type;
            fish_sold_at[i+1] |= (1 << (fish_type-1));
        }
        
        //cout << "fish sold at " << i+1 << " " << fish_sold_at[i+1] << endl;
    }
    int x, y, z;
    for(int i = 0; i < m; i++){
        cin >> x >> y >> z;
        grph[x].push_back(edge{z, y});
        grph[y].push_back(edge{z,x});
    }
    djikstra(grph, 1, n);
    //cout << (1|4|16);
    return 0;
}
//YOU MIGHT HAVE TO GO PAST N
//1 <---> N <----> 2 (fish b here)
