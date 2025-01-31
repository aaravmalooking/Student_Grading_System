import colorama
import os
import dotenv
import mysql.connector
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from adodbapi import connect

dotenv.load_dotenv("password_sql_server.env")
mysql_password = os.getenv("MYSQL_PASSWORD")

class login_page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grades")
        self.setGeometry(100, 100, 1400, 800)
        self.resize(1400, 800)


        layout = QVBoxLayout()

        hidden_top = QPushButton("Top")
        layout.addWidget(hidden_top)


        signup = QPushButton("Login")
        layout.addWidget(signup)
        signup.setGeometry(640, 320, 200, 50)
        signup.setStyleSheet(
            "background-color: #FFFFFF; color: black; font: 14pt Homemade Apple; border-radius: 146px;"
        )
        # You can connect the button to a function if needed
        # signup.clicked.connect(self.stop_capture)

        # Create the "Register" button and add it to the layout
        register = QPushButton("Register")
        layout.addWidget(register)

        # Hide the "Top" button
        hidden_top.hide()

        # Set the layout to the central widget of the QMainWindow
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# class backend:
#     connect_db = mysql.connector.connect(
#         host="192.168.1.38",
#         user="aaravmalooking",
#         password=mysql_password
#     )
#     cursor_0 = connect_db.cursor()
#







if __name__ == "__main__":
    app = QApplication([])
    window = login_page()
    window.show()
    app.exec()