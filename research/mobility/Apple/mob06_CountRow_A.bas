Attribute VB_Name = "mob06_CountRow_A"
Option Explicit
Option Base 1
Function CountRows(wsname As String, colnum As Integer)

On Error GoTo ErrHandler

CountRows = Sheets(wsname).Cells(Rows.Count, colnum).End(xlUp).Row

Exit Function
ErrHandler:
    MsgBox "Error in Function CountRows:" & Err.Description
    Stop
End Function

