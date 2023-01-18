
void countSwaps(vector<int> a) {
    int sw=0;
    for (int i = 0; i < a.size(); i++) {
    
    for (int j = 0; j < a.size()-1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            sw++;
        }
    }
    
}
    cout<<"Array is sorted in "<<sw<<" swaps."<<endl;
    cout<<"First Element: "<<a[0]<<endl;
    cout<<"Last Element: "<<a[a.size()-1];
}
