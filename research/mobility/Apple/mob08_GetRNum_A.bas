Attribute VB_Name = "mob08_GetRNum_A"
Option Explicit
Option Base 1
Function GetTheRNum(wsnum As Integer, rownum As Long, colnum As Integer) As Long
'get the number of sub regions contained in the dataset for that country
'take the rownum as the row where the place first appears
Dim i As Integer
Dim place_1 As String
Dim rnum As Long

On Error GoTo ErrHandler

With Sheets(wsnum)

place_1 = CStr(.Cells(rownum, colnum))

i = 1
rnum = rownum
While CStr(.Cells(rnum + 1, colnum)) = place_1
    i = i + 1
    rnum = rnum + 1
Wend
GetTheRNum = i
End With


Exit Function
ErrHandler:
    MsgBox "Error in Function GetTheRNum:" & Err.Description
    Stop
End Function


