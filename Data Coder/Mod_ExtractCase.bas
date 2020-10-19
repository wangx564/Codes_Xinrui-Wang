Attribute VB_Name = "Mod_ExtractCase"
Option Explicit
Option Base 1
Sub GetTextInfo()

Dim text As String
Dim SrchRng As Range, cel As Range
Dim ws As Worksheet
Dim i As Long, lRow As Long
Dim wsv As String, casev As Variant
On Error GoTo ErrHandler

text = CStr(InputBox("What text?", "Please Input Here"))
Set ws = Sheets.Add(After:=Sheets(1))
ws.Name = "Case_Related_to " & text

With Sheets(1)
.Cells(1, 1).EntireRow.Copy Destination:=Sheets(ws.Name).Cells(1, 1).EntireRow.End(xlUp)
lRow = .Cells(Rows.Count, 1).End(xlUp).Row

For i = 2 To lRow
    If Not IsEmpty(.Cells(i, 1)) Then
        Set SrchRng = Range(.Cells(i, 3), .Cells(i, 17))
    For Each cel In SrchRng
    lRow_2 = Sheets(ws.Name).Cells(Rows.Count, 1).End(xlUp).Row
        If InStr(1, CStr(cel.Value), text) > 0 And Sheets(ws.Name).Cells(lRow_2, 1).Value <> .Cells(i, 1).Value Then
            .Cells(i, 1).EntireRow.Cut Destination:=Sheets(ws.Name).Cells(Rows.Count, 1).EntireRow.End(xlUp).Offset(1)
        End If
    Next cel
    End If
Next i

End With


Exit Sub

ErrHandler:
    MsgBox "Error in sub GeTextInfo:" & Err.Description
    Stop
End Sub

