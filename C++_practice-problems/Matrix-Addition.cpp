#include <iostream>
using namespace std;

int main()
{
    int rows, cols;

    cout << "Enter number of rows: ";
    cin >> rows;

    cout << "Enter number of columns: ";
    cin >> cols;

    int first_arr[10][10];
    int sec_arr[10][10];
    int third_arr[10][10];

    cout << "Enter elements of first matrix:\n";
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cin >> first_arr[i][j];
        }
    }

    cout << "Enter elements of second matrix:\n";
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cin >> sec_arr[i][j];
        }
    }

    cout << "Matrix Addition:\n";
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            third_arr[i][j] = first_arr[i][j] + sec_arr[i][j];
            cout << third_arr[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
