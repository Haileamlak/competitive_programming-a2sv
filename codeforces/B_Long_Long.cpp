#include <iostream>
#include <vector>

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

        int res = 0;
        long long sum = 0;
        for (int i = 0; i < n;)
        {
            if (a[i] < 0)
            {
                while (i < n && a[i] <= 0)
                {
                    sum += abs(a[i]);
                    i++;
                }
                res++;
            }
            else
            {
                sum += a[i];
                i++;
            }
        }
        cout << sum << ' ' << res << '\n';
    }
    return 0;
}