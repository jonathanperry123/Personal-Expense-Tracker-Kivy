from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.app import App
from datetime import datetime
import sqlite3

class UserInterface(BoxLayout):
    pass

class Expensetracker(App):
    def build(self):
        self.connection = sqlite3.connect('FinanceManager.db')
        self.create_table()
        return UserInterface()
    
    def create_table(self):
        cursor = self.connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            location TEXT NOT NULL 
                       
        )
''')
        
        self.connection.commit()

    def validate_date(self, date_text):
        for date_format in ('%Y-%m-%d', '%Y/%m/%d'):
            try:
                datetime.strptime(date_text, date_format)
                return True
            except ValueError:
                continue
        return False
    
    def insert_data(self, date_text, category, amount, location):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO expenses (date, category, amount, location) VALUES (?,?,?,?)''', (date_text,category,amount, location))
        self.connection.commit()

    def validate_and_update(self): #Calls insert_date() and validate_date()
        #Gathers inputs from 
        date = self.root.ids.date_input.text
        category = self.root.ids.category_input.text
        amount = self.root.ids.amount_input.text
        location = self.root.ids.location_input.text

        if not date or not category or not amount or not location:
            self.root.ids.error_label.text = "One or Multiple Fields left empty"
            return 

        elif self.validate_date(date):
            self.insert_data(date,category,amount,location)
            self.root.ids.error_label.text = "Transaction Successfully Added"
            return
            
        else:
            self.root.ids.error_label.text = "Date Not Formatted Correctly"
            return

    def fetch_and_print_data(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM expenses')
        rows = cursor.fetchall()
        for row in rows:
            print(row)


               

if __name__ == '__main__':
    Expensetracker().run()

#Updating to main
#Add error message when data is not correctly entered in date.
#Challenge - When adding the build function, everything dissapeared until I placed everything
