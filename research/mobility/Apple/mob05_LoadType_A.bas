Attribute VB_Name = "mob05_LoadType_A"
Option Explicit
Option Base 1
Public tlen As Integer
Function LoadTypes(wsnum As Integer, rownum As Long, colnum As Integer) As String
'load transportation types contained
Dim i As Integer
Dim output As String, tadd As String

On Error GoTo ErrHandler

With Sheets(wsnum)

tlen = GetTheNum(wsnum, rownum)
If tlen = 1 Then
    LoadTypes = CStr(.Cells(rownum, colnum))

ElseIf tlen > 1 Then
    output = CStr(.Cells(rownum, colnum))
    For i = 2 To tlen
    tadd = CStr(.Cells(rownum + i - 1, colnum))
    output = output & ", " & tadd
    Next i
    LoadTypes = output
End If
End With

Exit Function
ErrHandler:
    MsgBox "Error in Function LoadTypes:" & Err.Description
    Stop

End Function

