import sqlite3

#################~FOREIGN KEY Activation~#######################
# try:
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("la base de donnée est connecté a SQLite")#     
#     cur.execute('PRAGMA foreign_keys=ON;')
#     cur.close()
#     conn.close()
#     print('la connextion est fermée')
# except sqlite3.Error as error:
#     print("erreur lors de la connection", error)

#################~Connexion a la base de donnée~#######################
# try:
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("la base de donnée est connecté a SQLite")

#     sql = "SELECT sqlite_version()"
#     cur.execute(sql)
#     res = cur.fetchall()
#     print('la version de SQLite est ', res)
#     cur.close()
#     conn.close()
#     print('la connextion est fermée')
# except sqlite3.Error as error:
#     print("erreur lors de la connection", error)

#################~Créer une nouvelle table~#######################
# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     sql = '''CREATE TABLE cds(
#         id INTEGER PRIMARY KEY,
#         artist TEXT NOT NULL,
#         album_name TEXT NOT NULL,
#         year_published TEXT NOT NULL
#         )'''
#     print("connection success")
#     cur.execute(sql)
#     conn.commit()
#     print("Table créée")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

# try: 
#     conn = sqlite3.connect('mydb.db')
#     sql = '''CREATE TABLE user(
#         id INTEGER PRIMARY KEY,
#         lastname TEXT NOT NULL,
#         firstname TEXT NOT NULL,
#         role_id INTEGER REFERENCES role(id)
#     )'''
#     cur = conn.cursor()
#     print("connection success")
#     cur.execute(sql)
#     conn.commit()
#     print("Table créée")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

# try: 
#     conn = sqlite3.connect('mydb.db')
#     sql = '''CREATE TABLE role(
#         id INTEGER PRIMARY KEY,
#         role_name TEXT NOT NULL
#         )'''
#     cur = conn.cursor()
#     print("connection success")
#     cur.execute(sql)
#     conn.commit()
#     print("Table créée")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

# try: 
#     conn = sqlite3.connect('mydb.db')
#     sql = '''CREATE TABLE status(
#         id INTEGER PRIMARY KEY,
#         status_name TEXT NOT NULL
#         )'''
#     cur = conn.cursor()
#     print("connection success")
#     cur.execute(sql)
#     conn.commit()
#     print("Table créée")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

#################~Inserer des données dans une table~#######################
# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     cur.execute("PRAGMA foreign_keys=on")
#     sql = '''INSERT INTO cds(
#         artist,
#         album_name,
#         year_published,
#         status_id,
#         user_id) 
#         VALUES (
#         'indochine',
#         'paradize',
#         '2001',
#          1,
#          1 )'''    
#     cur.execute(sql)
#     conn.commit()
#     print("status ajouté")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = '''INSERT INTO user(
#         lastname,
#         firstname,
#         role_id )
#         VALUES (
#         'jamet',
#         'ludo',
#         2)'''    
#     cur.execute(sql)
#     conn.commit()
#     print("status ajouté")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = '''INSERT INTO role(
#         role_name)
#         VALUES (
#         'user')'''    
#     cur.execute(sql)
#     conn.commit()
#     print("status ajouté")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

#################~Select all sur une table~#######################
try: 
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    # cur.execute("PRAGMA foreign_keys=on")
    print("connection success")
    sql = "SELECT * FROM cds"   
    cur.execute(sql)
    # cur.execute("PRAGMA foreign_keys=on")
    res = cur.fetchall()
    for row in res:
        print("id:",row[0])
        print("artist:",row[1])
        print("album_name:",row[2])
        print("published_year:",row[3])
    conn.commit()        
    cur.close()
    conn.close()
    print("connection closed")

except sqlite3.Error as error:
    print("error", error)

# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = "SELECT * FROM user"   
#     cur.execute(sql)
#     res = cur.fetchall()
#     for row in res:
#         print("id:",row[0])
#         print("lastname:",row[1])
#         print("firstname:",row[2])       
            
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = "SELECT * FROM status"   
#     cur.execute(sql)
#     res = cur.fetchall()
#     for row in res:
#         print("id:",row[0])
#         print("status_name:",row[1])     
            
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

#################~Update d'une table~#######################
# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = '''UPDATE user SET lastname = 'Michel' WHERE id = 3'''    
#     cur.execute(sql)
#     conn.commit()
#     print("Enregistrement de la modification")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

#################~Modifier une colonne d'une table~#######################
# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = '''ALTER TABLE cds DROP COLUMN status_id'''   
#     cur.execute(sql)
#     conn.commit()
#     print("colonne modifié")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

#################~Supprimer une colonne d'une table~#######################
# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = '''DELETE FROM cds WHERE cds_id = 3'''    
#     cur.execute(sql)
#     conn.commit()
#     print("colonne supprimé")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

#################~ajouter une colonne dans une table avec FK~#######################
# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = '''ALTER TABLE cds ADD COLUMN status INTEGER FK status_id REFERENCES status(id)'''    
#     cur.execute(sql)
#     conn.commit()
#     print("colonne ajouté")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)

#################~supprimer table~#######################
# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = '''DROP table cds'''    
#     cur.execute(sql)
#     conn.commit()
#     print("table supprimée")
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)


#################~jointure~#######################
# try: 
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     print("connection success")
#     sql = """SELECT author FROM cds 
#     INNER JOIN status
#     ON cds.status_id = status.status_name"""   
#     cur.execute(sql)
#     res = cur.fetchall()
#     for row in res:
#         print(row)
    
#     cur.close()
#     conn.close()
#     print("connection closed")

# except sqlite3.Error as error:
#     print("error", error)