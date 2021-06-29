from lib.database import db_connect


def vertikal():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(f"SELECT nama_barang, kategori_barang FROM public.barang")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def horizontal():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM public.barang WHERE public.barang.lokasi_barang = 'A1'")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def campuran():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(f"SELECT nama_barang, kategori_barang, lokasi_barang FROM public.barang WHERE public.barang.lokasi_barang = 'A2'")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data