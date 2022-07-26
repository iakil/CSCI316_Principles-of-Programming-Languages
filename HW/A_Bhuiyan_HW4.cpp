// Akil Bhuiyan
// Professor Joshua Waxman
// CSCI 316
// HW4 - Static keyword

#include <iostream>
using namespace std;

int fib() {
  static int a = 0;
  static int b = 1; // static local var Stored on static storage area
  int temp = a + b;
  a = b;
  b = temp; 
  return a; // func return val
}

int main() {
  std::cout << "Akil's HW4\n";
  int x;
  cout << "Enter a number\t";
  cin >> x; // input

  for(int i=0; i < x; i++){
    if (i+1 == x) {
      cout << fib() << endl; //If input is the last val print
    }

    else {
      cout << fib() << ", "; //Output separated with commas
    }
  }
  return 0;
}
