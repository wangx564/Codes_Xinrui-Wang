Attribute VB_Name = "mob02_CheckData1_A"
Option Explicit
Option Base 1
Sub CheckAData_one()
Dim i As Long, pindex  As Long
Dim d As String, types As String
Dim ws As Worksheet
Dim dt1 As Date, dt2 As Date

On Error GoTo ErrHandler

Set ws = Sheets.Add(After:=Sheets(1))
ws.Name = "Data Info Summary 1"

With Sheets(ws.Name)
.Cells(1, 1).Value = "Country "
.Cells(1, 2).Value = "Sub-Region"
.Cells(1, 3).Value = "Geo Type"
.Cells(1, 4).Value = "Region"
.Cells(1, 5).Value = "Transportation Types"
End With

With Sheets(1)
i = 2
While Not IsEmpty(.Cells(i, 2))
    pindex = CountRows(ws.Name, 1) + 1
    types = LoadTypes(1, i, 3)
    Sheets(ws.Name).Cells(pindex, 5) = types
    
    If CStr(.Cells(i, 1)) = "country/region" Then
    Sheets(ws.Name).Cells(pindex, 1) = .Cells(i, 2) 'country
    Sheets(ws.Name).Cells(pindex, 2) = .Cells(i, 1) 'geo_type
    
    Else
    Sheets(ws.Name).Cells(pindex, 1) = .Cells(i, 6)
    Sheets(ws.Name).Cells(pindex, 2) = .Cells(i, 1)
    Sheets(ws.Name).Cells(pindex, 3) = .Cells(i, 5)
    Sheets(ws.Name).Cells(pindex, 4) = .Cells(i, 2)
    End If
    
i = i + tlen
Wend

End With
Call AZSorting(ws.Name, "E")
Exit Sub
ErrHandler:
    MsgBox "Error in sub CheckAData_one:" & Err.Description
    Stop

End Sub
