#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


using namespace std;

struct Edge {
    int from, to;
    long long w;
};

bool negative_cycle(vector<Edge> &graph, vector<long long> &dist, vector<int> &parent, vector<int> &answer, int n) {
    int x;
    for (int i = 0; i < n; i++) {
        x = -1;
        for (auto edge : graph) {
            if (dist.at(edge.from) + edge.w < dist.at(edge.to)) {
                dist.at(edge.to) = dist.at(edge.from) + edge.w;
                parent.at(edge.to) = edge.from;
                x = edge.to;
            }
        }
    }

    if (x == -1) {
        return false;
    } else {
        int v = x;
        for (int i = 0; i < n; i++) {
            v = parent.at(v);
        }

        for (int u = v;; u = parent.at(u)) {
            answer.push_back(u);
            if (u == v && answer.size() > 1) break;
        }

        reverse(answer.begin(), answer.end());
        return true;
    }
}


int main() {
    ifstream fin("negcycle.in");
    ofstream fout("negcycle.out");

    int n;
    vector<Edge> graph;
    vector<long long> dist;
    vector<int> parent;
    vector<int> answer;
    Edge edge{};
    long long w;

    fin >> n;

    dist.resize(n, 1);
    parent.resize(n, -1);

    dist.at(0) = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            fin >> w;
            if (w != 1e9) {
                edge.from = i;
                edge.to = j;
                edge.w = w;
                graph.push_back(edge);
            }
        }
    }

    if (negative_cycle(graph, dist, parent, answer, n)) {
        fout << "YES\n" << answer.size() << '\n';
        for (auto ans : answer) {
            fout << ans + 1 << ' ';
        }
    } else {
        fout << "NO";
    }
}