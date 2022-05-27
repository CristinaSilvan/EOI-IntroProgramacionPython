import sqlite3
try:
    while 1:
        eleccion = int(input("0-Salir\n1-Crear BD\n2-Crear tabla\n3-Insertar\n4-Insertar Lote\n5-Recuperar Datos\nEleccion: "))
        
        if eleccion == 1:
            miconexion = sqlite3.connect("Base SQLite")
            micursor = miconexion.cursor()
            print("\n")
        elif eleccion == 2:
            micursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(2))")
            print("\n")
        elif eleccion == 3:
            micursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
            miconexion.commit()
            print("\n")
        elif eleccion == 4:
            #micursor.execute("INSERT INTO PRODUCTOS VALUES('Camiseta', 10, 'Deportes')")
            #micursor.execute("INSERT INTO PRODUCTOS VALUES('Jarrón', 30, 'Cerámica')")
            #micursor.execute("INSERT INTO PRODUCTOS VALUES('Barbie', 5, 'Juguetería')")
            loteProductos = [ 
                ("Camiseta", 10, "Deportes"),
                ("Jarrón", 30, "Cerámica"),
                ("Barbie", 5, "Juguetería")
            ]
            micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", loteProductos)

            miconexion.commit()
            print("\n")
        elif eleccion == 5:
            micursor.execute("SELECT * FROM PRODUCTOS")
            datos = micursor.fetchall()
            #print(f"\nDatos Recuperados:\n{datos}")
            print("\nDatos Recuperados:\n")
            #for i in datos:
            #    print(i)

            for i in datos:
                print(f"Nombre artículo: {i[0]} || Precio: {i[1]} || Sección: {i[2]}")

            miconexion.commit()
            print("\n")
        elif eleccion == 0:
            print("\tFinalizando programa...")
            break

    miconexion.close()
except Exception as e:
    print("\tNo se estableció ninguna conexión...")