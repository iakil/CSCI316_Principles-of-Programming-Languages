// Why in line  (greenly == 3 ? greenly : purple) = 5;  wouldn't work.
using System;

class Program {
    public static void Main (string[] args) {
        Console.WriteLine ("Hello World");
        int greenly = 3;
        int purple = 3;
        (greenly == 3 ? greenly : purple) = 5;

    }
}

