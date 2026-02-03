import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, acc_num, acc_type, user):
        self.acc_num = acc_num
        self.acc_type = acc_type
        self.user = user
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"₹{amount} deposited successfully"
        return "Invalid amount"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"₹{amount} withdrawn successfully"

    def check_balance(self):
        return f"Current Balance: ₹{self.balance}"


account = None

def create_account():
    global account
    try:
        acc = int(acc_entry.get())
        acc_type = type_entry.get()
        name = name_entry.get()
        account = Account(acc, acc_type, name)
        messagebox.showinfo("Success", "Account created successfully")
    except:
        messagebox.showerror("Error", "Enter valid details")

def deposit_money():
    try:
        amt = int(amount_entry.get())
        messagebox.showinfo("Deposit", account.deposit(amt))
    except:
        messagebox.showerror("Error", "Invalid amount")

def withdraw_money():
    try:
        amt = int(amount_entry.get())
        messagebox.showinfo("Withdraw", account.withdraw(amt))
    except:
        messagebox.showerror("Error", "Invalid amount")

def show_balance():
    messagebox.showinfo("Balance", account.check_balance())


root = tk.Tk()
root.title("Python Banking System")
root.geometry("350x400")

tk.Label(root, text="Banking System", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Account Number").pack()
acc_entry = tk.Entry(root)
acc_entry.pack()

tk.Label(root, text="Account Type").pack()
type_entry = tk.Entry(root)
type_entry.pack()

tk.Label(root, text="User Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Button(root, text="Create Account", command=create_account).pack(pady=5)

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Deposit", command=deposit_money).pack(pady=5)
tk.Button(root, text="Withdraw", command=withdraw_money).pack(pady=5)
tk.Button(root, text="Check Balance", command=show_balance).pack(pady=5)

root.mainloop()
