#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a;
    long long b;
    char ch;
    float d;
    double e;

    cin >> a >> b >> ch >> d >> e;

    cout << a << "\n";
    cout << b << "\n";
    cout << ch << "\n";

    cout << fixed << setprecision(3) << d << "\n";
    cout << fixed << setprecision(15) << e << "\n";

    return 0;
}
