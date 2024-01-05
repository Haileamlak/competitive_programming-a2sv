#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        string paper;
        cin >> n >> k >> paper;
        int i = 0;
        int res = 0;
        while (i < n){
            if (paper[i] == 'W')
                i++;
            else{
                i += k;
                res += 1;
            }
        }

        cout << res << "\n";
    }
    return 0;
}