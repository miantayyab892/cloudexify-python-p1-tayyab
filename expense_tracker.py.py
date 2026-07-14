# Initialize an empty list to store all expense dictionaries
expenses = []

# Infinite loop to keep the application running until user exits
while True:
    print("----Personal Expense Tracker----")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total & Breakdown")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Save & Exit")
    
    # Get user's menu choice
    choice = input("Enter your choice (1-6): ")
    
    # --- OPTION 1: Add a new expense ---
    if choice == '1':
        print("\n--- Add Expense ---")
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        description = input("Enter the description: ")
        
        # Generate a unique ID based on the current number of expenses
        expense_id = len(expenses) + 1
        
        # Create a dictionary structure for the new expense
        new_expense = {
            "id": expense_id,
            "amount": amount,
            "category": category,
            "description": description,
        }
        
        # Append the new expense dictionary to the main list
        expenses.append(new_expense)    
        print("Expense added successfully!\n")
        
    # --- OPTION 2: View all recorded expenses ---
    elif choice == '2':
        print("\n--- View Expense ---")
        # Check if the list is empty before iterating
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            # Loop through the list and print each expense details smoothly
            for exp in expenses:
                print(f"ID: {exp['id']}, Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}")
                print("-----------------------------")
        print()
            
    # --- OPTION 3: Calculate total spending ---
    elif choice == '3':
        print("\n--- View Total & Breakdown ---")
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            # Sum up all the 'amount' values from the expense dictionaries
            total_amount = sum(exp['amount'] for exp in expenses)
            print(f"Total Amount: {total_amount}")
        print()
        
    # --- OPTION 4: Filter expenses by a specific category ---
    elif choice == '4':
        print("\n--- Filter by Category ---")
        search_category = input("Enter the category to filter: ").lower()
        
        # Perform a case-insensitive sub-string search using 'in' keyword
        found_expenses = [exp for exp in expenses if search_category in exp['category'].lower()]
        
        # Display the filtered results if matches are found
        if len(found_expenses) > 0:
            print(f"\nExpenses in category '{search_category}':")
            for exp in found_expenses:
                print(f"ID: {exp['id']} | Amount: {exp['amount']} | Category: {exp['category']} | Description: {exp['description']}")
        else:
            print(f"Category '{search_category}' ka koi expense nahi mila.")
        print()
         
    # --- OPTION 5: Delete an expense using its ID ---
    elif choice == '5':
        print("\n--- Delete Expense ---")
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            expense_id = int(input("Enter the ID of the expense to delete: "))
            # Search for the expense dictionary that matches the given ID
            expense_to_delete = next((exp for exp in expenses if exp['id'] == expense_id), None)
            
            # Remove the expense from the list if it exists
            if expense_to_delete:
                expenses.remove(expense_to_delete)
                print(f"Expense with ID {expense_id} deleted successfully.")
            else:
                print(f"No expense found with ID {expense_id}.")
        print()
        
    # --- OPTION 6: Gracefully exit the program ---
    elif choice == '6':
        print("\n--- Saving and exiting ---")
        break # Terminate the while loop
        
    # Handle any invalid input outside the 1-6 range
    else:
        print("\nInvalid choice. Please try again.\n")