vector<int> countingSort(vector<int> arr)
{
    vector<int> newArr(100);
    int size = arr.size();
    for (size_t i = 0;i < size; i++)
    {
        newArr[arr[i]]++;
    }
    return newArr;
}
