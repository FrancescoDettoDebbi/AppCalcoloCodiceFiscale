import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from CodiceFiscale import CodiceFiscale
from main import CityFinder

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

searcher = CityFinder()


@app.get("/comuni/{piece}")
async def get_cities(piece):
    return searcher.get_comune(piece)


@app.get("/codice")
async def get_codice_fiscale(name: str, last_name: str, date: str, sex: bool, city: str):
    data_nascita = datetime.datetime.fromisoformat(date)

    c = CodiceFiscale(name, last_name, data_nascita, sex, city)
    return {"codiceFiscale": c.codice_fiscale}
