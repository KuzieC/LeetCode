#include <vector>

class UF {
private:
    std::vector<int> parent;
    int count;

public:
    UF(int n) {
        parent.resize(n);
        count = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void connect(int a, int b) {
        int par_a = find(a);
        int par_b = find(b);
        if (par_a != par_b) {
            parent[par_a] = par_b;
            count--;
        }
    }

    bool connected(int a, int b) {
        return find(a) == find(b);
    }

    int get() {
        return count;
    }
};