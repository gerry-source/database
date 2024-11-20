import mysql.connector

connessione_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bariale2024",
    database="tabella"
)
print(connessione_db)
puntatore = connessione_db.cursor()


def crea_tabella():
    # CREA TABELLA
    puntatore.execute("CREATE DATABASE tabella")


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


mostra_tutto()
modifica("UPDATE clienti SET nome='valentina' WHERE id=12")
mostra_tutto()
