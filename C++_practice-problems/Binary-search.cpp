// Note: For binary search elements should be sorted
#include <iostream>
using namespace std;
#include<algorithm>

int binarySearch(int arr[], int n, int target)
{
    int low = 0;
    int high = n - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;

        if (arr[mid] == target)
        {
            return mid;
        }
        else if (target > arr[mid])
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return -1;
}

int main()
{
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];

    cout << "Enter elements in sorted order: ";

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr+n);  //suppose the user have enter in some random order

    int target;

    cout << "Enter target: ";
    cin >> target;

    int result = binarySearch(arr, n, target);

    if (result != -1)
    {
        cout << "Element found at index: " << result;
    }
    else
    {
        cout << "Element not found";
    }

    return 0;
}
