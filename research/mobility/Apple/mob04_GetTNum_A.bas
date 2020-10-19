Attribute VB_Name = "mob04_GetTNum_A"
Option Explicit
Option Base 1
Function GetTheNum(wsnum As Integer, rownum As Long) As Integer
'get the number of transportation types contained in the dataset for that region
'take the rownum as the row where the place first appears
Dim i As Integer
Dim place_1 As String, place_2 As String
Dim rnum As Long

On Error GoTo ErrHandler

With Sheets(wsnum)

place_1 = CStr(.Cells(rownum, 2))
place_2 = CStr(.Cells(rownum, 5))

i = 1
rnum = rownum
While CStr(.Cells(rnum + 1, 2)) = place_1 And CStr(.Cells(rnum + 1, 5)) = place_2
    i = i + 1
    rnum = rnum + 1
Wend

If i > 3 Then
    MsgBox "Transportation Type Error!"
    Stop
    Exit Function
End If

GetTheNum = i
End With


Exit Function
ErrHandler:
    MsgBox "Error in Function GetTheNum:" & Err.Description
    Stop
End Function

