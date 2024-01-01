#include <bits/stdc++.h>

using namespace std;

int solve(vector<string> &temp)
{
    int n = temp.size();
    vector<vector<int>> score(5, vector<int> (n));
    string chars = "abcde";
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < n; j++)
        {
            score[i][j] = 2 * count(temp[j].begin(), temp[j].end(), chars[i]) - temp[j].size();
        }
        sort(score[i].begin(), score[i].end());
    }

    vector<int> total_score(5);
    for (int i = 0; i < 5; i++)
    {
        int curr = 0;
        for (int j = 0; j < n; j++)
        {
            curr += score[i][j];
        }
        total_score[i] = curr;
    }



    for (int i = 0; i < n; i++)
    {

        for (int j = 0; j < 5; j++)
        {
            if (total_score[j] > 0){
                return n - i;
            }
            total_score[j] -= score[j][i];
        }

    }
    return 0;

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
        int n;
        cin >> n;
        vector<string> a(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        cout<<solve(a)<<"\n";
    }
    return 0;
}
