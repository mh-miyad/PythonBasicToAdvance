@echo off
echo Creating price page based on your existing design...
python code_agent/create_price_page.py --target dist --open
echo.
echo Done! The price.html and price.css files have been created.
pause
