#include <iostream>
#include <vector>
#include<cmath>

using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    std::cout.sync_with_stdio(0);
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    vector<int> b(m);
    for (int i = 0; i < m; i++)
        cin >> b[i];

    int top = 0, bottom = 0;
    int res = 0;
    // int k = int(pow(10, 9) + 7);
    while (top < n && bottom < m)
    {
        if (a[top] == b[bottom])
        {
            top++;
            bottom++;
            int i = 1, j = 1;
            while (top < n && a[top] == a[top - 1])
            {
                i++;
                top++;
            }
            while (bottom < m && b[bottom] == b[bottom - 1])
            {
                bottom++;
                j++;
            }
            res += ((i % INT_MAX) * (j % INT_MAX)) % INT_MAX;
            res %= INT_MAX;
        }
        else if (a[top] < b[bottom])
            top++;
        else
            bottom++;
    }
    std::cout << res % INT_MAX;
    return 0;
}