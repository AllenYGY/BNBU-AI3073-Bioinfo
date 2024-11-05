#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

struct Interval {
    int left;
    int right;
    int weight;
};

// Comparator to sort intervals by right endpoint
bool compare(const Interval &a, const Interval &b) {
    return a.right < b.right;
}

pair<vector<int>, vector<Interval>> ExonChaining(const vector<Interval> &G, int n) {
    vector<int> s(2 * n + 1, 0);
    vector<vector<Interval>> selected_intervals(2 * n + 1);  // Records the selected intervals for each endpoint

    // Collect and sort all unique endpoints
    vector<int> endpoints;
    for (const auto &interval : G) {
        endpoints.push_back(interval.left);
        endpoints.push_back(interval.right);
    }
    sort(endpoints.begin(), endpoints.end());
    endpoints.erase(unique(endpoints.begin(), endpoints.end()), endpoints.end());  // Remove duplicates

    // Map each endpoint to its index
    map<int, int> endpoint_index;
    for (int i = 0; i < endpoints.size(); i++) {
        endpoint_index[endpoints[i]] = i + 1;
    }

    // Convert intervals using mapped indices
    vector<tuple<int, int, int>> intervals;
    for (const auto &interval : G) {
        intervals.emplace_back(endpoint_index[interval.left], endpoint_index[interval.right], interval.weight);
    }

    // Dynamic programming to find the maximum weight and selected intervals
    for (int i = 1; i <= endpoints.size(); i++) {
        // Collect intervals ending at current endpoint
        vector<tuple<int, int, int>> right_intervals;
        for (const auto &interval : intervals) {
            if (get<1>(interval) == i) {
                right_intervals.push_back(interval);
            }
        }

        if (!right_intervals.empty()) {
            for (const auto &[l, r, w] : right_intervals) {
                if (s[i] < s[l] + w) {
                    s[i] = s[l] + w;
                    selected_intervals[i] = selected_intervals[l];
                    selected_intervals[i].emplace_back(Interval{endpoints[l - 1], endpoints[r - 1], w});
                }
            }
        } else {
            // If no intervals are chosen, inherit from the previous endpoint
            s[i] = s[i - 1];
            selected_intervals[i] = selected_intervals[i - 1];
        }
    }

    // Return the maximum weight and the selected intervals for the last endpoint
    return {s, selected_intervals[endpoints.size()]};
}

int main() {
    vector<Interval> G2 = {
        {1, 5, 4},
        {2, 3, 5},
        {4, 8, 11},
        {6, 12, 8},
        {7, 17, 9},
        {9, 10, 0},
        {11, 15, 6},
        {13, 14, 3},
        {16, 18, 2}
    };

    auto [s, selected] = ExonChaining(G2, G2.size());
    cout << "最大不重叠区间的总权重为: " << s.back() << endl;
    cout << "选择的区间为:" << endl;
    for (const auto &interval : selected) {
        cout << "(" << interval.left << ", " << interval.right << ", " << interval.weight << ")" << endl;
    }

    return 0;
}