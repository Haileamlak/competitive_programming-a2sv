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
        vector<int> arr(n);
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        auto sorted = arr;
        sort(sorted.begin(), sorted.end());
        string res = "YES";
        for (int i = 0; i < n; i++)
        {
            if (arr[i] % 2 == 0 && sorted[i] % 2 != 0)
            {
                res = "NO";
                break;
            }
            else if (arr[i] % 2 != 0 && sorted[i] % 2 == 0)
            {
                res = "NO";
                break;
            }
        }
        cout << res << '\n';
    }
    return 0;
}