import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qwerty",
  database="s123_WhiteList"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT DISTINCT Player FROM WLTable")

players = mycursor.fetchall()

with open('output.txt', 'w') as f:
    f.write('[')
    first = True
    for player in players:
        if not first:
            f.write(', ')
        f.write(f'"{player[0]}"')
        first = False
    f.write('];')
