Attribute VB_Name = "mob03_CheckData2_G"
Option Explicit
Option Base 1
Sub CheckGData_two()

Dim ws As Worksheet
Dim i As Long, subindex As Long, inputindex_1 As Long, inputindex_2 As Long, inputindex_3 As Long, inputindex_4 As Long

On Error GoTo ErrHandler

Set ws = Sheets.Add(After:=Sheets(2))
ws.Name = "Data Info Summary 2"

With Sheets(ws.Name)
.Cells(1, 1).Value = "With Only Country Level"
.Cells(1, 2).Value = "With Country & Sub-Region 1 Levels"
.Cells(1, 3).Value = "With Country & Sub-Region 2 Levels"
.Cells(1, 4).Value = "With All 3 Levels"
End With
    
With Sheets("Data Info Summary 1")
i = 2
While Not IsEmpty(.Cells(i, 1))
    If Not .Cells(i + 1, 1) = .Cells(i, 1) Then 'only country level data
        inputindex_1 = CountRows(ws.Name, 1) + 1
        Sheets(ws.Name).Cells(inputindex_1, 1) = .Cells(i, 1)
        i = i + 1
    
    ElseIf .Cells(i + 1, 1) = .Cells(i, 1) Then 'may have sub1 or sub2 data
        subindex = .Cells(i + 1, 2).End(xlDown).Row 'the last row of data about the country before encountering an empty cell
        
        If Not IsEmpty(.Cells(subindex, 2)) And IsEmpty(.Cells(subindex, 3)) Then 'have only sub1 data
            inputindex_2 = CountRows(ws.Name, 2) + 1
            Sheets(ws.Name).Cells(inputindex_2, 2) = .Cells(i, 1)
            i = subindex + 1
        ElseIf Not IsEmpty(.Cells(subindex, 3)) And IsEmpty(.Cells(subindex, 2)) Then  'have only sub2 data
            inputindex_3 = CountRows(ws.Name, 3) + 1
            Sheets(ws.Name).Cells(inputindex_3, 3) = .Cells(i, 1)
            i = subindex + 1
        ElseIf Not IsEmpty(.Cells(subindex, 2)) And Not IsEmpty(.Cells(subindex, 3)) Then  'have both sub1 and sub2 data
            inputindex_4 = CountRows(ws.Name, 4) + 1
            Sheets(ws.Name).Cells(inputindex_4, 4) = .Cells(i, 1)
            i = subindex + 1
        End If
    
    End If
Wend

End With

Exit Sub
ErrHandler:
    MsgBox "Error in sub CheckGData_two:" & Err.Description
    Stop

End Sub
Function CountRows(wsname As String, colnum As Integer)

On Error GoTo ErrHandler

CountRows = Sheets(wsname).Cells(Rows.Count, colnum).End(xlUp).Row

Exit Function
ErrHandler:
    MsgBox "Error in Function CountRows:" & Err.Description
    Stop
End Function
