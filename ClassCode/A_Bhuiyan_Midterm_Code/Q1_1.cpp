// Ternary or Elvis operator in c++

#include <iostream>
using namespace std;
int main(){
string x = "";
int y=3;
x = (y == 3 ? "hello" : "goodbye"); 
cout << x;
return 0;
}