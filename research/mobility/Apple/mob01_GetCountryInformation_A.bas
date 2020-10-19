Attribute VB_Name = "mob1_GetCountryInformation_A"
Option Explicit
Option Base 1
Sub GetCountryInfo()

Dim country As String
Dim ws As Worksheet
Dim i As Integer, nrow As Integer
On Error GoTo ErrHandler

country = CStr(InputBox("Which country?", "Please Input Here"))
Set ws = Sheets.Add(After:=Sheets(1))
ws.Name = "Sample_Apple_" & UCase(country)

With Sheets(1)
nrow = .Cells(Rows.Count, 1).End(xlUp).Row

.Cells(1, 1).EntireRow.Copy Destination:=Sheets(ws.Name).Cells(1, 1).EntireRow.End(xlUp)
For i = 2 To nrow
    If LCase(CStr(.Cells(i, 2))) = LCase(country) Or LCase(CStr(.Cells(i, 6))) = LCase(country) Then
        .Cells(i, 1).EntireRow.Copy Destination:=Sheets(ws.Name).Cells(Rows.Count, 1).EntireRow.End(xlUp).Offset(1)
    End If
Next i
End With

Exit Sub

ErrHandler:
    MsgBox "Error in sub GetCountryInfo:" & Err.Description
    Stop
End Sub
