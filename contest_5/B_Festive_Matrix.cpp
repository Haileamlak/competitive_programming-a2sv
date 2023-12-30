#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> arr(n);
    vector<int> temp(n);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> temp[j];
        }
        arr[i] = temp;
    }
 
    int good = 0;
    int end = (n - 1) / 2;
    for (int i = 0; i < n; i++)
    {
        good += arr[i][i];
    }
    for (int i = 0; i < n; i++)
    {
        good += arr[i][n - i - 1];
    }

    for (int i = 0; i < n; i++)
    {
        good += arr[i][end];
    }
    for (int i = 0; i < n; i++)
    {
        good += arr[end][i];
    }
    good -= 3 * arr[end][end];
    cout << good;
    return 0;
}