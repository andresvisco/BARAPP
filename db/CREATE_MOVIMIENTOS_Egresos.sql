-- SQLite
CREATE TABLE IF NOT EXISTS EGRESOS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion varchar(64) NOT NULL,
        importe int(11) NOT NULL,
        fecha datetime NOT NULL,
        tipo varchar(64) NOT NULL,
        destino varchar(64) NOT NULL
    )