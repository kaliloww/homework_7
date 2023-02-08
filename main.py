from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.uic import loadUi
import sys 
import sqlite3
import datetime


connect = sqlite3.connect("datbase.db")
cursor = connect.cursor()
cursor.execute ("""CREATE TABLE IF NOT EXISTS orders (
    name VARCHAR(255),
    surname VARCHAR(255),
    phone_number VARCHAR(255),
    adress VARCHAR(255),
    food VARCHAR(255),
    time VARCHAR (255)
    );""")

connect.commit()

class MenuWindow(QWidget):
    def __init__(self):
        super(MenuWindow, self).__init__()
        loadUi('menu.ui', self)
        print("Ok")
class DatabaseWindow(QWidget):
    def __init__(self):
        super(DatabaseWindow , self).__init__()
        loadUi('database.ui' , self)
        cur  = connect.cursor()
        cur.execute(f"SELECT name FROM orders")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.name.addItem(res1)
            
        cur.execute(f"SELECT surname FROM orders")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.surname.addItem(res1)
            
        cur.execute(f"SELECT phone_number FROM orders")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.number.addItem(res1)
            
        cur.execute(f"SELECT adress FROM orders")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.address.addItem(res1)
            
        cur.execute(f"SELECT food FROM orders")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.food.addItem(res1)
        cur.execute(f"SELECT time FROM orders")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.time.addItem(res1)

class AdminWindow(QWidget):
    def __init__(self):
        super(AdminWindow, self).__init__()
        loadUi('admin.ui', self)
        self.confirm.clicked.connect(self.check_password)
        self.show_database = DatabaseWindow()

    def check_password(self):
        get_password = self.password.text()
        if get_password == "geeks":
            self.result.setText("Good")
            self.confirm.clicked.connect(self.show_window_database)
        else:
            self.result.setText("Incorrect")

    def show_window_database(self):
        self.show_database.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('main.ui', self)
        self.menu_window = MenuWindow()
        self.admin_window = AdminWindow()
        self.hide_input_order()
        self.order.clicked.connect(self.send_order)
        self.send.clicked.connect(self.send_order)
        self.menu.clicked.connect(self.show_menu_window)
        self.admin.clicked.connect(self.show_admin_window)

    def show_menu_window(self):
        self.menu_window.show()

    def show_admin_window(self):
        self.admin_window.show()

    def hide_input_order(self):
        self.name.hide()
        self.surname.hide()
        self.number.hide()
        self.address.hide()
        self.food.hide()
        self.send.hide()

    def show_input_order(self):
        self.name.show()
        self.surname.show()
        self.number.show()
        self.address.show()
        self.food.show()
        self.send.show()

    def send_order(self):
        self.show_input_order()
        get_name = self.name.text()
        get_surname = self.surname.text()
        get_number = self.number.text()
        get_address = self.address.text()
        get_food = self.food.text()
        print(get_name, get_surname, get_number, get_address, get_food)
     
        if [get_name , get_number , get_address ,get_food] == ['','','','']:
            print("недостоточная информация")
        else :   

            cursor = connect.cursor()
            cursor.execute(f"SELECT name FROM orders WHERE name='{get_name}';")
            res = cursor.fetchall()
            cursor.execute(f"""INSERT INTO  orders  VALUES (
            '{get_name}' , 
            '{get_surname}',
            '{get_number}',
            '{get_address}',
            '{get_food}',
            '{datetime.datetime.now()}' )""")
            connect.commit()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()