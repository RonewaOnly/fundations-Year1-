import csv ## For handling CSV file operations

class PersonalFinanceTracker:
    LIST_OF_CATEGORIES = ['Income', 'Expense', 'Investment', 'Savings']
    MONTHY_BUDGET_LIMITS = {
        'Income': 10000,
        'Expense': 3000,
        'Investment': 1000,
        'Savings': 3000
    }
    def __init__(self, filename='finance_data.csv'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Loads financial data from a CSV file.

        Returns:
            list: A list of dictionaries representing financial records.
        """
        data = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
            print(f"Financial data loaded from {self.filename}.")
        except FileNotFoundError:
            print(f"No existing finance file found. Starting with an empty dataset.")
        return data

    def save_data(self):
        """Saves the current financial data to a CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['Date', 'Description', 'Amount', 'Category']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for record in self.data:
                writer.writerow(record)
        print(f"Financial data saved to {self.filename}.")

    def add_record(self, date, description, amount, category):
        """Adds a new financial record.

        Args:
            date (str): The date of the transaction.
            description (str): A description of the transaction.
            amount (float): The amount of the transaction.
            category (str): The category of the transaction.
        """
        new_record = {
            'Date': date,
            'Description': description,
            'Amount': amount,
            'Category': category
        }
        self.data.append(new_record)
        print(f"Added new record: {new_record}")

    def delete_record(self, index):
        """Deletes a financial record by its index.

        Args:
            index (int): The index of the record to delete.
        """
        if 0 <= index < len(self.data):
            removed_record = self.data.pop(index)
            print(f"Removed record: {removed_record}")
        else:
            print("Invalid index. No record removed.")
            
    def view_records(self):
        """Displays all financial records."""
        for i, record in enumerate(self.data):
            print(f"{i}: {record}")
    
    def monitor_budget(self):
        """Monitors the budget against predefined limits."""
        totals = {category: 0 for category in self.LIST_OF_CATEGORIES}
        for record in self.data:
            category = record['Category']
            amount = float(record['Amount'])
            if category in totals:
                totals[category] += amount
        
        for category, total in totals.items():
            limit = self.MONTHY_BUDGET_LIMITS.get(category, float('inf'))
            if total > limit:
                print(f"Alert: {category} has exceeded the budget limit! Total: {total}, Limit: {limit}")
            else:
                print(f"{category}: Total = {total}, Limit = {limit}")



def main():
    tracker = PersonalFinanceTracker()
    
    name = input("Enter your name: ")
    print(f"Welcome, {name}, to your Personal Finance Tracker!")
    
    while True:
        
        menu = int(
            input("""
                    1. Add Record
                    2. View Records
                    3. Delete Record
                    4. Save Data
                    5. Monitor Budget
                    6. Exit
                """))
    
        if menu == 1:
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input(f"Enter category ({', '.join(tracker.LIST_OF_CATEGORIES)}): ")
            tracker.add_record(date, description, amount, category)
        elif menu == 2:
            tracker.view_records()
        elif menu == 3:
            index = int(input("Enter the index of the record to delete: "))
            tracker.delete_record(index)
        elif menu == 4:
            tracker.save_data()
        elif menu == 5:
            tracker.monitor_budget()
        elif menu == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main() ## Run the main function to start the program