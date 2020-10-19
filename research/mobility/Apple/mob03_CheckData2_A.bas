Attribute VB_Name = "mob03_CheckData2_A"
Option Explicit
Option Base 1
Public countries() As String, ccountry() As String, scountry() As String, coucountry() As String
Sub CheckAData_two()

Dim ws As Worksheet
Dim i As Long, subindex As Long, inputindex_1 As Long, inputindex_2 As Long, inputindex_3 As Long, inputindex_4 As Long
Dim srnum As Long, j As Long, k0 As Long, k1 As Long, k2 As Long, k3 As Long
Dim country As String

On Error GoTo ErrHandler

Set ws = Sheets.Add(After:=Sheets(2))
ws.Name = "Data Info Summary 2"

With Sheets(ws.Name)
.Cells(1, 1).Value = "With Country Level "
.Cells(1, 2).Value = "transportation_types"
.Cells(1, 4).Value = "With City Level"
.Cells(1, 5).Value = "transportation_types"
.Cells(1, 7).Value = "With Sub-Region Level"
.Cells(1, 8).Value = "transportation_types"
.Cells(1, 10).Value = "With County Level"
.Cells(1, 11).Value = "transportation_types"
End With

With Sheets("Data Info Summary 1")
i = 2
k0 = 0
k1 = 0
k2 = 0
k3 = 0

While Not IsEmpty(.Cells(i, 1))
country = .Cells(i, 1)

    If CStr(.Cells(i, 2)) = "country/region" Then  'has country level data
        k0 = k0 + 1
        ReDim Preserve countries(k0)
        inputindex_1 = CountRows(ws.Name, 1) + 1
        Sheets(ws.Name).Cells(inputindex_1, 1) = country 'country
        countries(k0) = country
        Sheets(ws.Name).Cells(inputindex_1, 2) = .Cells(i, 5) 'transportation type
        i = i + 1
    
    ElseIf CStr(.Cells(i, 2)) = "city" Then 'has city level data
        k1 = k1 + 1
        ReDim Preserve ccountry(k1)
        srnum = GetTheRNum(2, i, 2) 'get the number of cities contained
        inputindex_2 = CountRows(ws.Name, 4) + 1 'input index
        Sheets(ws.Name).Cells(inputindex_2, 4) = country 'country
        ccountry(k1) = country
        Sheets(ws.Name).Cells(inputindex_2, 5) = LoadTypes_two(2, i, 5, srnum)  'transpotation type
        i = i + srnum
        
    ElseIf CStr(.Cells(i, 2)) = "sub-region" Then
        k2 = k2 + 1
        ReDim Preserve scountry(k2)
        srnum = GetTheRNum(2, i, 2)  'get the number of sub-regions contained
        inputindex_3 = CountRows(ws.Name, 7) + 1 'input index
        Sheets(ws.Name).Cells(inputindex_3, 7) = country 'country
        scountry(k2) = country
        Sheets(ws.Name).Cells(inputindex_3, 8) = LoadTypes_two(2, i, 5, srnum)  'transpotation type
        i = i + srnum
        
    ElseIf CStr(.Cells(i, 2)) = "county" Then
        k3 = k3 + 1
        ReDim Preserve coucountry(k3)
        srnum = GetTheRNum(2, i, 2)  'get the number of counties contained
        inputindex_4 = CountRows(ws.Name, 10) + 1 'input index
        Sheets(ws.Name).Cells(inputindex_4, 10) = country 'country
        coucountry(k3) = country
        Sheets(ws.Name).Cells(inputindex_4, 11) = LoadTypes_two(2, i, 5, srnum)  'transpotation type
        i = i + srnum
    End If
Wend
End With

Exit Sub
ErrHandler:
    MsgBox "Error in sub CheckAData_two:" & Err.Description
    Stop

End Sub
