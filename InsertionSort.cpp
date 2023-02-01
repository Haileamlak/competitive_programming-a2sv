void insertionSort1(int n, vector<int> arr) {
    int temp = arr[n-1];
    bool found = false;
    for (int i = n - 2; i >= -1 && !found; i--)
    {
        if (i == -1)
            arr[0] = temp;
        if (arr[i] < temp){
            arr[i + 1] = temp;
            found = true;
        }
        else arr[i+1] = arr[i];
        for(int i=0;i<n;i++)
            cout<<arr[i]<<" ";
        cout<<endl;
    }
}
