import sqlite3
conn = sqlite3.connect("c7Music.db")
cursor = conn.cursor()

def read():
    cursor.execute("SELECT * FROM songs") # select all songs
    row = cursor.fetchall() # use to fetch all data from the songs table and pass it to variable "row"
    for record in row:
        print(record) 
#readSongs()