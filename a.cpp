//these are my OI code -_-
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int x[3] = {a, b, c};
    auto mn = 1e9;
    int ans = 0;
    for (auto i = 0; i < 3; i++)
        for (auto j = 0; j < 3; j++)
            if (i != j) {
                auto p = x[i], q = x[j];
                auto g = gcd(p, q);
                p /= g; q /= g;
                auto v = (int)p / q;
                if (v < mn) {
                    mn = v;
                    ans = p + q;
                }
            }
    cout << ans;
}
