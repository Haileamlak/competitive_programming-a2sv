#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    string guest, host, letters;
    cin >> guest >> host >> letters;
    guest += host;
    sort(guest.begin(), guest.end());
    sort(letters.begin(), letters.end());
    if (guest == letters)
        cout << "YES";
    else
        cout<<"NO";
}