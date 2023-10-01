x = MsgBox("Ceci est un exemple de boîtes de dialogue en VBScript. Le bouton par défaut est 1. Ce message est critique.", vbOKCancel + vbCritical + vbDefaultButton1, "Exemple")

If x = vbOK Then
	x = MsgBox("Vous avez répondu OK.", vbInformation, "Exemple")
Else
	x = MsgBox("Vous avez répondu Annuler.", vbInformation, "Exemple")
End If

x = MsgBox("Est-ce que vous aimez Windows ?", vbQuestion + vbDefaultButton2 + vbYesNo, "Sondage de satisfaction")

If x = vbYes Then
	x = MsgBox("AAAAAAAAAAAAH vous êtes stupide.", vbInformation, "Exemple")
Else
	x = MsgBox("LINUX", vbInformation, "Exemple")
End If

x = MsgBox("Ceci est une boîte avec de l'aide où le texte est aligné à droite.", vbMsgBoxHelpButton + vbMsgBoxRight, "Même le titre ^^ (sous win7)")

count = 0
Do While count < 5
	x = MsgBox("Ce message apparîtra 5 fois.", vbInfo + vbOKOnly, "Exemple")
	count = count + 1
Loop
