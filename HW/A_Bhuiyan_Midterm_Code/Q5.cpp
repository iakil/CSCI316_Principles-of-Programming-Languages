#include <iostream>
using namespace std;
int * flarmer() {
    static int a[100] = {4, 5, 6};
    if (a[0] > 10)
    cout << "hello";
    return a;
}

int main() {
    int *p;
    p = flarmer();
    p[0] = 100;
    flarmer();
}