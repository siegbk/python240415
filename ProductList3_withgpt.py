import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3
import os

class ProductDatabase:
    def __init__(self, db_path="ProductList.db"):
        self.db_path = db_path
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()
        self._initialize_database()
    
    def _initialize_database(self):
        if not os.path.exists(self.db_path):
            self.cur.execute("CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);")
            self.con.commit()

    def add_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, prod_id))
        self.con.commit()

    def remove_product(self, prod_id):
        self.cur.execute("DELETE FROM Products WHERE id=?;", (prod_id,))
        self.con.commit()

    def fetch_all_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()


class Window(QMainWindow):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setupUi()
        self._initialize_ui()
        
    def setupUi(self):
        uic.loadUi("ProductList3.ui", self)
        
    def _initialize_ui(self):
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.on_table_double_click)
        self.load_products()
        
    def add_product(self):
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.database.add_product(name, price)
        self.load_products()
        
    def update_product(self):
        prod_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.database.update_product(prod_id, name, price)
        self.load_products()

    def remove_product(self):
        prod_id = self.prodID.text()
        self.database.remove_product(prod_id)
        self.load_products()

    def load_products(self):
        self.tableWidget.clearContents()
        products = self.database.fetch_all_products()
        for row, product in enumerate(products):
            prod_id, name, price = product
            self._add_product_to_table(row, prod_id, name, price)
        
    def _add_product_to_table(self, row, prod_id, name, price):
        item_id = QTableWidgetItem(str(prod_id))
        item_id.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(row, 0, item_id)
        
        item_name = QTableWidgetItem(name)
        self.tableWidget.setItem(row, 1, item_name)
        
        item_price = QTableWidgetItem(str(price))
        item_price.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(row, 2, item_price)
        
    def on_table_double_click(self):
        current_row = self.tableWidget.currentRow()
        self.prodID.setText(self.tableWidget.item(current_row, 0).text())
        self.prodName.setText(self.tableWidget.item(current_row, 1).text())
        self.prodPrice.setText(self.tableWidget.item(current_row, 2).text())

def main():
    app = QApplication(sys.argv)
    database = ProductDatabase()
    window = Window(database)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
