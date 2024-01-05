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

    int first = 0;
    for (int second = 0; second < m; second++)
    {
        while (first < n && b[second] > a[first])
            first++;

        cout << first << " ";
    }
    return 0;
}