
'''

Parse the String:   i+i

s - shift
r - reduce

Stack      Input Buffer      Action

0           i+i$              s4
0i4          +i$              r5
0F3          +i$              r4
0T1          +i$              s6
0T1+6         i$              s4
0T1+6i4        $
                              Accept

'''



'''

O -> r
O -> Or
O -> sOO
O -> OOs
O -> OsO
O -> “”




O -> Or
O -> sOO
O -> OsO


********
O ->  sOO

O ->  ssOOO
O ->  ssrOO
O ->  ssrrO
O ->  ssrrr

Failed
********





********
O ->  Or

O ->  sOOr
O ->  srrr

Failed
********




********
O ->  OsO

O ->  sOOsr
O ->  srrsr

Failed
********



'''