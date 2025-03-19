# ============== SELWYN EVENT TICKETING SYSTEM ==============
# Student Name: AUNG THU YA
# Student ID : 1164080
# ================================================================
 
from datetime import datetime,timedelta     # datetime module is required for working with dates

# Make the variables and function in set_data.py available in this code (without needing 'set_data.' prefix)
from set_data import customers,events,unique_id,display_formatted_row   

#Start Layout format
format_line_str = "{: <100}"
line_style_str = "="  
format_line_width = 100 
#End Layout format


def list_all_customers():
    """
    Lists customer details.
    This is an example of how to produce basic output."""
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <20}"            # Use the same format_str for column headers and rows to ensure consistent spacing. 
    display_formatted_row(["ID","First Name","Family Name","Birth Date","e-Mail"],format_str)     # Use the display_formatted_row() function to display the column headers with consistent spacing
    for customer in customers:
        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        email = customer[4]

        display_formatted_row([id,fname,famname,birthdate,email],format_str)     # Use the display_formatted_row() function to display each row with consistent spacing
    input("\nPress Enter to continue.")

def list_customers_and_tickets():
    """
    Lists Customer details (including birth date), and the events they have purchased tickets to attend."""
    input("\nPress Enter to continue.")

def list_event_details():
    """
    List the events, show all details except Customers who have purchased tickets."""
    
    #start
    format_event_header_str = "{: <20}"
    format_event_details_str = "{: <20}" 
    

    for event_name, event_details in sorted(events.items()):
        print("\n")
        v_event_name = {event_name}
        display_formatted_row([v_event_name],format_event_header_str)
        display_formatted_row([line_style_str],format_line_str)
         
        for v_event_details in sorted(event_details.items()):
            v_age_restriction_str = {v_event_details[0]} #set age_restriction
            #v_event_date_date = {v_event_details[1]} #set event_date
            #v_capacity_int = {v_event_details[2]} #set capacity
            #v_tickets_sold_int = {v_event_details[3]} #set tickets_sold
            
            display_formatted_row([v_age_restriction_str],format_event_details_str)
        
    input("\nPress Enter to continue.")     
    #end   

def buy_tickets():
    """
    Choose a customer, then a future event, the purchase can only proceed if they meet the minimum age requirement and tickets are available """
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def add_new_customer():
    """
    Add a new customer to the customer list."""
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def list_future_available_events():
    """
    List all future events that have tickets available
    """
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)


def disp_menu():
    """
    Displays the menu and current date.  No parameters required.
    """
    print("==== WELCOME TO SELWYN EVENT TICKETING SYSTEM ===")
    print(" 1 - List Customers")
    print(" 2 - List Customers and their Events")
    print(" 3 - List Event Details")
    print(" 4 - Buy Tickets")
    print(" 5 - Future Events with tickets")
    print(" 6 - Add New Customer")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Don't change the menu numbering or function names in this menu.
# Although you can add arguments to the function calls, if you wish.
# Repeat this loop until the user enters an "X" or "x"
response = ""
while response != "X":
    disp_menu()
    # Display menu for the first time, and ask for response
    response = input("Please enter menu choice: ").upper()    
    if response == "1":
        list_all_customers()
    elif response == "2":
        list_customers_and_tickets()
    elif response == "3":
        list_event_details()
    elif response == "4":
        buy_tickets()
    elif response == "5":
        list_future_available_events()
    elif response == "6":
        add_new_customer()
    elif response != "X":
        print("\n*** Invalid response, please try again (enter 1-6 or X)\n")
print("\n=== Thank you for using the SELWYN EVENT TICKET SYSTEM! ===\n")

