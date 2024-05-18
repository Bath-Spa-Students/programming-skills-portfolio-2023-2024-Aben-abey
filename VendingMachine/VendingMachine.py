print('''
       __      _____________.____   _________  ________      _____  ___________ ___________________       _____ _____.___.                  
/  \    /  \_   _____/|    |  \_   ___ \ \_____  \    /     \ \_   _____/ \__    ___/\_____  \     /     \\__  |   |                  
\   \/\/   /|    __)_ |    |  /    \  \/  /   |   \  /  \ /  \ |    __)_    |    |    /   |   \   /  \ /  \/   |   |                  
 \        / |        \|    |__\     \____/    |    \/    Y    \|        \   |    |   /    |    \ /    Y    \____   |                  
  \__/\  / /_______  /|_______ \______  /\_______  /\____|__  /_______  /   |____|   \_______  / \____|__  / ______|                  
       \/          \/         \/      \/         \/         \/        \/                     \/          \/\/                         
____   _______________ _______  ________  .___ _______    ________     _____      _____  _________   ___ ___ .___ _______  ___________
\   \ /   /\_   _____/ \      \ \______ \ |   |\      \  /  _____/    /     \    /  _  \ \_   ___ \ /   |   \|   |\      \ \_   _____/
 \   Y   /  |    __)_  /   |   \ |    |  \|   |/   |   \/   \  ___   /  \ /  \  /  /_\  \/    \  \//    ~    \   |/   |   \ |    __)_ 
  \     /   |        \/    |    \|    `   \   /    |    \    \_\  \ /    Y    \/    |    \     \___\    Y    /   /    |    \|        \
   \___/   /_______  /\____|__  /_______  /___\____|__  /\______  / \____|__  /\____|__  /\______  /\___|_  /|___\____|__  /_______  /
                   \/         \/        \/            \/        \/          \/         \/        \/       \/             \/        \/
       ''')

class VendingMachine:
    def __init__(self):
        self.menu = {
            1: {"item": "Coke", "price": 1.50},
            2: {"item": "Chips", "price": 1.00},
            3: {"item": "Candy", "price": 0.75},
            4: {"item": "Water", "price": 1.00},
            5: {"item": "Juice", "price": 1.25},
            6: {"item": "Sandwich", "price": 2.50},
            7: {"item": "Cookies", "price": 1.50},
            8: {"item": "Granola Bar", "price": 1.00},
            9: {"item": "Gum", "price": 0.50},
            10: {"item": "Coffee", "price": 1.75}
        }
        self.balance = 0.0
        self.purchased_items = []

    def display_menu(self):
        print("Menu:")
        for key, value in self.menu.items():
            print(f"{key}: {value['item']} - ${value['price']}")

    def select_item(self, choice):
        if choice in self.menu:
            item = self.menu[choice]["item"]
            price = self.menu[choice]["price"]
            if self.balance >= price:
                self.balance -= price
                self.purchased_items.append(item)
                print(f"Enjoy your {item}!")
            else:
                print("Insufficient balance. Please add more money.")
        else:
            print("Invalid selection.")

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} added. Your balance is now ${self.balance:.2f}.")
        else:
            print("Invalid amount.")

def main():
    machine = VendingMachine()
    
    while True:
        print("\nWhat would you like to do?")
        print("1: Display menu")
        print("2: Add money")
        print("3: Select item")
        print("4: Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            machine.display_menu()
        elif choice == "2":
            amount = float(input("Enter the amount to add: $"))
            machine.add_money(amount)
        elif choice == "3":
            item_choice = int(input("Enter the item number you wish to purchase: "))
            machine.select_item(item_choice)
        elif choice == "4":
            print("Thank you for using the vending machine. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

    print("\nSummary of your purchases:")
    for item in machine.purchased_items:
        print(f"- {item}")
    print(f"Remaining balance: ${machine.balance:.2f}")

    print('''______________ ___    _____    _______   ____  __. _____.___.________   ____ ___ 
\__    ___/   |   \  /  _  \   \      \ |    |/ _| \__  |   |\_____  \ |    |   \
  |    | /    ~    \/  /_\  \  /   |   \|      <    /   |   | /   |   \|    |   /
  |    | \    Y    /    |    \/    |    \    |  \   \____   |/    |    \    |  / 
  |____|  \___|_  /\____|__  /\____|__  /____|__ \  / ______|\_______  /______/  
                \/         \/         \/        \/  \/               \/          
      ''')

if __name__ == "__main__":
    main()
