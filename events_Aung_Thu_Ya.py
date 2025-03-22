# ============== SELWYN EVENT TICKETING SYSTEM ==============
# Student Name : AUNG THU YA
# Student ID   : 1164080
# For          : COMP 636: Python Assessment
# ===========================================================
 
#region Import List
from datetime import datetime,timedelta     # datetime module is required for working with dates
from datetime import date

# Make the variables and function in set_data.py available in this code (without needing 'set_data.' prefix)
from set_data import customers,events,unique_id,display_formatted_row   
#endregion

#region Global Variable
#Student and Assessment info
v_student_id = "1164080"
v_student_name = "AUNG THU YA"
v_assement_name = "=== COMP 636: Python Assessment ==="

#Date time value
v_current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
v_today = date.today()

#Start Layout formats
double_underline_style = "="
single_underline_style = "-"
#End Layout format

#endregion

#region Student Info
def disp_student_info():
    """
    Displays the student info and current date.
    """
    display_formatted_row([f"\n{v_assement_name}"], "{: ^100}")      
    display_formatted_row(["\nStudent ID", f"{v_student_id}"], "{: <20} : {: <80}")
    display_formatted_row(["\nStudent Name", f"{v_student_name}"], "{: <20} : {: <80}") 
    display_formatted_row(["\nDate Time", f"{v_current_datetime}"], "{: <20} : {: <80}") 
    display_formatted_row([f"\n{v_assement_name}"], "{: ^100}")           
#endregion

#region Menu List
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
#endregion   
   
#region Menu 1 : List Customers    
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
#endregion

#region Menu 2 : List Customers and their Events

def list_customers_and_tickets():
    """
    Lists Customer details (including birth date), and the events they have purchased tickets to attend."""
    
    #Define title and Formatted Style
    display_formatted_column_width = "{: <30} {: <30} {: ^11} {: <30}"
    title = "===== List Customers and their Events ====="
    
    #Render the title
    display_formatted_row([title], "{: ^100}")    
    
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
        display_formatted_row(["\nCustomer ID", f"{v_customer_id}"], "{: <20} : {: <50}") 
        display_formatted_row(["\nFirst Name", f"{v_first_name}"], "{: <20} : {: <50}") 
        display_formatted_row(["\nFamily Name", f"{v_family_name}"], "{: <20} : {: <50}") 
        display_formatted_row(["\nBirth Date", f"{v_formatted_birthdate}"], "{: <20} : {: <50}") 
        display_formatted_row(["\nnEmail", f"{v_email}"], "{: <20} : {: <50}") 
   
        #Render the event list bought by customer
        list_events_by_customerid(v_customer_id)
    
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
            #Check customer bought the event
            if customer_id == p_customer_id: 
                #Set Value
                v_event_name = event_name
                v_event_date = details['event_date'].strftime("%d %b %Y")
                v_age_restriction = details['age_restriction']
                v_capacity = details['capacity']
                v_tickets_bought = tickets_bought
                
                #Get the total ticket 
                total_ticket_bought = total_ticket_bought + v_tickets_bought
                        
                #Render the list of event
                display_formatted_row([v_event_name, v_event_date, v_age_restriction, v_capacity, v_tickets_bought], display_customer_event_formatted_column_width)
    
    #Render the sub group break line
    display_formatted_row([single_underline_style*85], "{: ^85}")   
       
    #Check total ticket value is 0 then show No ticket bought else show the total ticket value bought by customer                
    if (total_ticket_bought>0):
        display_formatted_row([f"Total tickets bought : {total_ticket_bought}" ], "{:>85}")
    else:
        display_formatted_row(["*** No ticket bought ***"], "{: ^86}")       
      
    #Render the sub group break line
    display_formatted_row([single_underline_style*85], "{: ^85}")   
#endregion

#region Menu 3 : List Event Details       
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
    display_formatted_row(["Event Name"             , "Age Restriction"        , "Event Date"             , "Capacity"              , "Tickets Sold"            ], display_event_formatted_column_width)
    display_formatted_row([double_underline_style*30, double_underline_style*15, double_underline_style*14, double_underline_style*8, double_underline_style*12 ], display_event_formatted_column_width) 

    #Sorted by Event Name
    sorted_events = sorted(events.items(), key=lambda x: x[0])
    
    #Retrieve value from the list
    for event_name, details in sorted_events:
        
        #Set Value
        v_event_name = event_name
        v_event_date = details['event_date'].strftime("%d %b %Y")
        v_age_restriction = details['age_restriction']
        v_capacity = details['capacity']
        v_tickets_sold = details['tickets_sold']
        
        #Render list of the event
        display_formatted_row([v_event_name, v_age_restriction, v_event_date, v_capacity, v_tickets_sold], display_event_formatted_column_width)
    
    #Render the footer
    display_formatted_row([single_underline_style*82], "{: ^82}")     
    
    input("\nPress Enter to return to the (Menu) list ...")     
    #end   
#endregion

#region Menu 4 : Buy Tickets
def buy_tickets():
    """
    Choose a customer, then a future event, the purchase can only proceed if they meet the minimum age requirement and tickets are available """

    response = ""
    while response != "X":
        
        v_input_customer_id = input("\nPlease enter customer id: ")
        v_pass_integer = validation("int", v_input_customer_id)

        if(v_pass_integer != True):
            print("\n*** Please enter integer value (0-9), Try again : \n")
            response = "FaildValiation"
        else:
            v_found_customer = check_customer(v_input_customer_id)  
            if(v_found_customer != True):
                 print(f"\n*** Enter customer id [\"{v_input_customer_id}\"] is not found in the system,",
                        "\n If you would like to try again, enter \"Y\", othewise enter \"N\" to back to main menu\n")
                 response = input("\nPlease enter \"Y\" or \"N\" : ").upper() 
            else:
                list_event_details_by_customerid(v_input_customer_id) 
                #loop for try buy with another count or exit by enter "X"
                buy_ticket_by_selected_eventid_customerid(v_input_customer_id)

       
def check_customer(p_customer_id = "none"):
    pass

def list_event_details_by_customerid(p_customer_id = "none"):
    pass
    """
    #1- Show listing for available event respective to the selected customer 
        *(filter with 
            1) future date event, 
            2) old enough to attend
         )
    """
   
def buy_ticket_by_selected_eventid_customerid(p_event_id = "none", p_customer_id = "none"):
    pass
    """
    "Please enter the Event ID to buy the ticket"
    "Please enter the ticket count  "
     
    then check
        3* selected event has available ticket for purchase ticket amount
        if enough to buy 
            - Update the ticket in the event dict
                - show "you have bought [n] tickets successful, e-Ticket will be sent ticket to you email", route to main menu by show press enter to back to menu
        else
            show "[n] ticket is only available as of now", Please enter to buy others event or enter "X" to exit to main menu
    """
    response_buy_event_customer = ""
    while response_buy_event_customer != "X":
        pass
#endregion

#region Menu 5 : Future Events with tickets

def list_future_available_events():
    """
    List all future events that have tickets available who have purchased tickets."""
    
    #Define title and Formatted Style
    title = "===== Event Listing - Future event with available ticket ====="
    display_event_formatted_column_width = "{: <30} {: >15} {: ^14} {: >8} {: >12} {: >26}"

    #Render the title
    display_formatted_row([title], "{: ^108}")    
    
    #Render the header
    display_formatted_row([double_underline_style*30, double_underline_style*15, double_underline_style*14, double_underline_style*8, double_underline_style*12, double_underline_style*26    ], display_event_formatted_column_width) 
    display_formatted_row(["Event Name"             , "Age Restriction"        , "Event Date"             , "Capacity"              , "Tickets Sold"           , "Available Ticket As of Now" ], display_event_formatted_column_width)
    display_formatted_row([double_underline_style*30, double_underline_style*15, double_underline_style*14, double_underline_style*8, double_underline_style*12, double_underline_style*26    ], display_event_formatted_column_width) 

    #Filter with future event and available tiket event
    filtered_events = {}
    for name, details in events.items():
        if details["event_date"] > v_today and (details["capacity"] - details["tickets_sold"]) > 0:
            filtered_events[name] = details

    #Sorted by Event Date asc order
    sorted_events = dict(sorted(filtered_events.items(), key=lambda x: x[1]["event_date"], reverse=False))
     
    #Retrieve value from the list
    for event_name, details in sorted_events.items():
        
        #Set Value
        v_event_name = event_name
        v_event_date = details['event_date']
        v_age_restriction = details['age_restriction']
        v_capacity = details['capacity']
        v_tickets_sold = details['tickets_sold']
        v_tickets_available = v_capacity - v_tickets_sold     
        
        #Render list of the event
        display_formatted_row([v_event_name, v_age_restriction, v_event_date, v_capacity, v_tickets_sold, v_tickets_available], display_event_formatted_column_width)
    
    #Render the footer
    display_formatted_row([single_underline_style*82], "{: ^108}")     
    
    input("\nPress Enter to return to the (Menu) list ...")     
    #end   
#endregion

#region Menu 6 : Add New Customer
def add_new_customer():
    """
    Add a new customer to the customer list."""
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)
#endregion


#region Validation
def validation(p_validation_type = "none", p_validation_value = "none"):
    pass
#endregion
# ------------ This is the main program ------------------------

# Don't change the menu numbering or function names in this menu.
# Although you can add arguments to the function calls, if you wish.
# Repeat this loop until the user enters an "X" or "x"

disp_student_info()

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

