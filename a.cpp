#include <iostream>
using namespace std;

int main() {
    long long k, n = 0, c = 0;
    cin >> k;
    while (c < k) {
        n++;
        if (n % 3 != 0 && n % 10 != 3) c++;
    }
    cout << n;

    return 0;
}