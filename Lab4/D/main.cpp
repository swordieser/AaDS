#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

struct Edge {
    int to;
    long long w;
};

const long long inf = 9e18;

void dfs_visit(vector<vector<Edge>> &graph, vector<bool> &used, int v) {
    used.at(v) = true;
    for (auto edge : graph.at(v)) {
        if (!used.at(edge.to)) {
            dfs_visit(graph, used, edge.to);
        }
    }
}

void dfs_negative(vector<vector<Edge>> &graph, vector<bool> &negative, int v) {
    negative.at(v) = true;
    for (auto edge : graph.at(v)) {
        if (!negative.at(edge.to)) {
            dfs_negative(graph, negative, edge.to);
        }
    }
}


void bellman_ford(vector<vector<Edge>> &graph, vector<long long> &dist, vector<bool> &used, vector<bool> &negative, int n, int v) {
    dist.at(v) = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (auto edge : graph.at(j)) {
                if (dist.at(edge.to) > dist.at(j) + edge.w) {
                    dist.at(edge.to) = max(-inf, dist.at(j) + edge.w);
                    if (i == n - 1 && used.at(edge.to)) {
                        dfs_negative(graph, negative, edge.to);
                    }
                }
            }
        }
    }
}

int main() {
    ifstream fin("path.in");
    ofstream fout("path.out");

    int n, m, v;
    vector<vector<Edge>> graph;
    vector<bool> used;
    vector<bool> negative;
    vector<long long> dist;
    Edge edge{};
    int from, to;
    long long w;

    fin >> n >> m >> v;

    graph.resize(n);
    used.resize(n, false);
    negative.resize(n, false);
    dist.resize(n, inf);

    for (int i = 0; i<m; i++){
        fin >> from >> to >> w;
        edge.to = --to;
        edge.w = w;
        graph.at(--from).push_back(edge);
    }

    dfs_visit(graph, used, --v);
    bellman_ford(graph, dist, used, negative, n, v);
    for (int i = 0; i< n; i++){
        if (negative.at(i) || dist.at(i) <= -inf){
            fout << "-\n";
        } else if (!used.at(i)) {
            fout << "*\n";
        } else {
            fout << dist.at(i) << '\n';
        }
    }

}