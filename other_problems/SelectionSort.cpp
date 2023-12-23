class Solution
{
public:
    int select(int arr[], int i)
    {
        return arr[i];
    }

    void selectionSort(int arr[], int n)
    {
        int index1;
        for (size_t i = 0; i < n; i++)
        {   
            index1 = i;
            for (size_t j = i + 1; j < n; j++)
                if (arr[j] < arr[index1])
                {
                    index1 = j;
                }
            swap(arr[i], arr[index1]);
        }
    }
};
