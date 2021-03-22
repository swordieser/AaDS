#include <iostream>
#include <fstream>
#include <vector>
#include <cfloat>
#include <cmath>
#include <iomanip>

using namespace std;

vector<pair<int, int>> graph;
vector<double> range;
vector<bool> visited;
vector<int> path;
int n;

double countWeight(int a, int b) {
    return sqrt((graph.at(b).first - graph.at(a).first) * (graph.at(b).first - graph.at(a).first) +
                (graph.at(b).second - graph.at(a).second) * (graph.at(b).second - graph.at(a).second));
}

int main() {
    ifstream fin("spantree.in");
    ofstream fout("spantree.out");

    fin >> n;
    graph.resize(n);
    range.assign(n, DBL_MAX);
    visited.assign(n, false);
    path.resize(n, -1);
    double answer = 0;

    int x, y;
    for (int i = 0; i < n; i++) {
        fin >> x >> y;
        graph.at(i).first = x;
        graph.at(i).second = y;
    }

    range.at(0) = 0;
    for (int i = 0; i < n; i++) {
        int v = -1;
        for (int j = 0; j < n; j++) {
            if (!visited.at(j) && (v == -1 || range.at(j) < range.at(v))) {
                v = j;
            }
        }
        visited.at(v) = true;
        if (path.at(v) != -1) {
            answer += countWeight(v, path.at(v));
        }
        for (int next = 0; next < n; next++) {
            if (countWeight(v, next) < range.at(next)) {
                range.at(next) = countWeight(v, next);
                path.at(next) = v;
            }
        }
    }

    fout << setprecision(10) << answer;
    return 0;
}