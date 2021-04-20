#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

const int INF = 1e9;


int main() {
    int n;
    cin >> n;
    vector<int> sequence;
    int a;
    for (int i = 0; i < n; i++) {
        cin >> a;
        sequence.push_back(a);
    }

    vector<int> d(n + 1, INF);
    vector<int> pos(n + 1, 0);
    vector<int> prev(n, 0);
    int length = 0;
    pos.at(0) = -1;
    d.at(0) = -INF;

    for (int i = 0; i < n; i++) {
        int j = int(upper_bound(d.begin(), d.end(), sequence.at(i)) - d.begin());
        if ((d.at(j - 1) < sequence.at(i)) && (sequence.at(i) < d.at(j))) {
            d.at(j) = sequence.at(i);
            pos.at(j) = i;
            prev.at(i) = pos.at(j - 1);
            length = max(length, j);
        }
    }

    vector<int> answer;
    int p = pos.at(length);
    while (p != -1) {
        answer.push_back(sequence.at(p));
        p = prev.at(p);
    }

    reverse(answer.begin(), answer.end());
    cout << answer.size() << '\n';
    for (auto num: answer) {
        cout << num << ' ';
    }
}
