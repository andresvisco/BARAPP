import sqlite3

class Egresos:
    def __init__(self, descripcion, importe, fecha, tipo, destino):
        self.descipcion = descripcion
        self.importe = importe
        self.fecha = fecha
        self.tipo = tipo
        self.destino = destino
    
    def guardar(self):
        db = sqlite3.connect('db/bar.db')
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO EGRESOS (DESCRIPCION, IMPORTE, FECHA, TIPO, DESTINO)
            VALUES (?, ?, ?, ?, ?)
        """, (self.descipcion, self.importe, self.fecha, self.tipo, self.destino))
        db.commit()
        db.close()

    