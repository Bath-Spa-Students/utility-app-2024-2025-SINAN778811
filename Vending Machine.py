#Importing tkinter to create a GUI
from tkinter import Tk, Label, Button, Entry, StringVar

#Defining the VendingMachine class
class VendingMachine:
    def __init__(self, root):
        #Initializing the main window
        self.root = root
        self.root.title("Vending Machine")

        #Defining a dictionary to store items in the vending machine
        self.items = {
            "A1": {"name": "Soda", "price": 2.50, "stock": 10},  
            "A2": {"name": "Chips", "price": 1.50, "stock": 15},
            "A3": {"name": "Candy", "price": 1.75, "stock": 20},
            "A4": {"name": "Snickers", "price": 3.75, "stock": 10},
            "A5": {"name": "laban", "price": 0.75, "stock": 10},
        }

        #Variables to store user input and messages
        self.selected_code = StringVar()  
        self.payment = StringVar()       
        self.message = StringVar()  

        #Create GUI widgets
        self.create_widgets()

    #Method to create widgets for the GUI
    def create_widgets(self):
        #Label to display items
        Label(self.root, text="Available Items:").grid(row=0, column=0, columnspan=2)

        #Loop to display each item 
        row = 1
        for code, details in self.items.items():
            name, price, stock = details.values()
            Label(self.root, text=f"{code}: {name} - $ {price:.2f} ({stock} left)").grid(row=row, column=0, columnspan=2, sticky="w")
            row += 1

        #Input field to enter the item code
        Label(self.root, text="Enter Code:").grid(row=row, column=0, sticky="e")
        Entry(self.root, textvariable=self.selected_code).grid(row=row, column=1, sticky="w")
        row += 1

        #Input field to enter the payment amount
        Label(self.root, text="Enter Payment:").grid(row=row, column=0, sticky="e")
        Entry(self.root, textvariable=self.payment).grid(row=row, column=1, sticky="w")
        row += 1

        #Button to initiate the purchase process
        Button(self.root, text="Purchase", command=self.vend_item).grid(row=row, column=0, columnspan=2)
        row += 1

        #Label to display messages to the user
        Label(self.root, textvariable=self.message, fg="blue").grid(row=row, column=0, columnspan=2)

    #Method to handle the vending process
    def vend_item(self):
        #Retrieve the entered item code and convert it to uppercase
        code = self.selected_code.get().upper()

        #Validate the entered payment amount
        try:
            payment = float(self.payment.get())
        except ValueError:
            self.message.set("Invalid payment amount. Please enter a number.")
            return

        #Check if the entered code exists in the items dictionary
        if code not in self.items:
            self.message.set("Invalid selection. Please choose a valid code.")
            return

        #Retrieve the item details
        item = self.items[code]

        #Check if the item is in stock
        if item["stock"] <= 0:
            self.message.set(f"{item['name']} is out of stock. Please choose another item.")
            return

        #Check if the payment is sufficient
        if payment < item["price"]:
            self.message.set(f"Insufficient funds. {item['name']} costs $ {item['price']:.2f}.")
            return

        #Calculate change and update stock
        change = payment - item["price"]
        item["stock"] -= 1
        #Display success message with change
        self.message.set(f"Dispensing {item['name']}. Your change is $ {change:.2f}.")

if __name__ == "__main__":
    #Create the main application window
    root = Tk()
    vending_machine = VendingMachine(root)
    #Run the application
    root.mainloop()
