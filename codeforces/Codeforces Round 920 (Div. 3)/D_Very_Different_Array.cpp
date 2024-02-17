#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    cout.sync_with_stdio(0);
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];
        vector<int> b(m);
        for (int i = 0; i < m; i++)
            cin >> b[i];

        sort(a.begin(), a.end());
        sort(b.begin(), b.end(), greater<int>());

        int l1 = 0, l2 = 0;
        int r1 = n - 1, r2 = m - 1;
        long long res = 0;
        while (l1 <= l2)
        {   
                int temp = abs(a[l1] - b[l2]);
                if (abs(a[l1] - b[l2]) > abs(a[r1] - b[l2]) && abs(a[l1] - b[l2]) > abs(a[r1] - b[r2]) && abs(a[l1] - b[l2]) > abs(a[l1] - b[l2]))
                {
                    if (abs(a[l1] - b[r2]) > abs(a[r1] - b[r2]))
                    {
                        res += abs(a[l1] - b[r2]);
                        l1++;
                        r2--;
                    }
                    else
                    {
                        res += abs(a[r1] - b[r2]);
                        r1--;
                    }

                    res += abs(b[l] - a[i]);
                    l++;
            }
            else
            {
                res += abs(b[r] - a[i]);
                r--;
            }
        }
        cout << res << '\n';
    }
    return 0;
}