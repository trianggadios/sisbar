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
    cur.execute("SELECT public.barang.nama_barang, public.barang.lokasi_barang, public.rak.rak_lokasi, public.barang.kategori_barang FROM public.barang INNER JOIN public.rak ON public.barang.rak_lokasi_barang = public.rak.id")
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