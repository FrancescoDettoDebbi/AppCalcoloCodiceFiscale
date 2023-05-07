# AppCalcoloCodiceFiscale
this simple web app generates codice fiscale.


this App consists in:
  -frontend:
    -index.html
    -main.css
    -script.js
  -API:
    -mainAPI.py
  -backend:
    -CodiceFiscale.py
    -CityFinder.py
  -database:
    -mysql

the idea is to use javascript to call the API that will talk to the database.

first run the queries in the catastale.sql file to create the database.
after that import the data in the codice_catastale.csv file to the database

then import the required libraries with pip:
  pip install mysql-connector-python
  pip install uvicorn
  pip install fastapi

edit the CodiceFiscale.py and CityFinder.py providing correct user and password

then run this command in the terminal:
  uvicorn mainAPI:app --reload

then load the index.html file in the browser

and now you can create Codice Fiscale!
