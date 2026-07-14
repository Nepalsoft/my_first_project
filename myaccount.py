import datetime

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0.0):
        """Initializes a new bank account with account details and initial balance."""
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transactions = []  # List to store all transaction history
        
        # Record the initial deposit as the first transaction
        self._record_transaction("Account Opened", initial_balance)

    def _record_transaction(self, action_type, amount):
        """Internal method to log each transaction with a real-time timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction_log = {
            "timestamp": timestamp,
            "description": action_type,
            "amount": f"${amount:,.2f}",
            "balance_after": f"${self.balance:,.2f}"
        }
        self.transactions.append(transaction_log)

    def deposit(self, amount):


        This program is designed for handle Bank account of school management and teacher
        to make easy for the parents of students 
        
        """Deposits a specified amount into the account."""
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return
        
        self.balance += amount
        print(f"Success: Deposited ${amount:,.2f}")
        self._record_transaction("Deposit", amount)

    def withdraw(self, amount):
        """Withdraws a specified amount from the account if funds are sufficient."""
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print(f"Error: Insufficient funds! Current balance is ${self.balance:,.2f}")
            return
        
        self.balance -= amount
        print(f"Success: Withdrew ${amount:,.2f}")
        self._record_transaction("Withdrawal", amount)

    def display_statement(self):
        """Prints a clean, formatted bank statement showing full transaction history."""
        print("\n" + "="*75)
        print(f"                           BANK STATEMENT                          ")
        print("="*75)
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Current Balance: ${self.balance:,.2f}")
        print("-"*75)
        
        # Table Headers
        print(f"{'Date & Time':<20} | {'Description':<20} | {'Amount':<12} | {'Available Balance'}")
        print("-"*75)
        
        # Display each logged transaction
        for txn in self.transactions:
            print(f"{txn['timestamp']:<20} | {txn['description']:<20} | {txn['amount']:<12} | {txn['balance_after']}")
        print("="*75 + "\n")


# --- System Testing ---

# 1. Create a new bank account (Holder: John Doe, Starting Balance: $5,000)
customer_acc = BankAccount(account_number="987654321", holder_name="John Doe", initial_balance=5000.0)

# 2. Perform various banking transactions
customer_acc.deposit(2500.0)    # Deposit $2,500
customer_acc.withdraw(1200.0)   # Withdraw $1,200
customer_acc.deposit(10000.0)   # Deposit $10,000
customer_acc.withdraw(4000.0)    # Withdraw $4,000

# 3. Print the final account statement
customer_acc.display_statement()
