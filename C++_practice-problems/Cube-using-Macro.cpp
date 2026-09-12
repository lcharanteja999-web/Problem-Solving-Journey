// A macro is a piece of code that is replaced by its actual code before the program is compiled.

#include <iostream>
using namespace std;

#define CUBE(x) ((x) * (x) * (x))

int main()
{
    int n;

    cout << "Enter a number: ";
    cin >> n;

    cout << "Cube = " << CUBE(n);

    return 0;
}
