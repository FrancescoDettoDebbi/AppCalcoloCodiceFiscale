import mysql.connector


class CityFinder:

    db_name = "catastale"
    db = mysql.connector.connect(
        host='localhost',
        user='',
        passwd='',
        database=db_name
    )
    cursor = db.cursor()

    def get_comune(self, pezzo: str) -> dict:
        pezzo = pezzo.upper()
        self.cursor.execute(f"select comuni.comune from comuni where comuni.comune like '%{pezzo}%'")
        results = self.cursor.fetchall()
        return {"comuni": [result[0] for result in results]}


if __name__ == "__main__":
    c = CityFinder()
    print(c.get_comune("sass"))
