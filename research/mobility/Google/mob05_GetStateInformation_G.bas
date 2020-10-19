Attribute VB_Name = "mob05_GetStateInformation_G"
Option Explicit
Option Base 1
Sub GetStateInfo()

Dim State As String
Dim ws As Worksheet
Dim i As Long, j As Long
On Error GoTo ErrHandler

State = CStr(InputBox("Which State?", "Please Input Here. Input 'All' for Country-Level Data."))
Set ws = Sheets.Add(After:=Sheets(1))

With Sheets(1)
.Cells(1, 1).EntireRow.Copy Destination:=Sheets(ws.Name).Cells(1, 1).EntireRow.End(xlUp)

If LCase(CStr(State)) = LCase(CStr("All")) Then
    ws.Name = "Sample_Google_US"
    i = 2
    While IsEmpty(.Cells(i, 3))
        .Cells(i, 1).EntireRow.Copy Destination:=Sheets(ws.Name).Cells(Rows.Count, 1).EntireRow.End(xlUp).Offset(1)
    i = i + 1
    Wend
    
Else
    ws.Name = "Sample_Google_US_State_" & UCase(State)
    j = 2
    While Not IsEmpty(.Cells(j, 2))
        If LCase(CStr(.Cells(j, 3))) = LCase(State) Then
            .Cells(j, 1).EntireRow.Copy Destination:=Sheets(ws.Name).Cells(Rows.Count, 1).EntireRow.End(xlUp).Offset(1)
            If Not LCase(CStr(.Cells(j + 1, 3))) = LCase(State) Then
                Exit Sub
            End If
        End If
    j = j + 1
    Wend

End If
End With
Exit Sub

ErrHandler:
    MsgBox "Error in sub GetStateInfo:" & Err.Description
    Stop
End Sub
