#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];

        sort(a.begin(), a.end());
        int cost = 0;
        int i = 0, j = n - 1;
        for (int i = 0, j = n - 1; i < j; i++, j--)
            cost += a[j] - a[i];

        cout << cost << endl;
    }
    return 0;
}