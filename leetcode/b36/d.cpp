// legitimately an interesting problem for me!  good job, leetcode.

class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        vector<pair<int, pair<int, int>>> events;
        // events a vector of (time, (is_start, request_num))
        // is_start is 0 if it's a start event, 1 otherwise.
        for (int i = 0; i < arrival.size(); i++ ) {
            events.push_back(make_pair(arrival[i], make_pair(1, i)));
            events.push_back(make_pair(arrival[i]+load[i], make_pair(0, i)));
        }
        // counts[i] is how many times server i served a request (used to find the answer at the end)
        // serverforreq[i] stores which server was used for request i (-1 if not served)
        // availableservers is a BST that stores all currently free servers;
        vector<int> counts(k, 0);
        vector<int> serverforreq(arrival.size(), -1);
        set<int> availableservers;
        for(int i = 0; i < k; i++) {
            availableservers.insert(i);
        }
        sort(events.begin(), events.end());
        for (int i = 0; i < events.size(); i++) {
            int t = events[i].first;
            int type = events[i].second.first;
            int r = events[i].second.second;
            // cout << t << " " << type << " " << r << endl;
            if (type == 1){
                if (availableservers.empty()) {
                    continue;
                }
                int rr = r%k;
                auto it = availableservers.lower_bound(rr);
                if (it == availableservers.end()) {
                    it = availableservers.begin();
                }
                counts[*it]++;
                serverforreq[r] = *it;
                availableservers.erase(it);
            } else {
                if (serverforreq[r] == -1) {
                    continue;
                }
                availableservers.insert(serverforreq[r]);
            }
        }
        vector<int>ans;
        int best = 0;
        for (int i = 0; i < counts.size(); i++) {
            // cout << counts[i] << " ";
            if (counts[i] > best) {
                ans.clear();
                ans.push_back(i);
                best = counts[i];
            } else if (counts[i] == best){
                ans.push_back(i);
            }
        }
        return ans;
    }
};