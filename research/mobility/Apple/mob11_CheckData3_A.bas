Attribute VB_Name = "mob11_CheckData3_A"
Option Explicit
Option Base 1
Sub CheckAData_three()

Dim ws As Worksheet
Dim i As Long, inputindex_1 As Long, inputindex_2 As Long, inputindex_3 As Long, inputindex_4 As Long, inputindex_5 As Long
Dim inputindex_6 As Long, inputindex_7 As Long, inputindex_8 As Long

On Error GoTo ErrHandler

Set ws = Sheets.Add(After:=Sheets(3))
ws.Name = "Data Info Summary 3"

With Sheets(ws.Name)
.Cells(1, 1).Value = "With Only Country Level"
.Cells(1, 2).Value = "With Only City Level"
.Cells(1, 3).Value = "With Only Sub-Region Level"
.Cells(1, 4).Value = "With Country & City Levels"
.Cells(1, 5).Value = "With Country & Sub-Region Levels"
.Cells(1, 6).Value = "With City & Sub-Region Levels"
.Cells(1, 7).Value = "With Country & City & Sub-Region Levels"
.Cells(1, 8).Value = "With All 4 Levels"
End With

With Sheets(ws.Name)
For i = 1 To UBound(countries()) 'Only Country Level
    If searchIndex(countries(i), ccountry()) < 0 And searchIndex(countries(i), scountry()) < 0 _
    And searchIndex(countries(i), coucountry()) < 0 Then
    inputindex_1 = CountRows(ws.Name, 1) + 1
    .Cells(inputindex_1, 1) = countries(i)
    End If
Next i

For i = 1 To UBound(ccountry()) 'Only City Level
    If searchIndex(ccountry(i), countries()) < 0 And searchIndex(ccountry(i), scountry()) < 0 _
    And searchIndex(ccountry(i), coucountry()) < 0 Then
    inputindex_2 = CountRows(ws.Name, 2) + 1
    .Cells(inputindex_2, 2) = ccountry(i)
    End If
Next i

For i = 1 To UBound(scountry()) ' Only Sub-Region Level
    If searchIndex(scountry(i), countries()) < 0 And searchIndex(scountry(i), ccountry()) < 0 _
    And searchIndex(scountry(i), coucountry()) < 0 Then
    inputindex_3 = CountRows(ws.Name, 3) + 1
    .Cells(inputindex_3, 3) = scountry(i)
    End If
Next i

'Only Country and City Levels
For i = 1 To UBound(countries)
    If searchIndex(countries(i), ccountry()) > 0 And searchIndex(countries(i), scountry()) < 0 _
    And searchIndex(countries(i), coucountry()) < 0 Then
        inputindex_4 = CountRows(ws.Name, 4) + 1
        .Cells(inputindex_4, 4) = countries(i)
    End If
Next i
'Only Country and Sub-Region Levels
For i = 1 To UBound(countries)
    If searchIndex(countries(i), scountry()) > 0 And searchIndex(countries(i), ccountry()) < 0 _
    And searchIndex(countries(i), coucountry()) < 0 Then
        inputindex_5 = CountRows(ws.Name, 5) + 1
        .Cells(inputindex_5, 5) = countries(i)
    End If
Next i
'Only City and Sub-Region Level
For i = 1 To UBound(ccountry())
    If searchIndex(ccountry(i), scountry()) > 0 And searchIndex(ccountry(i), countries()) < 0 _
    And searchIndex(ccountry(i), coucountry()) < 0 Then
        inputindex_6 = CountRows(ws.Name, 6) + 1
        .Cells(inputindex_6, 6) = ccountry(i)
    End If
Next i
'With Country, City, and Sub-Region Levels
For i = 1 To UBound(countries())
    If searchIndex(countries(i), ccountry()) > 0 And searchIndex(countries(i), scountry()) > 0 _
    And searchIndex(countries(i), coucountry()) < 0 Then
    inputindex_7 = CountRows(ws.Name, 7) + 1
    .Cells(inputindex_7, 7) = countries(i)
    End If
Next i
'All 4 Levels
For i = 1 To UBound(countries())
    If searchIndex(countries(i), ccountry()) > 0 And searchIndex(countries(i), scountry()) > 0 _
    And searchIndex(countries(i), coucountry()) > 0 Then
    inputindex_8 = CountRows(ws.Name, 8) + 1
    .Cells(inputindex_8, 8) = countries(i)
    End If
Next i
End With

Exit Sub
ErrHandler:
    MsgBox "Error in sub CheckAData_three:" & Err.Description
    Stop
End Sub

