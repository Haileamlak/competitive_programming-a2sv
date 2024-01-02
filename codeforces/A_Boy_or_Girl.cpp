#include <iostream>
#include <unordered_set>

using namespace std;

int main()
{
    string a;
    cin >> a;
    unordered_set<char> aa;
    for (auto ch : a)
    {
        aa.insert(ch);
    }
    if (aa.size() % 2 == 1)
        cout << "IGNORE HIM!";
    else
        cout << "CHAT WITH HER!";
    return 0;
}