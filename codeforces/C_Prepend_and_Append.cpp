#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        string binary;
        cin >> n >> binary;
        int i = 0, j = n - 1;
        while (i < j)
        {

            if (binary[i] != binary[j])
            {
                i++;
                j--;
            }
            else
                break;
        }
    
        cout << j - i + 1 << "\n";
    }
    return 0;
}