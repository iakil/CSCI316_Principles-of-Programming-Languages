// Akil Bhuiyan
// Professor Joshua Waxman
// CSCI 316
// HW5 - Bubble Sort

using System;
class Program {
  private static void swap(ref int a, ref int b)
  {
  int c = a;
  a = b;
  b = c;
  }
  
  public static void bubbleSort(int[] arr) {
    int n = arr.Length;
    for (int i=0; i < n-1; i++) {
    for (int j=0; j < n-1; j++) {
    if (arr[j] > arr[j+1]) {
    swap(ref arr[j], ref arr[j+1]);
        }}}}
  
  public static void Main (string[] args) {
    int[] arr=new int[10]; 
    for (int i = 0; i < arr.Length; i++)
    {
      Console.Write($"Enter input# {i+1} out of {arr.Length-i} to your array and press enter key:  ");
      arr[i] = int.Parse(Console.ReadLine());   
    }

    Console.Write("\n\n\nGiven Array Is: \t\t\t");
    for (int i = 0; i < arr.Length; i++) {
      if(i == arr.Length-1) Console.Write(arr[i] + "\n");
      else Console.Write(arr[i] + ", ");
    }
    Console.Write("\n");
    Program.bubbleSort(arr);
    
    Console.Write("Sorted Array Using Bubble Sort Is: \t");
    for (int i = 0; i < arr.Length; i++) {
      if(i == arr.Length-1) Console.Write(arr[i] + "\n");
      else Console.Write(arr[i] + ", ");
    }
    Console.Write("\n\n\n");
  } //main 
  }