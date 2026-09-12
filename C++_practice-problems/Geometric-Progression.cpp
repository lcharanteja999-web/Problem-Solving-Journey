#include <iostream>
using namespace std;

int geometricSeries(int a, int r, int n)
{
    int sum = 0;
    int term = a;

    for(int i = 1; i <= n; i++)
    {
        sum = sum + term;
        term = term * r;
    }

    return sum;
}

int main()
{
    int a, r, n;

    cout << "Enter first term: ";
    cin >> a;

    cout << "Enter common ratio: ";
    cin >> r;

    cout << "Enter number of terms: ";
    cin >> n;

    int result = geometricSeries(a, r, n);

    cout << "Sum of geometric series = " << result;

    return 0;
}
