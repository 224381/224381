import os
import sqlite3
import unittest
import artDB

def create_database():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    
    # tworzenie tabeli
    cursor.execute("""CREATE TABLE KLUBY
                          (nazwa text, trener text, kraj text, liczba_pilkarzy int, najlepszy_zawodnik text, sponsor_glowny text)
                       """)
    # insert 
    cursor.execute("INSERT INTO KLUBY VALUES "
                   "('PZPN', 'Paulo_Sousa', 'Polska', '11', 'Robert_Lewandowski', 'T-Mobile' )")
    
    # zapisanie danych do bazy 
    conn.commit()
    
def select_wybrany_klub(nazwa):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM KLUBY WHERE NAZWA=?"
    cursor.execute(sql, [(nazwa)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def insert(nazwa, trener, kraj, liczba_pilkarzy, najlepszy_zawodnik, sponsor_glowny):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "INSERT INTO KLUBY VALUE (?, ?, ?, ?, ?)"
    cursor.execute(sql, [(nazwa)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_nazwa_klub(trener, nazwa):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "UPDATE KLUBY SET TRENER WHERE NAZWA ?"
    cursor.execute(sql, [(nazwa)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
	

if __name__ == '__main__':
	unittest.main()

    if not os.path.exists("mydatabase.db"):
        create_database()
    print(select_wybrany_klub('U2’))
