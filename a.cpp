#include <bits/stdc++.h>
using namespace std;

int main() {
    long long a, b, x;
    cin >> a >> b >> x;
    if (a >= b) {
        cout << 0 << endl;
    } else {
        long long res = (b - a + x - 1) / x;
        cout << res;
    }

    return 0;
}
