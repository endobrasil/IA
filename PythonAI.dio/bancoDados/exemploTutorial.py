import sqlite3
con = sqlite3.connect('tutorial.db')

cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE stocks2 (date text, trans text, symbol text, qty real, price real)''')

#cur.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
# Insert a row of data
#cur.execute("INSERT INTO stocks2 VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#nome ="andre"
#email ="andre@brasil.com"

#data = ("Guilherme","gui@gui.com")

lote = [
	('gui',"gui@lerme.com"),
	('andre',"andre@lerme.com"),
	('wendel',"wendel@lerme.com")
]

#cur.executemany("Insert into clientes(nome,email) values (?,?);",lote)

#cur.execute("Insert into clientes(nome,email) values (?,?);",data)


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()