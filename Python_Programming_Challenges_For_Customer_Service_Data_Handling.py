#task1
service_tickets = {
    "1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket():
    ticket_number = input("Enter a unique ticket number: ")
    if ticket_number in service_tickets:
        print("This ticket number already exists. Please use a unique ID.")
        return
    
    customer_name = input("Enter the customer's name: ")
    issue_description = input("Describe the issue: ")
    
    service_tickets[ticket_number] = {
        "Customer": customer_name,
        "Issue": issue_description,
        "Status": "open"
    }
    print(f"New ticket {ticket_number} created successfully!")

def status_update():
    ticket_number = input("Enter the ticket number you want to update: ")
    if ticket_number not in service_tickets:
        print("Ticket not found. Please enter a valid ticket number.")
        return
    
    new_status = input("Enter the new status (open/closed): ").lower()
    if new_status not in ["open", "closed"]:
        print("Invalid status. Please enter 'open' or 'closed'.")
        return
    
    service_tickets[ticket_number]["Status"] = new_status
    print(f"Ticket {ticket_number} status updated to {new_status}.")

def display_ticket():
    if not service_tickets:
        print("No tickets to display.")
        return
    
    print("\nDisplaying all tickets:")
    for ticket_number, details in service_tickets.items():
        print(f"{ticket_number}: {details}")


while True:
    print("\nWelcome to the Customer Service Ticket Tracker")
    print("\n1. Open a new ticket\n2. Update the status of a ticket\n3. Display all tickets\n4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        open_ticket()
    elif choice == "2":
        status_update()
    elif choice == "3":
        display_ticket()
    elif choice == "4":
        print("Exiting program now...")
        break
    else:
        print("Enter a valid number. Try again.")
