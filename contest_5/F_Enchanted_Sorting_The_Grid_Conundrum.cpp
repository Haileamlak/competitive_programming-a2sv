// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int main()
// {
//     int t, m, n;
//     cin >> t;
//     for (int i = 0; i < t; i++)
//     {
//         cin >> n >> m;
//         vector<vector<int>> nums(n);
//         vector<int> temp(n);
//         for (int j = 0; j < n; j++)
//         {
//             for (int k = 0; k < m; k++)
//             {
//                 cin >> temp[k];
//             }
//             nums[j] = temp;
//         }

//         vector<vector<int>> nums2 = nums;

//         sort(nums.begin(), nums.end());
//         vector<vector<int>> index(n);
//         vector<int> good(n);

//         bool cant = false;
//         int start = -1;
//         for (int j = 0; j < n; j++)
//         {
//             index[j] = {-1, -1};
//             bool yes1 = false;
//             bool yes2 = false;
//             for (int k = 0; k < m; k++)
//             {
//                 if (nums[j][k] != nums2[j][k])
//                 {
//                     if (!yes1)
//                     {
//                         yes1 = true;
//                         index[j][0] = k;
//                         good[j] = 1;
//                     }
//                     else if (!yes2)
//                     {
//                         yes2 = true;
//                         index[j][1] = k;
//                         good[j] = 1;
//                         start = j;
//                     }
//                     else
//                     {
//                         cant = true;
//                         break;
//                     }
//                 }
//             }
//             if (cant)
//                 break;
//         }
//         if (cant)
//         {
//             cout << -1 << '\n';
//         }
//         else
//         {
//             for (int i = 0; i < n; i++)
//             {
//                 if (good[i] == 1)
//                 {
//                     if (index[start][0] != index[i][0] || index[start][1] != index[i][1])
//                     {
//                         cant = true;
//                         break;
//                     }
//                 }
//             }
//             if (cant)
//             {
//                 cout << -1 << '\n';
//             }
//             else
//             {
//                 cout << index[start][0] << " " << index[start][1] << "\n";
//             }
//         }
//     }

//     return 0;
// }

// #include <bits/stdc++.h>

using namespace std;

void solve(vector<vector<int>> &a)
{
    int n = a.size(), m = a[0].size();
    vector<int> bad;
    for (int i = 0; i < n && bad.empty(); i++)
    {
        vector<int> b = a[i];
        sort(b.begin(), b.end());
        for (int j = 0; j < m; j++)
        {
            if (a[i][j] != b[j])
                bad.push_back(j);
        }
    }
    if ((int)bad.size() == 0)
    {
        cout << 1 << " " << 1 << "\n";
        return;
    }
    if ((int)bad.size() > 2)
    {
        cout << -1 << "\n";
        return;
    }
    for (int i = 0; i < n; i++)
    {
        swap(a[i][bad[0]], a[i][bad[1]]);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j < m; j++)
        {
            if (a[i][j] < a[i][j - 1])
            {
                cout << -1 << "\n";
                return;
            }
        }
    }
    cout << bad[0] + 1 << " " << bad[1] + 1 << "\n";
    return;
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
#endif
    int T;
    cin >> T;
    while (T--)
    {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> a(n, vector<int>(m));
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cin >> a[i][j];
            }
        }
        solve(a);
    }
    return 0;
}