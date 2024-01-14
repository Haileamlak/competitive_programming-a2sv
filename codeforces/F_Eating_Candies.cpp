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
        vector<int> nums(n);
        for (int i = 0; i < n; i++)
            cin >> nums[i];

        int left = 0, right = n - 1;
        int res = 0;
        int lsum = nums[0];
        int rsum = nums[n - 1];
        while (left < right)
        {
            if (lsum == rsum)
                res = left + 1 + n - right;
            if (lsum <= rsum)
                lsum += nums[++left];
            else
                rsum += nums[--right];
        }
        cout << res << '\n';
    }
    return 0;
}