#include <iostream>

using namespace std;

int main()
{
    int k, n, w;
    cin >> k >> n >> w;
    int x = w * (w + 1) / 2 * k;
    if (n >= x)
        cout << 0;
    else
        cout << x - n;
    return 0;
}