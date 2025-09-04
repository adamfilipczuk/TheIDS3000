@echo off
REM Quick setup for IDS 3000

python -m venv .venv
call .\.venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

crewai install

echo Setup complete. To run the project:
echo .\.venv\Scripts\activate
echo crewai run 
pause
