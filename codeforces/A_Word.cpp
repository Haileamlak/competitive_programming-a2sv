#include <iostream>

using namespace std;

int main()
{
    string a;
    cin >> a;
    int low = 0;
    int up = 0;
    for (char ch : a)
    {
        if (ch > 93)
        {
            low++;
        }
        else
            up++;
    }

    if (low >= up)
    {
        for (char ch : a)
        {
            cout << tolower(ch);
        }
    }
    else
    {
        for (char ch : a)
        {
            cout << toupper(ch);
        }
    }
    return 0;
}