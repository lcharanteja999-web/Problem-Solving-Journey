#include <iostream>
using namespace std;

bool isSymmetric(int a[3][3])
{
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            if(a[i][j] != a[j][i])
            {
                return false;
            }
        }
    }

    return true;
}

int main()
{
    int a[3][3];

    cout << "Enter elements of matrix:\n";

    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            cin >> a[i][j];
        }
    }

    bool symmetric = isSymmetric(a);

    if(symmetric == true)
    {
        cout << "Matrix is symmetric";
    }
    else
    {
        cout << "Matrix is not symmetric";
    }

    return 0;
}
