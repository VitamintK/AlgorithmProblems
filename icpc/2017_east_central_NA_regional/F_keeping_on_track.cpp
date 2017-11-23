//author: Pasha
#include<bits/stdc++.h>

using namespace std;

int n;
vector<vector<int> > adj;
vector<int> sub;
vector<int> disc;
vector<bool> visited;

int dfs(int node){
    visited[node] = true;
    int ans = 1;
    for(int j = 0; j < adj[node].size(); j++){
        int next = adj[node][j];
        if(!visited[next])
            ans += dfs(next);
    }
    sub[node] = ans;
    return ans;
}


int main(){
    
    cin >> n;
    adj = vector<vector<int> >(n+1);
    visited = vector<bool> (n+1);
    sub = vector<int>(n+1);
    disc = vector<int>(n+1);
    for(int i = 0 ; i < n;i++){
        int a,b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }


    dfs(0);
    
    // for(int i=0;i<=n;i++)
    //     cout << sub[i] << " " ;
    // cout << flush << endl;   

    for(int node = 0; node <= n;node++){
        int ans = (n * (n-1)) / 2 ;
        // cout << node << " : " << ans << " ";
        for(int j = 0; j < adj[node].size(); j++){
            int next = adj[node][j];
            if(sub[next] > sub[node])
                continue;

            int s = sub[next];
            // cout << " , " << s;
            ans -= s * (s-1) / 2;
        }
        
        int top = n+ 1 - sub[node];
        ans -= (top * (top-1))  /2;
        // cout << " , " << top;
        
        disc[node] = ans;
        // cout << " == " << ans; 
    }

    // for(int i=0;i<=n;i++)
    //     cout << disc[i] << " " ;
    // cout << endl;

    int critical = 0;
    for(int i=0;i<=n;i++){
        if(disc[i] > disc[critical])
            critical = i;
    }
    
    vector<int> R;
    for(int j = 0; j < adj[critical].size(); j++){
        int next = adj[critical][j];
        if(sub[next ] > sub[critical])
            continue;
        R.push_back(sub[next]);
    }
    R.push_back(n + 1 - sub[critical]);

    sort(R.begin(), R.end());
    int ans2 = disc[critical];
    if(R.size() >= 2)
        ans2 -= R[R.size()-1] * R[R.size()-2];

    cout << disc[critical] << " " << ans2 << endl;

    return 0;
}