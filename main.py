import mysql.connector

database = input("inserisci database")
password = input("inserisci password database")
connessione_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database=database
)
print(connessione_db)
puntatore = connessione_db.cursor()


def crea_database(nome):
    # CREA TABELLA
    puntatore.execute(f"CREATE DATABASE {nome}")


def crea_tabella(tabella):
    # CREA TABELLA
    puntatore.execute(f"CREATE TABLE {tabella}")


def vedi_tabelle_esistenti():
    # VEDI TABELLE ESISTENTI
    puntatore.execute("SHOW TABLES")
    for db in puntatore:
        print(db)


def aggiungi(nome):
    ## INSERISCI RIGHE
    inserzione = "INSERT INTO clienti (nome) VALUES (%s)"
    values = (nome,)
    puntatore.execute(inserzione, values)
    connessione_db.commit()
    print(puntatore.lastrowid)


def fai_query(query):
    ## FARE UNA QUERY
    puntatore.execute(query)
    lista = puntatore.fetchall()
    print(lista)
    for riga in lista:
        print(riga)


def elimina_riga(cancella):
    ## ELIMINARE RIGA
    puntatore.execute(cancella)
    connessione_db.commit()


def modifica(query):
    puntatore.execute(query)
    connessione_db.commit()
    pass


def mostra_tutto():
    fai_query("SELECT * FROM clienti")

## MODIFICA
# modifica("UPDATE clienti SET nome='valentina' WHERE id=12")

## TODO RIVEDERE I JOIN
## JOIN
# fai_query("SELECT nome, citta.Name, citta.CountryCode FROM clienti INNER JOIN citta ON clienti.città = citta.ID ")

## CREA TABELLA
# crea_tabella("provaa1 (c1 VARCHAR(255), c2 VARCHAR(255))")

## ELIMINA TABELLA
# query = "DROP TABLE IF EXISTS provaa1"
# puntatore.execute(query)
