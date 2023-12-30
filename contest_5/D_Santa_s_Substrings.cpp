#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compareByLength(const std::string &a, const std::string &b)
{
    return a.length() < b.length();
}
int main()
{
    int n;
    cin >> n;
    vector<string> temp(n);
    int i = 0;
    while (i < n)
    {
        cin >> temp[i];
        i++;
    }
    sort(temp.begin(), temp.end(), compareByLength);

    bool fal = false;
    for (int i = 0; i < n - 1; i++)
    {
        int idx = temp[n - 1].find(temp[i]);
        if (idx == string::npos)
        {
            fal = true;
            break;
        }
    }
    if (fal)
        cout << "NO\n";
    else
    {
        cout << "YES\n";
        for (int i = 0; i < n ; i++)
        {
            cout << temp[i] << "\n";
        }
    }

    return 0;
}