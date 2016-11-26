#Benjamin Ramirez
#creating a PyQt UI that will interface with a MySQL Database
#November 23 2016

import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from GLOBALS import *
from DBConnect import MyDB


class Window(QDialog):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,WINDOW_LENGTH, WINDOW_HEIGHT)
        self.mainLayout = QVBoxLayout()
        self.setWindowTitle("A9 AeroDB GUI")
        self.setWindowIcon(QIcon('pythonlogo.png'))

        self.create_main_display()

        self.setLayout(self.mainLayout)
        self.show()

    def create_main_display(self):
        self.db_connection_fields()
        self.query_text_fields()

    def db_connection_fields(self):
        self.db_connection_row = QGroupBox("DB Connection Params")
        layout = QHBoxLayout()

        self.host_textbox = QLineEdit(self)
        self.host_textbox.baseSize()
        self.host_textbox.setPlaceholderText("Host (ex: 'localhost')")
        layout.addWidget(self.host_textbox)

        self.user_textbox = QLineEdit(self)
        self.user_textbox.baseSize()
        self.user_textbox.setPlaceholderText("UserName (ex: 'root')")
        layout.addWidget(self.user_textbox)

        self.password_textbox = QLineEdit(self)
        self.password_textbox.baseSize()
        self.password_textbox.setPlaceholderText("Password")
        layout.addWidget(self.password_textbox)

        self.database_textbox = QLineEdit(self)
        self.database_textbox.baseSize()
        self.database_textbox.setPlaceholderText("DB Name ('aerodb')")
        layout.addWidget(self.database_textbox)

        connect_button = QPushButton("Connect")
        connect_button.clicked.connect(self.connect_DB)
        layout.addWidget(connect_button)

        self.db_connection_row.setLayout(layout)
        self.mainLayout.addWidget(self.db_connection_row)


    def connect_DB(self):
        try:
            self.database = MyDB(self.host_textbox.text(),
                                 self.user_textbox.text(),
                                 self.password_textbox.text(),
                                 self.database_textbox.text())
            QMessageBox.question(self, 'ConnectionResult', "Connection SUCCESS", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.question(self, 'ConnectionResult', "Connection FAILED", QMessageBox.Ok, QMessageBox.Ok)

    def query_text_fields(self):
        self.sql_textbox = QLineEdit(self)
        self.mainLayout.addWidget(self.sql_textbox)

        execute_button = QPushButton('ExecuteSQL!')
        execute_button.clicked.connect(self.run_query)
        self.mainLayout.addWidget(execute_button)

    def run_query(self):
        self.database.execute_query(self.sql_textbox.text())
        try:
            for result in self.database.cursor.fetchall():
                print(result['Type'])
        except:
            QMessageBox.question(self, 'The result:', "Query failed", QMessageBox.Ok, QMessageBox.Ok)



print ("starting application")
app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
