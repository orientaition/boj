#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i=0; i<(n); ++i)
#define REP(i, a, b) for(int i=(a); i<(b); ++i)
#define all(v) (v).begin(), (v).end()
#define SIZE(v) ((int)(v).size())
typedef long long lld;
typedef pair<int, int> ii;
typedef pair<lld, lld> ll;

const int INF = 0x3f3f3f3f;
const lld LNF = 0x3f3f3f3f3f3f3f3f;
const int MOD = 1e9 + 7;

static int dy[] = { -1,0,1,0 };
static int dx[] = { 0,-1,0,1 };

struct node {
    lld val;
    node* left, *right;

    node(node* left = NULL, node* right = NULL) :
        left(left), right(right), val(0) {
    }

    // [l, r]
    node* insert(int l, int r, int w, lld val) {
        if (l <= w && w <= r) {
            // With in the range, we need a new node
            if (l == r) {
                node* leaf = new node();
                leaf->val = this->val + val;
                return leaf;
            }
            int m = (l + r) >> 1;
            node* cl = this->left->insert(l, m, w, val);
            node* cr = this->right->insert(m + 1, r, w, val);
            node* leaf = new node(cl, cr);
            leaf->val = cl->val + cr->val;
            return leaf;
        }
        // Out of range, we can use previous tree node.
        return this;
    }
};

// searching [l, r]
// node means: range [s, e]
lld query(node* p, int s, int e, int l, int r) {
    if (e < l || r < s) return 0;
    if (l <= s && e <= r) return p->val;
    int m = (s + e) >> 1;
    lld ans = 0;
    ans += query(p->left, s, m, l, r);
    ans += query(p->right, m + 1, e, l, r);
    return ans;
}

#define MAX_SIZE 100005
int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        scanf("%d %d", &n, &m);
        vector<int> xpos[MAX_SIZE];
        for (int i = 0; i < n; ++i) {
            int y, x;
            scanf("%d %d", &x, &y);
            y++, x++; // [0...n] -> [1...n+1]
            xpos[y].push_back(x);
        }

        vector<node*> t(MAX_SIZE + 2);
        t[0] = new node();
        t[0]->left = t[0]->right = t[0];
        t[0]->val = 0;

        for (int y = 1; y < MAX_SIZE; ++y) {
            t[y] = t[y - 1];
            for (auto& x : xpos[y]) {
                t[y] = t[y]->insert(1, MAX_SIZE, x, 1);
            }
        }

        lld ans = 0;
        while (m--) {
            int l, r, b, u;
            scanf("%d %d %d %d", &l, &r, &b, &u);
            l++, r++, b++, u++;
            ans += query(t[u], 1, MAX_SIZE, l, r);
            ans -= query(t[b - 1], 1, MAX_SIZE, l, r);
        }
        printf("%lld\n", ans);
    }

    return 0;
}