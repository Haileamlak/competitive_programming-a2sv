#include <iostream>

using namespace std;

int main()
{
    int a;

    cin >> a;
    int res = a / 5;
    a %= 5;
    // if(a > 0)
    cout << res + int(bool(a));
    // else
    //     cout << res;
    return 0;
}