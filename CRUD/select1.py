from dotenv import load_dotenv
import mysql.connector
import sys
import os

load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")


def main():
    conn = None
    cur = None

    # membangun koneksi
    try:
        # membuat objek koneksi
        conn = mysql.connector.connect(
            user=user, password=password, host=host, database="BUKUDB"
        )

        # membuat objek cursor
        cur = conn.cursor()

    except mysql.connector.errors.ProgrammingError:
        print("Kesalahan: koneksi ke server MySQL gagal")
        sys.exit(1)

    # seleksi data dengan parameter
    try:
        sql = """
                SELECT * FROM PENGARANG
                WHERE PENGARANG_ID = %(kode)s
            """

        cur.execute(sql, {"kode": "P07"})

        resultSet = cur.fetchall()

        for kode, nama in resultSet:
            print("%s, %s" % (kode, nama))

    except mysql.connector.errors.ProgrammingError:
        print("Kesalahan: seleksi data gagal")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
