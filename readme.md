[![Build Status](https://app.travis-ci.com/BlazeFace/security-backend.svg?token=pKqjhnyssdGdPSXryWxh&branch=main)](https://app.travis-ci.com/BlazeFace/security-backend)
1. Clone repo
2. Run ```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -``` for Mac/Linux run ```(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -``` for windows
3. Run ```cd app``` then ```poetry install ```
4. Run ```pip install uvicorn[standard] fastapi```
5. To run server use ```uvicorn main:app --reload```
