@echo off
echo Creating price page with Bootstrap styling...
python code_agent/direct_file_creator.py --type price --output ./
echo.
echo Done! The price.html and price.css files have been created.
pause
