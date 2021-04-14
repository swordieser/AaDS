#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

struct Edge {
    int to;
    long long w;
};

const long long infinity = 2e16;

void dijkstra(vector<long long> &dist, vector<bool> &used, vector<vector<Edge>> &graph, int start, int n) {
    dist.at(start - 1) = 0;
    for (int i = 0; i < n; i++) {
        int v = -1;
        for (int j = 0; j < n; j++) {
            if (!used.at(j) && (v == -1 || dist.at(j) < dist.at(v))) {
                v = j;
            }
        }

        if (dist.at(v) == infinity) break;

        used.at(v) = true;

        for (int j = 0; j < graph.at(v).size(); ++j) {
            if (dist[v] + graph.at(v).at(j).w < dist[graph.at(v).at(j).to]) {
                dist[graph.at(v).at(j).to] = dist[v] + graph.at(v).at(j).w;
            }
        }
    }
}

int main() {
    ifstream fin("pathmgep.in");
    ofstream fout("pathmgep.out");

    int n, s, f;
    vector<vector<Edge>> graph;
    vector<long long> dist;
    vector<bool> used;

    fin >> n >> s >> f;

    graph.resize(n);
    dist.resize(n, infinity);
    used.resize(n, false);

    int temp;
    Edge edge{};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            fin >> temp;
            if (temp != -1 && i != j) {
                edge.to = j;
                edge.w = temp;
                graph.at(i).push_back(edge);
            }
        }
    }

    dijkstra(dist, used, graph, s, n);

    if (dist.at(f - 1) != infinity) fout << dist.at(f - 1);
    else fout << -1;
}