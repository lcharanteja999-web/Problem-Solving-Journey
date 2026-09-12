#include<iostream>
using namespace std;

void linear_search(int n,int arr[],int target)
{
    for(int i =0; i< n;i++)
    {
        if(arr[i] == target)
        {
            cout << "Element found at index " << i;
            return;
        }
    }

    cout << "Element not found";
    return;
}

int main()
{
    int n,target;

    cout << "Enter size of array:\n";
    cin >> n;

    int arr[n];
    for(int i =0; i< n;i++)
    {
        cout << "Enter Element " << i+1;
    }
    linear_search(n,arr,target);

}
