from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.app import App
from datetime import datetime

class UserInterface(BoxLayout):
    pass

class ExpenseTracker(App):
    
    def validate_and_print(self):
        date = self.root.ids.date_input
        category = self.root.ids.category_input

        amount = self.root.ids.amount_input
        location = self.root.ids.location_input

        amount = amount.text
        date_text = date.text

        if self.validate_date(date_text):
            print(f"Amount {amount}")
            print(f"Date: {date_text}")
        else:
            print("Invalid date format. Please enter date in YYYY-MM-DD")


    def validate_date(self,date_text):
        try:
            datetime.strptime(date_text,'%Y-%m-%d')
            return True
        except ValueError:
            return False
        

if __name__ == '__main__':
    ExpenseTracker().run()