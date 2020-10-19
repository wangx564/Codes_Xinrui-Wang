Attribute VB_Name = "mob02_CheckData1_G"
Option Explicit
Option Base 1
Sub CheckGData_one()
Dim i As Long, nDays As Long
Dim d As String
Dim ws As Worksheet
Dim dt1 As Date, dt2 As Date

On Error GoTo ErrHandler

dt1 = "02/15/2020"
d = CStr(InputBox("What date?", "Please input in the format of mm/dd/yyyy."))
dt2 = Format(d, "mm/dd/yyyy")
nDays = DateDiff("d", dt1, dt2)

Set ws = Sheets.Add(After:=Sheets(1))
ws.Name = "Data Info Summary 1"

With Sheets(ws.Name)
.Cells(1, 1).Value = "Country"
.Cells(1, 2).Value = "Sub-Region 1"
.Cells(1, 3).Value = "Sub-Region 2"
End With
   
i = 2
With Sheets(1)

While Not IsEmpty(.Cells(i, 2))
.Range("B" & i & ":D" & i).Copy
Sheets(ws.Name).Range("A" & Rows.Count).End(xlUp).Offset(1).PasteSpecial
i = i + nDays + 1
Wend

End With

Call AZSorting(ws.Name, "C")

Exit Sub
ErrHandler:
    MsgBox "Error in sub CheckGData_one:" & Err.Description
    Stop

End Sub
