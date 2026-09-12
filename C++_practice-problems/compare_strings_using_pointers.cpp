#include <iostream>
#include <cstring>
using namespace std;

bool compareStrings(char *str1, char *str2)
{
    while(*str1 != '\0' && *str2 != '\0')
    {
        if(*str1 != *str2)
        {
            return false;
        }

        str1++;
        str2++;
    }

    if(*str1 == '\0' && *str2 == '\0')
    {
        return true;
    }

    return false;
}

int main()
{
    char str1[100], str2[100];

    cout << "Enter first string: ";
    cin >> str1;

    cout << "Enter second string: ";
    cin >> str2;

    bool result = compareStrings(str1, str2);

    if(result == true)
    {
        cout << "Strings are equal";
    }
    else
    {
        cout << "Strings are not equal";
    }

    return 0;
}
