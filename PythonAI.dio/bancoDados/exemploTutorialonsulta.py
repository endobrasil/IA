import sqlite3
con = sqlite3.connect('tutorial.db')

cur = con.cursor()


#seleciona um mundo
cur.execute('select * from clientes where id = 1')

resultado=cur.fetchone()
print(resultado)

#seleciona um todos
cur.execute('select * from clientes')

resultados=cur.fetchall()

for linha in resultados:
	print(linha)


con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()