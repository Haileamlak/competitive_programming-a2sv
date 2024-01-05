#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int left = 0, right = n - 1;
    int dima = 0, sereja = 0;

    bool isSereja = true;
    while (left <= right)
    {
        if (isSereja)
        {
            if (arr[left] > arr[right])
                sereja += arr[left++];
            else
                sereja += arr[right--];
        }
        else
        {
            if (arr[left] > arr[right])
                dima += arr[left++];
            else
                dima += arr[right--];
        }
        isSereja = !isSereja;
    }
    cout << sereja << ' ' << dima;
    return 0;
}