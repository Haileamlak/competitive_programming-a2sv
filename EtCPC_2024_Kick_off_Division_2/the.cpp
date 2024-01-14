#include <iostream>

using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    cout.sync_with_stdio(0);
    int res = 0;
    int n;
    cin >> n;
    long long alex;
    long long x;
    cin >> alex;
    for (int i = 1; i < n; i++)
    {
        cin >> x;
        if (x >= alex)
        {
            res++;
        }
    }
    cout << res;
    return 0;
}