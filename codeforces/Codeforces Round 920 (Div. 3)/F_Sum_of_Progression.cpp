#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, q;
        cin >> n >> q;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];

        vector<vector<int>> pre(n - 1);
        for (int i = 1; i < n; i++)
        {
            pre[i] = vector<int>(i);
            pre[i][0] = a[0];
        }

        for (int i = 1; i < n - 1; i++)
        {

            for (int j = 1; j <= i; j++)
            {
                pre[j][i - 1] = pre[j][i - 2] + a[i - 1];
            }
            // pre[i] = temp;
        }
        int s, d, k;
        for (int i = 0; i < q; i++)
        {
            cin >> s >> d >> k;
            cout << pre[d][k - 1] << ' ';
        }
        cout << '\n';
    }
    return 0;
}