#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int check_board(vector<vector<int>> board, int i, int N){
	int ans = 0;
	vector<map<int, int>> rows(N);
	vector<map<int, int>> cols(N);
	i <<= 1;
	for(int r = 0; r < N; r++){
		for(int c = 0; c < N; c++){
			i>>=1;
			if((i&1) != 0){
				ans+=1;
				continue;
			}
			rows[r][board[r][c]]+=1;
			cols[c][board[r][c]]+=1;
			if(rows[r][board[r][c]]>1){
				return -1;
			}
			if(cols[c][board[r][c]] > 1){
				return -1;
			}
		}
	}
	return ans;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int N;
		cin >> N;
		vector<vector<int> > board;
		for(int i = 0; i < N; i++){
			vector<int> row(N);
			for(int j = 0; j < N; j++){
				cin >> row[j];
			}
			board.push_back(row);
		}

		int ans = 1000;
		for(int i = 0; i < (1<<(N*N));i++){
			int check = check_board(board, i, N);
			if(check > -1){
				ans = min(ans, check);
			}
		}
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	
	return 0;
}