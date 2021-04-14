#include <iostream>
#include <fstream>
#include <vector>
#include <set>


using namespace std;

struct Edge {
    int to;
    long long w;
};

const long long infinity = 2e16;

void dijkstra(vector<long long> &dist, vector<bool> &used, vector<vector<Edge>> &graph, set<pair<long long, int>> &set,
              int start) {
    dist.at(start) = 0;
    set.insert(make_pair(dist.at(start), start));
    while (!set.empty()) {
        int v = set.begin()->second;
        set.erase(set.begin());
        for (int i = 0; i < graph.at(v).size(); i++) {
            if (dist.at(v) + graph.at(v).at(i).w < dist.at(graph.at(v).at(i).to)) {
                set.erase(make_pair(graph.at(v).at(i).w, graph.at(v).at(i).to));
                dist.at(graph.at(v).at(i).to) = dist.at(v) + graph.at(v).at(i).w;
                set.insert(make_pair(dist.at(graph.at(v).at(i).to), graph.at(v).at(i).to));
            }
        }
    }
}

int main() {
    ifstream fin("pathbgep.in");
    ofstream fout("pathbgep.out");

    int n, m;
    vector<vector<Edge>> graph;
    vector<long long> dist;
    vector<bool> used;

    fin >> n >> m;

    graph.resize(n);
    dist.resize(n, infinity);
    used.resize(n, false);
    set<pair<long long, int>> set;

    int from, to;
    long long weight;

    for (int i = 0; i < m; i++) {
        fin >> from >> to >> weight;
        from--;
        to--;
        Edge edge_first{to, weight};
        graph.at(from).push_back(edge_first);
        Edge edge_second{from, weight};
        graph.at(to).push_back(edge_second);
    }

    dijkstra(dist, used, graph, set, 0);

    for (auto &d : dist) {
        fout << d << " ";
    }
    fout << endl;

}