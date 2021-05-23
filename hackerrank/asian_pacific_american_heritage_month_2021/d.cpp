#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);



/*
 * Complete the 'findMinimumPathLength' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY edges
 *  3. INTEGER_ARRAY visitNodes
 */

// translating python code to C++ to fix segfault
// 
// def dfs(start, edges, visitNodes, visited):
//     tot_dist = 0
//     visited.add(start)
//     for v in edges[start]:
//         if v not in visited:
//             relevant_distance = dfs(v, edges, visitNodes, visited)
//             if relevant_distance > 0 or v in visitNodes:
//                 tot_dist += relevant_distance + 1
//     return tot_dist

// def findMinimumPathLength(n, edges, visitNodes):
//     # Write your code here
//     ed = [[] for i in range(n)]
//     visitNodes = {v-1 for v in visitNodes}
//     for u,v in edges:
//         ed[u-1].append(v-1)
//         ed[v-1].append(u-1)
//     straight = dfs(0, ed, {n-1}, set())
//     al = dfs(0,ed,visitNodes|{n-1}, set())
//     return straight + (al-straight)*2

int dfs(int start, vector<vector<int> > &edges, set<int> &visitNodes, set<int> &visited) {
    // cout << "did a single one" << endl;
    int tot_dist = 0;
    visited.insert(start);
    for (auto v = edges[start].begin(); v != edges[start].end(); v++){
        if (!visited.count(*v)){
            int relevant_distance = dfs(*v, edges, visitNodes, visited);
            if (relevant_distance > 0 || visitNodes.count(*v)){
                tot_dist += relevant_distance + 1;
            }
        }
    }
    // cout << start << "," << tot_dist << endl;
    return tot_dist;
}

int findMinimumPathLength(int n, vector<vector<int>> edges, vector<int> visitNodes) {
    vector<vector<int> > ed(n);
    set<int> visitNodeSet;
    for(int i = 0; i < visitNodes.size(); i++) {
        visitNodeSet.insert(visitNodes[i]-1);
    }
    visitNodeSet.insert(n-1);
    for(int i =0; i < edges.size(); i++){
        int u = edges[i][0];
        int v = edges[i][1];
        ed[u-1].push_back(v-1);
        ed[v-1].push_back(u-1);
    }
    // cout << "Made it here" << endl;
    set<int> a{n-1};
    set<int> b{};
    int straight = dfs(0, ed, a, b);
    // cout << "and here" << endl;
    set<int> c{};
    int al = dfs(0,ed,visitNodeSet, c);
    return straight + (al-straight)*2;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string edges_rows_temp;
    getline(cin, edges_rows_temp);

    int edges_rows = stoi(ltrim(rtrim(edges_rows_temp)));

    string edges_columns_temp;
    getline(cin, edges_columns_temp);

    int edges_columns = stoi(ltrim(rtrim(edges_columns_temp)));

    vector<vector<int>> edges(edges_rows);

    for (int i = 0; i < edges_rows; i++) {
        edges[i].resize(edges_columns);

        string edges_row_temp_temp;
        getline(cin, edges_row_temp_temp);

        vector<string> edges_row_temp = split(rtrim(edges_row_temp_temp));

        for (int j = 0; j < edges_columns; j++) {
            int edges_row_item = stoi(edges_row_temp[j]);

            edges[i][j] = edges_row_item;
        }
    }

    string visitNodes_count_temp;
    getline(cin, visitNodes_count_temp);

    int visitNodes_count = stoi(ltrim(rtrim(visitNodes_count_temp)));

    vector<int> visitNodes(visitNodes_count);

    for (int i = 0; i < visitNodes_count; i++) {
        string visitNodes_item_temp;
        getline(cin, visitNodes_item_temp);

        int visitNodes_item = stoi(ltrim(rtrim(visitNodes_item_temp)));

        visitNodes[i] = visitNodes_item;
    }

    int result = findMinimumPathLength(n, edges, visitNodes);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
