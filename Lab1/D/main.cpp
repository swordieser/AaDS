#include <fstream>
#include <vector>

using namespace std;

void dfs(int list, int counter, vector<vector<int>> &adjacency_matrix, vector<int> &visited) {
    visited.at(list) = counter;
    if (!adjacency_matrix.at(list).empty()) {
        for (auto iterator = adjacency_matrix.at(list).begin();
             iterator != adjacency_matrix.at(list).end();
             iterator++) {
            if (visited.at(*iterator) == 0)
                dfs(*iterator, counter, adjacency_matrix, visited);
        }
    }
}

int main() {
    ifstream fin("components.in");
    ofstream fout("components.out");
    int n, m, a, b;
    fin >> n >> m;
    vector<vector<int>> adjacency_matrix(n, vector<int>(0));
    vector<int> visited(n, 0);
    for (int i = 0; i < m; i++) {
        fin >> a >> b;
        adjacency_matrix.at(a - 1).push_back(b - 1);
        adjacency_matrix.at(b - 1).push_back(a - 1);
    }

    int counter = 1;
    for (int i = 0; i < n; i++) {
        if (visited.at(i) == 0) {
            dfs(i, counter, adjacency_matrix, visited);
            counter++;
        }
    }
    fout << counter - 1 << "\n";
    for (int i = 0; i < n; i++)
        fout << visited.at(i) << " ";
}
