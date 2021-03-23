#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <iomanip>

using namespace std;

int main() {
    ifstream fin("spantree3.in");
    ofstream fout("spantree3.out");
    int n, m, a, b;
    double w;
    fin >> n >> m;
    vector<bool> used(n);
    vector<vector<pair<double, int>>> g(n);
    for (int i = 0; i < m; i++) {
        fin >> a >> b >> w;
        g.at(a - 1).push_back(make_pair(w, b - 1));
        g.at(b - 1).push_back(make_pair(w, a - 1));
    }
    double answer = 0;
    priority_queue<pair<double, int>, vector<pair<double, int>>, greater<>> q;
    q.push({0, 0});
    while (!q.empty()) {
        auto c = q.top();
        q.pop();
        double weight = c.first;
        int v = c.second;
        if (used.at(v))
            continue;
        used.at(v) = true;
        answer += weight;
        for (auto e: g.at(v)) {
            if (!used.at(e.second)) {
                q.push(e);
            }
        }
    }
    fout << setprecision(10) << answer;
}