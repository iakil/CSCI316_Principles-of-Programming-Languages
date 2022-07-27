Option Explicit

' Akil Bhuiyan
' Professor Joshua Waxman
' CSCI 316
' HW6 - VBA Nested Ifs

' if (sum == 0) if (count == 0) result = 0; else result = 1;
' We can put Default count as 3 and sum as 0 (or anything for count or sum)
Sub Interpretation1 ()
  Dim Sum As Long, Count As Long, Result As Long
  Sum = InputBox("Sum = ")
  Count = InputBox("Count = ")
  If Sum  = 0 Then
    If Count = 0 Then
      Result = 0
    End If
  Else
    Result = 1
  End If
End Sub

Sub Interpretation2 ()
  Dim Sum As Long, Count As Long, Result As Long
  Sum = InputBox("Sum = ")
  Count = InputBox("Count = ")
    If Count = 0 Then
      Result = 0
  Else
    Result = 1
  End If
End Sub

Sub foo()
  Dim x As Long
  x=0
  Do
    Debug.Print x
    x = x + 1
  Loop While x < 5

  Dim a(5) As Long
  For Each c In a

  Next v
End sub

Function bar(x As Long) As Long
  bar = 56
End Function
