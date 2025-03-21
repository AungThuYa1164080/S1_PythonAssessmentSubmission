# ============== SELWYN EVENT TICKETING SYSTEM ==============
# Student Name: AUNG THU YA
# Student ID : 1164080
# ================================================================
 
from datetime import datetime,timedelta     # datetime module is required for working with dates

# Make the variables and function in set_data.py available in this code (without needing 'set_data.' prefix)
from set_data import customers,events,unique_id,display_formatted_row   

#Start Layout format
double_underline_style = "="
single_underline_style = "-"
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
    
    #Define title and Formatted Style
    display_formatted_column_width = "{: <30} {: <30} {: ^11} {: <30}"
    title = "===== List Customers and their Events ====="
    
    #Render the title
    display_formatted_row([title], "{: ^100}")    
    
    #Render the header
    #N.A
    
    #Sorted for customer listing ordered by family name, then first name
    customers_sorted = sorted(customers, key=lambda x: (x[2], x[1]))
    
    #Retrieve customer list    
    for customer in customers_sorted:
        v_customer_id = customer[0]
        v_first_name = customer[1]
        v_family_name = customer[2]
        v_birthdate = customer[3]
        v_email = customer[4]
        v_formatted_birthdate = v_birthdate.strftime("%d %b %Y")

        #Render Customer Info
        print(f"\n Customer ID : {v_customer_id}") 
        print(f"\n First Name  : {v_first_name}")
        print(f"\n Family Name : {v_family_name}") 
        print(f"\n Birth Date  : {v_formatted_birthdate}")  
        print(f"\n Email       : {v_email}") 
        
        #Render the event list bought by customer
        list_events_by_customerid(v_customer_id)
        
        display_formatted_row([double_underline_style*30], "{: ^85}") 
    #Render the footer
    display_formatted_row([single_underline_style*85], "{: ^85}")     
    
    input("\nPress Enter to return to the (Menu) list ...")     
    #end   
    
def list_events_by_customerid(p_customer_id):
    #Variables
    total_ticket_bought = 0
    
    #Define Formatted Style
    display_customer_event_formatted_column_width = "{: <30} {: ^15} {: >14} {: >8} {: >14}"
        
    #Render the header
    display_formatted_row([double_underline_style*30, double_underline_style*14, double_underline_style*15,  double_underline_style*8, double_underline_style*14 ], display_customer_event_formatted_column_width) 
    display_formatted_row(["Event Name"             , "Event Date"             , "Age Restriction"        ,  "Capacity"              , "Ticket Bought"           ], display_customer_event_formatted_column_width)
    display_formatted_row([double_underline_style*30, double_underline_style*14, double_underline_style*15,  double_underline_style*8, double_underline_style*14 ], display_customer_event_formatted_column_width) 

    #Sorted by Event Name
    sorted_events = sorted(events.items(), key=lambda x: x[0])
   
    #Get the list of event bought by customer
    for event_name, details in sorted_events:
        for customer_id, tickets_bought in details["customers"]:
            if customer_id == p_customer_id:
                #Set Value
                
                v_event_name = event_name
                v_event_date = details['event_date']
                v_age_restriction = details['age_restriction']
                v_capacity = details['capacity']
                v_tickets_bought = tickets_bought
                 
                total_ticket_bought = total_ticket_bought + v_tickets_bought
                        
                #Render into the row
                display_formatted_row([v_event_name, v_event_date, v_age_restriction, v_capacity, v_tickets_bought], display_customer_event_formatted_column_width)
    
                    
    if (total_ticket_bought>0):
        display_formatted_row([f"\nTotal tickets bought : {total_ticket_bought}" ], "{: <86}")
    else:
        display_formatted_row(["*** No ticket bought ***"], "{: ^86}")       
        
        
def list_event_details():
    """
    List the events, show all details except Customers who have purchased tickets."""
    
    #Define title and Formatted Style
    title = "===== Event Details Listing ====="
    display_event_formatted_column_width = "{: <30} {: >15} {: ^14} {: >8} {: >12}"

    #Render the title
    display_formatted_row([title], "{: ^82}")    
    
    #Render the header
    display_formatted_row([double_underline_style*30, double_underline_style*15, double_underline_style*14, double_underline_style*8, double_underline_style*12 ], display_event_formatted_column_width) 
    display_formatted_row(["Event Name"         , "Age Restriction"    , "Event Date"         , "Capacity"          , "Tickets Sold"        ], display_event_formatted_column_width)
    display_formatted_row([double_underline_style*30, double_underline_style*15, double_underline_style*14, double_underline_style*8, double_underline_style*12 ], display_event_formatted_column_width) 

    #Sorted by Event Name
    sorted_events = sorted(events.items(), key=lambda x: x[0])
    
    #Retrieve value from the list
    for event_name, details in sorted_events:
        
        #Set Value
        v_event_name = event_name
        v_event_date = details['event_date']
        v_age_restriction = details['age_restriction']
        v_capacity = details['capacity']
        v_tickets_sold = details['tickets_sold']
        
        #Render into the row
        display_formatted_row([v_event_name, v_age_restriction, v_event_date, v_capacity, v_tickets_sold], display_event_formatted_column_width)
    
    #Render the footer
    display_formatted_row([single_underline_style*82], "{: ^82}")     
    
    input("\nPress Enter to return to the (Menu) list ...")     
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
    print("\n\n==== WELCOME TO SELWYN EVENT TICKETING SYSTEM ===")
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
    response = input("\nPlease enter menu choice: ").upper() 
       
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

