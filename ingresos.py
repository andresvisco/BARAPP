import sqlite3

class Ingresos:
    def __init__(self, descripcion, importe, fecha, tipo, socio):
        self.descipcion = descripcion
        self.importe = importe
        self.fecha = fecha
        self.tipo = tipo
        self.socio = socio
    
    def guardar(self):
        db = sqlite3.connect('db/bar.db')
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO INGRESOS (DESCRIPCION, IMPORTE, FECHA, TIPO, SOCIO)
            VALUES (?, ?, ?, ?, ?)
        """, (self.descipcion, self.importe, self.fecha, self.tipo, self.socio))
        db.commit()
        db.close()

    