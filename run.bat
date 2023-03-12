pytest -s -v -m "Regression" --html=./Reports/report.html testCases/ --browser Firefox
REM pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ 
REM pytest -s -v -m "Regression" --html=./Reports/report.html testCases/ 
REM pytest -s -v -m "sanity and Regression" --html=./Reports/report.html testCases/ 

REM pytest -s -v -m "sanity and Regression" --html=./Reports/report.html testCases/ --browser firefox


