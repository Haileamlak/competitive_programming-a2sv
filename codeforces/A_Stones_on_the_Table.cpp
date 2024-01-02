#include <iostream>

using namespace std;

int main()
{
    int n;
    
    string a;
    cin >>n>> a;
    int cnt = 0;
    int res = 0;
    for (int i = 1; i < n; i++)
    {
        if (a[i] == a[i - 1])
            cnt++;
        else
        {
            res += cnt;
            cnt = 0;
        }
    }

    res += cnt;
    cout << res;
    return 0;
}