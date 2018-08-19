#include <bits/stdc++.h>
#include <string>

	//NOTE TO SELF: BEFORE SUBMISSION: THINK ABOUT AN EDGE CASE PLEASE!


#define ll long long
#define ull unsigned long long
using namespace std;

int order_count;
vector<int> lc;
vector<int> rc;
vector<int> pre_order_to_node(2001); //order_to_node[i] gives the index of i-th node traversed
vector<int> post_order_to_node(2001);

void preorder(int node){
	pre_order_to_node[order_count] = node;
	//cout << node << " was visited at time " << order_count << endl;
	order_count++;
	if(lc[node]){
		preorder(lc[node]);
	}
	if(rc[node]){
		preorder(rc[node]);
	}
}

void postorder(int node){
	if(lc[node]){
		postorder(lc[node]);
	}
	if(rc[node]){
		postorder(rc[node]);
	}
	post_order_to_node[order_count] = node;
	order_count++;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int n, k;
		cin >> n >> k;
		lc.clear();
		rc.clear();
		lc.resize(n+1);
		rc.resize(n+1);

		//read in the tree input
		for(int i = 1; i <= n; i++){
			int l, r;
			cin >> l >> r;
			lc[i] = l;
			rc[i] = r;
		}
		//perform the traversals and record the orderings
		order_count = 0;
		preorder(1);
		order_count = 0;
		postorder(1);
		//make our "meta-graph" that denotes which pairs of nodes must have the same label
		vector<int> succ(n+1);
		for(int i = 0; i < n; i++){
			//cout << i << endl << pre_order_to_node[i] << " " << post_order_to_node[i] << endl;
			//we likely only need to do these edges in 1 direction.
			//cout << 
			succ[pre_order_to_node[i]] = post_order_to_node[i];
		}
		//find our equivalency classes/connected components in the meta-graph
		int num_of_classes = 0;
		vector<int> class_association(n+1, -1);
		vector<int> class_sizes;
		for(int i = 1; i <= n; i++){
			if(class_association[i] == -1){
				//find all the nodes belonging to this class
				int class_size = 1;
				class_association[i] = num_of_classes;
				for(int j = succ[i]; j != i; j = succ[j]){
					//cout << j << endl;
					class_size++;
					class_association[j] = num_of_classes;
				}
				class_sizes.push_back(class_size);
				num_of_classes++;
			}
		}
		//calculate answer.
		//for(int i = 0; i < class_sizes.size(); i++){
		//	cout << class_sizes[i] << endl;
		//}
		if(num_of_classes < k){
			cout << "Case #" << t+1 << ": Impossible" << endl;
		} else {
			cout << "Case #" << t+1 << ":";
			for(int i = 1; i <= n; i++){
				cout << " " << 1+class_association[i]%k;
			}
			cout << endl;
		}
	}
	return 0;
}