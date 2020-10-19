Attribute VB_Name = "mob09_LoadType2_A"
Option Explicit
Option Base 1
Function LoadTypes_two(wsnum As Integer, rownum As Long, colnum As Integer, sublen As Long) As String
'load and aggregate transportation types contained
Dim i As Long, j As Long
Dim ttype() As String, tadd As String

On Error GoTo ErrHandler

With Sheets(wsnum)

If sublen = 1 Then
    LoadTypes_two = CStr(.Cells(rownum, colnum))

ElseIf sublen > 1 Then
    j = 1
    ReDim ttype(1)
    ttype(1) = CStr(.Cells(rownum, colnum))
    For i = 2 To sublen
        tadd = CStr(.Cells(rownum + i - 1, colnum))
        If searchIndex(tadd, ttype()) < 0 Then
            j = j + 1
            ReDim Preserve ttype(j)
            ttype(j) = tadd
        End If
    If UBound(ttype()) = 1 Then
        LoadTypes_two = ttype(1)
    ElseIf UBound(ttype()) > 1 Then
        LoadTypes_two = ArrayToString(ttype())
    End If
    Next i
End If
End With

Exit Function
ErrHandler:
    MsgBox "Error in Function LoadTypes_two:" & Err.Description
    Stop

End Function

Function ArrayToString(arr() As String) As String

On Error GoTo ErrHandler

Dim i As Long
Dim output As String, sadd As String

output = arr(1)
For i = 2 To UBound(arr())
    sadd = arr(i)
    output = output & "; " & sadd
Next i
ArrayToString = output

Exit Function
ErrHandler:
    MsgBox "Error in Function ArrayToString:" & Err.Description
    Stop

End Function
