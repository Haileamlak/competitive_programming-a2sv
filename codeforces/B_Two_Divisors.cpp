#include <iostream>

using namespace std;
int gcd(int a, int b)
{
    // Find Minimum of a and b
    int result = min(a, b);
    while (result > 0)
    {
        if (a % result == 0 && b % result == 0)
        {
            break;
        }
        result--;
    }

    // Return gcd of a and b
    return result;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {

        int a, b;
        cin >> a >> b;
        // if (b % )
        int nm = gcd(a, b);
        if (a == 1)
        {
            cout << b * 2 << "\n";
        }
        else if (b % a == 0)
        {
            cout << 2 * b << "\n";
        }
        else if (nm > 1)
        {
            cout << ((b * a) / nm) << "\n";
        }
        else
        {
            cout << a * b << "\n";
        }
    }
    return 0;
}