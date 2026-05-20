# Expense Tracker CLI

A simple command-line application to track income and expenses.

## Features

- **Add Entries**: Add income and expense entries with date, category, and amount.
- **Monthly Summary**: View a summary of total income, total expenses, and the balance for a specific month.
- **Data Export**: Export all transaction data to either a CSV or an Excel file.
- **Expense Chart**: Automatically generates and saves a pie chart visualizing the distribution of expenses for the selected month.

## How to Run

1.  **Install Dependencies**:
    Make sure you have Python installed. Then, install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application**:
    Execute the main script from your terminal:
    ```bash
    python app.py
    ```

3.  **Follow On-screen Instructions**:
    The application will present a menu with the following options:
    - `1. Add Entry (Income/Expense)`: To add a new transaction.
    - `2. View Monthly Summary`: To see a summary and a chart for a specific month.
    - `3. Export Data`: To save all your data in a file.
    - `4. Exit`: To close the application.

## File Structure

- `app.py`: The main script for the application.
- `requirements.txt`: A list of Python packages required for the project.
- `expenses.csv`: The default database file where all income and expense entries are stored.
- `monthly_summary.png`: The image file for the generated expense chart.
- `export.csv` / `export.xlsx`: The files generated when you choose to export your data.
