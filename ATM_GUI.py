from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty #Ask about this
from kivy.core.window import Window 

#Changing the background color
Window.clearcolor = (1,0,1,1)

class UserInterface(FloatLayout):
    #Initialize a balance attribute with a default value of 0
    balance = NumericProperty(0)
    
    


    def __init__(self, **kwargs):
        super(UserInterface, self).__init__(**kwargs)

        #balance is being binded to the on_balance_change function. Meaning, whenever balance changes, its called. 
        self.bind(balance = self.on_balance_change)

        #Initializing  Balance
        self.balance = 1000

    def deposit_money(self):
        self.balance +=float(self.ids.amount_input.text)
        

    #App won't go below $0
    def withdraw_money(self):
        self.balance -= float(self.ids.amount_input.text)
            

    def on_balance_change(self, instance, value):
        #This method is called automatically whenever 'balance' changes
        #Perform your complex operations here
        #Example: Updating a label with the new balance

       
        if self.balance >= 0:
            self.ids.balance_label.text = f"Balance: ${value}"
        else:
            self.ids.balance_label.text = f"You need more money. Your account is overdrafted by ${value * -1}"


        

class BankApp(App):
    def build(self):
        return UserInterface()
    

        

BankApp().run()

#I want a label to show the current balance of the account. 
#Labels only accept strings as input. 

#Things to learn about BEFORE going any further:
    #Binding labels, attribute referencing, correct defining of functions in scope
    #super function, build function, func(self, instance, value)
    #Properties. 
    #root, referencing, ids in labels.
    #When do I establish a property. Like why didn't I have to do so for the amount_input box. 
    
        
