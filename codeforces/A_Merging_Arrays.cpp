#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    for (int i = 0; i < m; i++)
        cin >> b[i];

    vector<int> merged(n + m);
    int p1 = 0, p2 = 0;

    while (p1 < n && p2 < m)
    {
        if (a[p1] <= b[p2])
            cout << a[p1++] << " ";
        else
            cout << b[p2++] << " ";
    }
    while (p1 < n)
        cout << a[p1++] << " ";

    while (p2 < m)
        cout << b[p2++] << " ";

    return 0;
}