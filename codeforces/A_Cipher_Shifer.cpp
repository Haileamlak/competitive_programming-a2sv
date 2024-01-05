#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        string word;
        cin >> n >> word;
        int count = 0;
        char temp;
        int i = 0;
        while (i < n)
        {
            temp = word[i++];
            cout << temp;
            while (word[i] != temp)
                i++;

            i++;
        }
        cout << "\n";
    }

    return 0;
}