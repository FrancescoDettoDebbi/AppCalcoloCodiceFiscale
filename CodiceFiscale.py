from datetime import datetime
import mysql.connector


class CodiceFiscale:
    # attrs
    cons = "BCDFGHJKLMNPQRSTVZ"
    wild_char = "X"
    month_letters = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'H',
        7: 'L',
        8: 'M',
        9: 'P',
        10: 'R',
        11: 'S',
        12: 'T'
    }

    odd_chars_dict = {
        "0": 1,
        "1": 0,
        "2": 5,
        "3": 7,
        "4": 9,
        "5": 13,
        "6": 15,
        "7": 17,
        "8": 19,
        "9": 21,
        "A": 1,
        "B": 0,
        "C": 5,
        "D": 7,
        "E": 9,
        "F": 13,
        "G": 15,
        "H": 17,
        "I": 19,
        "J": 21,
        "K": 2,
        "L": 4,
        "M": 18,
        "N": 20,
        "O": 11,
        "P": 3,
        "Q": 6,
        "R": 8,
        "S": 12,
        "T": 14,
        "U": 16,
        "V": 10,
        "W": 22,
        "X": 25,
        "Y": 24,
        "Z": 23
    }

    even_chars_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
    }
    opp_conversion_dict = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
    }

    conversion_dict = {v: k for k, v in opp_conversion_dict.items()}

    db_name = "catastale"

    # costruttore
    def __init__(self, nome, cognome, data, sesso, comune):
        self.db = mysql.connector.connect(
            host='localhost',
            user='Franco',
            passwd="FrancoDiMarte89!",
            database=self.db_name
        )
        self.my_cursor = self.db.cursor()
        cog = self.get_porzione_cognome(cognome)
        nom = self.get_porzione_nome(nome)
        an = self.get_porzione_anno(data.year)
        m = self.get_lettera_mese(data.month)
        gg = self.get_giorno_nascita(data.day, sesso)
        codice_catastale = self.get_code_comune(comune)
        codice_fiscale = cog + nom + an + m + gg + codice_catastale
        self.codice_fiscale = codice_fiscale + self.get_special_char(codice_fiscale)

    def get_porzione_nome(self, nome: str) -> str:
        nome_cons = [lettera for lettera in nome.upper() if lettera in self.cons]
        nome_vo = [lettera for lettera in nome.upper() if lettera not in self.cons]
        if len(nome_cons) > 3:
            return nome_cons[0] + nome_cons[2] + nome_cons[3]
        if len(nome_cons) == 3:
            return nome_cons[0] + nome_cons[1] + nome_cons[2]
        else:
            nome_cons += nome_vo
        if len(nome_cons) > 2:
            return nome_cons[0] + nome_cons[1] + nome_cons[2]
        if len(nome_cons) == 2:
            return nome_cons[0] + nome_cons[1] + self.wild_char
        if len(nome_cons) == 1:
            return nome_cons[0] + self.wild_char + self.wild_char

    def get_porzione_cognome(self, nome: str) -> str:
        nome_cons = [lettera for lettera in nome.upper() if lettera in self.cons]
        nome_vo = [lettera for lettera in nome.upper() if lettera not in self.cons]
        if len(nome_cons) > 2:
            return nome_cons[0] + nome_cons[1] + nome_cons[2]
        else:
            nome_cons += nome_vo
        if len(nome_cons) > 2:
            return nome_cons[0] + nome_cons[1] + nome_cons[2]
        if len(nome_cons) == 2:
            return nome_cons[0] + nome_cons[1] + self.wild_char
        if len(nome_cons) == 1:
            return nome_cons[0] + self.wild_char + self.wild_char

    def get_porzione_anno(self, anno: int) -> str:
        return str(anno)[2:]

    def get_lettera_mese(self, mese: int) -> str:
        return self.month_letters[mese]

    def get_giorno_nascita(self, giorno: int, sesso: bool) -> str:
        if sesso:
            if giorno < 10:
                return str(0) + str(giorno)
            else:
                return str(giorno)
        else:
            return str(giorno + 40)

    def get_code_comune(self, comune: str) -> str:
        self.my_cursor.execute(f"select * from comuni where comuni.comune = '{comune}'")
        ans = self.my_cursor.fetchall()
        return ans[0][0]

    def get_special_char(self, codice: str) -> str:
        sommatoria = 0
        for i in range(len(codice)):
            if i % 2 == 1:
                sommatoria += self.even_chars_dict[codice[i]]
            else:
                sommatoria += self.odd_chars_dict[codice[i]]
        return self.conversion_dict[sommatoria % 26]


if __name__ == "__main__":
    codici_fiscali = [CodiceFiscale("Francesco", "Debbi", datetime.fromisoformat("1998-07-23"), True, "Scandiano"),
                      CodiceFiscale("Andrea", "Debbi", datetime.fromisoformat("1968-02-21"), True, "Sassuolo"),
                      CodiceFiscale("Cinzia", "Rossini", datetime.fromisoformat("1969-03-30"), False, "Sassuolo")]
    for cod in codici_fiscali:
        print(cod.codice_fiscale)
