#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    //for each node A in the set of nodes:
    //we're gonna start at each node A, and find all the nodes that are 2 edges away from A.  If there's any node that 
    //has 2 different paths that are 2 edges away from A, then this is a cycle.  There are (n C 2) cycles involving that point
    //where n = paths of length 2 to that point.
    long n, m;
    cin >> n >> m;
    vector<vector<long> > graph(n+1);
    long a1, a2;
    for(int i =0; i < m; i++){
        cin >> a1 >> a2;
        graph[a1].push_back(a2);
        graph[a2].push_back(a1);
    }
    long long ans;
    for(int i = 1; i <= n; i++){
        int reachable[50001] = {0};
        long cycles_from_i = 0;
        for(int nodea : graph[i]){
            for(int nodeb: graph[nodea]){
                if(nodeb != i){
                    cycles_from_i += reachable[nodeb];
                    reachable[nodeb]++;
                }
            }
        }
        ans+=cycles_from_i;
    }
    cout << ans/4;
    return 0;
}
