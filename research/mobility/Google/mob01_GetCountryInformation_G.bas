Attribute VB_Name = "mob01_GetCountryInformation_G"
Option Explicit
Option Base 1
Sub GetCountryInfo()

Dim country As String
Dim ws As Worksheet
Dim i As Long
On Error GoTo ErrHandler

country = CStr(InputBox("Which country?", "Please Input Here"))
Set ws = Sheets.Add(After:=Sheets(1))
ws.Name = "Sample_Google_" & UCase(country)

With Sheets(1)
.Cells(1, 1).EntireRow.Copy Destination:=Sheets(ws.Name).Cells(1, 1).EntireRow.End(xlUp)

i = 2
While Not IsEmpty(.Cells(i, 2))
    If LCase(CStr(.Cells(i, 2))) = LCase(country) Then
        .Cells(i, 1).EntireRow.Copy Destination:=Sheets(ws.Name).Cells(Rows.Count, 1).EntireRow.End(xlUp).Offset(1)
        If Not LCase(CStr(.Cells(i + 1, 2))) = LCase(country) Then
            Exit Sub
        End If
    End If
i = i + 1
Wend
End With

Exit Sub

ErrHandler:
    MsgBox "Error in sub GetCountryInfo:" & Err.Description
    Stop
End Sub
