Attribute VB_Name = "Module1"
Option Explicit

Private Declare Function OCR Lib "AspriseOCR.dll" (ByVal file As String, ByVal imageType As Long) As String

Sub Main()
Dim a As String
a = OCR(App.Path & "\temp.bmp", -1)
a = Replace(a, vbTab, "")
a = Replace(a, vbCrLf, "")
a = Replace(a, vbNullChar, "")
a = Replace(a, " ", "")
a = Trim(a)
Open App.Path & "\temp.txt" For Binary As #1
Put #1, 1, a
Close #1
End
End Sub

