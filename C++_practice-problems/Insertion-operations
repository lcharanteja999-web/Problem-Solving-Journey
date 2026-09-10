#include<iostream>
using namespace std;

// Function to insert a new element into the array

void insert(int n, int arr[], int num, int pos)
{
    // Check if the array is already full
    if(n == 50)
    {
        cout << "Array is full. Cannot insert a new element.";
        return;
    }

    // If position is 0, insert at the beginning
    
    else if(pos == 0)
    {
        // Shift all elements one position to the right
        for(int i = n; i > pos; i--)
        {
            arr[i] = arr[i - 1];
        }

        // Insert the new element at position 0
        arr[pos] = num;

        // Increase the number of elements
        n++;

        cout << "After inserting the new element the new array is:\n";

        // Display the updated array
        for(int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }

        return;
    }

    // If position is equal to n, insert at the end
    
    else if(pos == n)
    {
        // Put the new element at the end
        arr[pos] = num;

        // Increase the number of elements
        n++;

        cout << "After inserting the new element the new array is:\n";

        // Display the updated array
        for(int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }

        return;
    }

    // Check whether the entered position is invalid
    else if(pos > n || pos < 0)
    {
        cout << "Invalid position!" << "\n"
             << "Please Enter Valid Position (starts from 1 to " << n << ")";
    }

    // If the position is somewhere in the middle
    else
    {
        // Convert the position into an array index
        // because array indexing starts from 0
        pos = pos - 1;

        // Shift elements one position to the right
        // Start from the end to avoid overwriting elements
        for(int i = n; i > pos; i--)
        {
            arr[i] = arr[i - 1];
        }

        // Insert the new element at the required position
        arr[pos] = num;

        // Increase the number of elements
        n++;

        cout << "After inserting the new element the new array is:\n";

        // Display the updated array
        for(int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }
    }
}

int main()
{
    int n, num, pos;

    // Get the number of elements in the array
    cout << "Enter the array size:\n";
    cin >> n;

    // Create an array with maximum capacity of 50
    int arr[50];

    // Take input for each element
    for(int i = 0; i < n; i++)
    {
        cout << "Enter element : " << i + 1 << endl;
        cin >> arr[i];
    }

    // Get the new element to be inserted
    cout << "Enter the element to be inserted: ";
    cin >> num;

    // Get the position where the element should be inserted
    cout << "Enter the position (starting from 1): ";
    cin >> pos;

    // Call the insert function
    insert(n, arr, num, pos);
}
