import colorama
import os
import dotenv
import mysql.connector
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
dotenv.load_dotenv("password_sql_server.env")
mysql_password = os.getenv("MYSQL_PASSWORD")

class front_end_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grades")
        self.setGeometry(100, 100, 1400, 800)
        self.resize(1400, 800)



# class UpdatorConnector:
#     def __init__(self):
#         pass
#
#     def register(self):
#         try:
#
#             connectdb = mysql.connector.connect(
#                 host="192.168.1.38",
#                 user="aaravmalooking",
#                 password=mysql_password
#             )
#             print("register your school and be a part of the best grading system ever!")
#             print("To register, please type your school name and a database specifically for your school will be "
#                   "created!")
#             school_name = input(colorama.Fore.MAGENTA+"$> ")
#             dbcursor = connectdb.cursor()
#             dbcursor.execute(f"CREATE DATABASE IF NOT EXISTS {school_name}")
#             print("To protect the database, you need to set up a root's account.")
#             rootacc_usrname = str(input("[$]usrname_root> "))
#             rootacc_usrpass = str(input("[$]usrname_rootpass> "))
#             rootacc_usrname_lower = rootacc_usrname.lower()
#             try:
#                 connectdb_updated = mysql.connector.connect(
#                     host="192.168.1.38",
#                     user="aaravmalooking",
#                     password=mysql_password,
#                     database=f"{school_name}"
#                 )
#                 cursor_updated = connectdb_updated.cursor()
#                 create_table_query = """
#                 CREATE TABLE IF NOT EXISTS teachers (
#                     usrname VARCHAR(100),
#                     usrpass VARCHAR(100) UNIQUE,
#                     usrpriv VARCHAR(100)
#                 );
#                 """
#                 cursor_updated.execute(create_table_query)
#                 insert_query = """
#                 INSERT INTO teachers (usrname, usrpass, usrpriv)
#                 VALUES (%s, %s, %s)
#                 """
#                 data_teachers= (f"{rootacc_usrname_lower}", f"{rootacc_usrpass}", "ALL")
#                 cursor_updated.execute(insert_query, data_teachers)
#             except mysql.connector.Error as e:
#                 print(f"Something went wrong {e}")
#
#
#         except mysql.connector.Error as e:
#             print(colorama.Fore.RED + f"Something went wrong: {e}" + colorama.Style.RESET_ALL)
#
#
#         except Exception as e:
#             print(colorama.Fore.RED + f"Unexpected error: {e}" + colorama.Style.RESET_ALL)

#
#
# instance = UpdatorConnector()
# instance.register()

if __name__ == "__main__":
    app = QApplication([])
    window = front_end_ui()
    window.show()
    app.exec()