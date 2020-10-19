Attribute VB_Name = "mob07_Sort_A"
Option Explicit
Option Base 1
Sub AZSorting(wsname As String, tocol As String)
Dim nrow As Long

On Error GoTo ErrHandler

nrow = Sheets(wsname).Cells(Rows.Count, 1).End(xlUp).Row
Sheets(wsname).Range("A2:" & tocol & nrow).Sort key1:=Range("A2:A" & nrow), order1:=xlAscending, Header:=xlNo

Exit Sub
ErrHandler:
    MsgBox "Error in sub AZSorting:" & Err.Description
    Stop
End Sub
