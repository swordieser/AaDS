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
    dist.at(start) = 0;
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
    ifstream fin("pathsg.in");
    ofstream fout("pathsg.out");

    int n, m;
    vector<vector<Edge>> graph;
    vector<long long> dist;
    vector<bool> used;

    fin >> n >> m;

    graph.resize(n);
    dist.resize(n, infinity);
    used.resize(n, false);


    int from, to;
    long long weight;
    Edge edge{};

    for (int i = 0; i < m; i++) {
        fin >> from >> to >> weight;
        from--;
        to--;
        edge.to = to;
        edge.w = weight;
        graph.at(from).push_back(edge);
    }

    for (int i = 0; i < n; i++){
        dist.assign(n, infinity);
        used.assign(n, false);
        dijkstra(dist, used, graph, i, n);
        for (auto &d : dist){
            fout << d << " ";
        }
        fout << endl;
    }
}