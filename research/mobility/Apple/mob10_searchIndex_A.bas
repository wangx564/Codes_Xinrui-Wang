Attribute VB_Name = "mob10_searchIndex_A"
Option Explicit
Option Base 1
Function searchIndex(target As String, fromarr() As String) As Integer
On Error GoTo handler

Dim i As Integer
For i = 1 To UBound(fromarr)
    If target = fromarr(i) Then
        Exit For
    End If
Next i
    
If i > UBound(fromarr) Then
    'MsgBox "Error: in searchIndex: " & target & " cannot be found. Exit(-1)!"
    searchIndex = -1
Else
    searchIndex = i
End If
Exit Function

handler:
MsgBox "Error: in searchIndex " & Err.Description
Stop
End Function


