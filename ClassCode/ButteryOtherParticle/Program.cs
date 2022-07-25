using System;

class Program {
  class A {
    public int a;
  }

  struct B {
   public int a;
  
  }
  public static void Main (string[] args) {
    A a = null;
    a = new A();
    a.a = 4;

    // reference semantic
    A c = a;
    c.a = 2; // impact A a as well

    B b;
    b.a = 3;

    B d;
    d = b;
    
    
    Console.WriteLine ("Hello World");
  }
}