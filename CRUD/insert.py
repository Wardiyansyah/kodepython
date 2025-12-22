from dotenv import load_dotenv
import mysql.connector
import sys
import os

load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


def main():
    conn = None
    cur = None

    # membangun koneksi
    try:
        # membuat koneksi
        conn = mysql.connector.connect(
            user=user, password=password, host=host, database="BUKUDB"
        )

        # membuat objek cursor
        cur = conn.cursor()
    except mysql.connector.errors.ProgrammingError:
        print("Kesalahan: koneksi ke server MySQL gagal!")
        sys.exit(1)

    # menambah data ke dalam tabel
    try:
        cur.execute("INSERT INTO PENGARANG VALUES('P06','Andi Winardi')")
        cur.execute("INSERT INTO PENGARANG VALUES('P07','Hermawan')")
        cur.execute("INSERT INTO PENGARANG VALUES('P08','Ari Wijaya')")

        # mengirim perintah commit ke server MySQL
        conn.commit()

    except mysql.connector.errors.ProgrammingError:
        print("Kesalahan: data gagal ditambahkan")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
