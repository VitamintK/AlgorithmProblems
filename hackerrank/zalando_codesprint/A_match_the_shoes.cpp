#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool comparePairs(const std::pair<long long, long long>& lhs, const std::pair<long long, long long>& rhs)
{
  return lhs.second > rhs.second || (lhs.second == rhs.second && lhs.first < rhs.first);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    long long K, N, M, A;
    cin >> K >> M >> N;
    pair<long long, long long> shoes[50001];
    for(long long i = 0; i < M; i++){
        shoes[i].first = i;
        shoes[i].second = 0ll;
    }
    for(long long i = 0; i < N; i++){
        cin >> A;
        shoes[A].second++;
    }
    sort(shoes, shoes+M, comparePairs);
    for(long long i = 0; i < K; i++){
        cout << shoes[i].first << endl;
    }
    return 0;
}
