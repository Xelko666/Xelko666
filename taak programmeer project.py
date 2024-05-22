import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Senne123!",
    database = "cinemax"
    )
cursor = con.cursor()

while True:
    print("BEHEER FILMS")
    print("Kies één van de opties:\n" 
          "1: Lijst films tonen\n" 
          "2: Film toevoegen\n"
          "3: Film zoeken\n"
          "4: Film verwijderen\n"
          "0: Terug naar hoofdmenu\n")
    
    user = input("Maak je  keuze")
    if user == "1":
        sql = "SELECT * FROM films ORDER BY naam ASC" 
        cursor.execute(sql)
    
        recs = cursor.fetchall()
        print(tabulate(recs))
    
    if user == "2":
        nieuwe_film_naam = input("Geef de naam van de film die je wilt toevoegen")
        nieuwe_film_tijd = input("Geef de duratie van de film die je wilt toevoegen. (in minuten)")
        nieuwe_film_knt = input("is de film die je wilt toevoegen 18+? (Ja of Nee)")
        nieuwe_film_tmndb_id = input("Geef de film id in van de film die je wilt toevoegen")
        nieuwe_film_3D = input("is de film die je wilt toevoegen in 3D? (Ja of Nee)")
        
        sql = f"INSERT INTO films (id, naam, speelduur, knt, tmndb_id, 3dfilm) VALUES (8, {nieuwe_film_naam}, {nieuwe_film_tijd}, {nieuwe_film_knt}, {nieuwe_film_tmndb_id}, {nieuwe_film_3D})"
        cursor.execute(sql)
    
        recs = cursor.fetchall()
        con.commit()
        print(tabulate(recs))
        
    if user == "0":
        pass
    
    if user == "3":
        gezochte_film = input("Geef de naam in van de film die u zoekt")
        sql = f"SELECT * FROM films WHERE naam = {gezochte_film}"
        cursor.execute(sql)
    
        recs = cursor.fetchall()
        con.commit()
        print(tabulate(recs))
        
    
    if user == "4":
        verwijder_film = input("Geef het id van welke film je wilt verwijderen")
        zekerheid = input("bent u zeker dat u deze film wilt verijderen? (Ja of Nee)")
        if zekerheid == "Ja":
            sql = f"DELETE FROM films WHERE id = {verwijder_film}"
            cursor.execute(sql)
    
            recs = cursor.fetchall()
            con.commit()
            print(tabulate(recs))
            print("film is verwijderd.")

        if zekerheid == "Nee":
            continue
    
        