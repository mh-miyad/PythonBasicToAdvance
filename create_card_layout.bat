@echo off
echo Creating card layout with Bootstrap styling...
python code_agent/direct_file_creator.py --type card --output ./
echo.
echo Done! The card_layout.html and card_layout.css files have been created.
pause
