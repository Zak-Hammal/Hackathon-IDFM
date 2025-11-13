@echo off
echo ========================================
echo   Demontrateur Score de Mobilite
echo ========================================
echo.
echo Installation des dependances...
pip install -r requirements.txt
echo.
echo Demarrage de l'application Flask...
echo.
echo L'application sera accessible sur : http://localhost:5000
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.
python app.py

