@echo off
Rem Batch-tests
Rem Illustration commande CHOICE, IF/ELSE et GOTO
choice /m "Hello ! Voulez-vous installer [truc] (yes/no/cancel)?" /c ync /t 10 /d y
Rem /m -> message, /c -> liste d'options, par défaut yn, /t -> timeout et /d -> option par défaut après le timeout
Rem Réponse stockée dans %errorlevel% en fonction de l'index de la réponse donnée dans la liste /c des réponses possibles. Attention, l'index commence à 1.
IF %errorlevel% == 1 (
	goto yes
) ELSE (  Rem pas de elseif ou de elif
	IF %errorlevel% == 2 (
		goto no
	) ELSE (
		goto cancel
	)
)

:yes
echo Installation en cours...
goto normalexit

:no
echo Vous avez dit non...
goto normalexit

:cancel
echo Annulation...

:normalexit
pause
