#include<iostream>
using namespace std;

void deleteElement(int n, int arr[], int pos)
{
    // Check if the array is empty
    if(n == 0)
    {
        cout << "Array is empty. Cannot delete an element.";
        return;
    }

    // Check if the position is invalid
    if(pos < 1 || pos > n)
    {
        cout << "Invalid position!";
        return;
    }

    // Convert position to array index
    pos = pos - 1;

    // Shift elements to the left
    for(int i = pos; i < n - 1; i++)
    {
        arr[i] = arr[i + 1];
    }

    // Reduce the number of elements
    n--;

    cout << "After deleting the element, the new array is:\n";

    // Display the updated array
    for(int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    int n, pos;

    // Get the number of elements
    cout << "Enter the array size: ";
    cin >> n;

    int arr[50];

    // Check whether the size is valid
    if(n < 0 || n > 50)
    {
        cout << "Invalid array size!";
        return 0;
    }

    // Get array elements
    for(int i = 0; i < n; i++)
    {
        cout << "Enter element " << i + 1 << ": ";
        cin >> arr[i];
    }

    // Get the position to delete
    cout << "Enter the position to delete (starting from 1): ";
    cin >> pos;

    // Call the delete function
    deleteElement(n, arr, pos);

    return 0;
}
