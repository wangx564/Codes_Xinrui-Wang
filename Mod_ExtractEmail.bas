Attribute VB_Name = "Mod_ExtractEmail"
Option Explicit
Option Base 1
Sub GetemailInfo()

Dim SrchRng As Range, cel As Range
Dim ws As Worksheet
Dim i As Long, lRow As Long
Dim j As Integer
On Error GoTo ErrHandler

Set ws = Sheets.Add(After:=Sheets(2))
ws.Name = "Email_Found"

With Sheets(2)
lRow = .Cells(Rows.Count, 1).End(xlUp).Row

For i = 1 To lRow
    If Not IsEmpty(.Cells(i, 4)) Then
        Set SrchRng = Range(Sheets(1).Cells(4, 2), Sheets(1).Cells(427, 2))
        For Each cel In SrchRng
            If CStr(.Cells(i, 4)) = CStr(cel) Then
                .Cells(i, 1).EntireRow.Cut Destination:=Sheets(ws.Name).Cells(Rows.Count, 1).EntireRow.End(xlUp).Offset(1)
                Exit For
            End If
        Next cel
    End If
Next i

End With


Exit Sub

ErrHandler:
    MsgBox "Error in sub GeemailInfo:" & Err.Description
    Stop
End Sub

