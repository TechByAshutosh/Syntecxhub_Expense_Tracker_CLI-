import csv
import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = 'expenses.csv'
CHART_FILE = 'monthly_summary.png'

def initialize_data_file():
    """Creates the data file with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'category', 'amount', 'type'])

def add_entry():
    """Adds a new income or expense entry."""
    date_str = input("Enter date (YYYY-MM-DD, default: today): ")
    if not date_str:
        date = datetime.date.today()
    else:
        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    category = input("Enter category: ")
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    while True:
        entry_type = input("Enter type (income/expense): ").lower()
        if entry_type in ['income', 'expense']:
            break
        else:
            print("Invalid type. Please enter 'income' or 'expense'.")

    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, entry_type])
    print("Entry added successfully.")

def get_monthly_summary(year, month):
    """
    Calculates and returns the total income, total expense, and balance for a given month.
    """
    try:
        df = pd.read_csv(DATA_FILE)
        df['date'] = pd.to_datetime(df['date'])
        
        month_df = df[(df['date'].dt.year == year) & (df['date'].dt.month == month)]
        
        total_income = month_df[month_df['type'] == 'income']['amount'].sum()
        total_expense = month_df[month_df['type'] == 'expense']['amount'].sum()
        balance = total_income - total_expense
        
        return total_income, total_expense, balance, month_df
    except FileNotFoundError:
        return 0, 0, 0, pd.DataFrame()


def view_monthly_summary():
    """Displays the monthly summary."""
    try:
        year = int(input("Enter year (e.g., 2023): "))
        month = int(input("Enter month (1-12): "))
        if not 1 <= month <= 12:
            print("Invalid month. Please enter a number between 1 and 12.")
            return
    except ValueError:
        print("Invalid input. Please enter numbers for year and month.")
        return

    total_income, total_expense, balance, month_df = get_monthly_summary(year, month)

    print(f"\n--- Monthly Summary for {year}-{month:02d} ---")
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expense: {total_expense:.2f}")
    print(f"Balance: {balance:.2f}")
    print("------------------------------------")
    
    if not month_df.empty:
        print("Entries for the month:")
        print(month_df.to_string(index=False))
        
        # Generate and save chart
        generate_chart(year, month, month_df)


def generate_chart(year, month, df):
    """Generates and saves a pie chart of expenses for the month."""
    expense_df = df[df['type'] == 'expense']
    if not expense_df.empty:
        category_summary = expense_df.groupby('category')['amount'].sum()
        
        plt.figure(figsize=(8, 8))
        plt.pie(category_summary, labels=category_summary.index, autopct='%1.1f%%', startangle=140)
        plt.title(f'Expense Distribution for {year}-{month:02d}')
        plt.ylabel('') # Hides the 'None' label on y-axis
        plt.savefig(CHART_FILE)
        plt.close()
        print(f"\nChart saved to {CHART_FILE}")

def export_data():
    """Exports all data to a CSV or Excel file."""
    try:
        df = pd.read_csv(DATA_FILE)
        
        format_choice = input("Export to (csv/excel): ").lower()
        
        if format_choice == 'csv':
            filename = 'export.csv'
            df.to_csv(filename, index=False)
            print(f"Data exported to {filename}")
        elif format_choice == 'excel':
            filename = 'export.xlsx'
            df.to_excel(filename, index=False)
            print(f"Data exported to {filename}")
        else:
            print("Invalid format. Please choose 'csv' or 'excel'.")
            
    except FileNotFoundError:
        print("No data to export.")
    except Exception as e:
        print(f"An error occurred during export: {e}")


def main():
    """Main function to run the CLI app."""
    initialize_data_file()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Entry (Income/Expense)")
        print("2. View Monthly Summary")
        print("3. Export Data")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_monthly_summary()
        elif choice == '3':
            export_data()
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
