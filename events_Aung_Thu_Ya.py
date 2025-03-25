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

    #Define title and Formatted Style
    title = "===== Customer Listing ====="
    display_customer_formatted_column_width = "{: <5} {: <15} {: <15} {: ^14} {: <25}"

    #Render the title
    display_formatted_row([title], "{: ^82}")    
    
    #Render the header
    display_formatted_row([double_underline_style*5, double_underline_style*15, double_underline_style*15, double_underline_style*14, double_underline_style*25 ], display_customer_formatted_column_width) 
    display_formatted_row(["ID"             , "First Name"        , "Family Name"             , "Birth Date"              , "Email"            ], display_customer_formatted_column_width)
    display_formatted_row([double_underline_style*5, double_underline_style*15, double_underline_style*15, double_underline_style*14, double_underline_style*25 ], display_customer_formatted_column_width) 

    #Sorted by cusotmer id
    sorted_customers = sorted(customers, key=lambda x: x[0])
        
    #end
    for customer in sorted_customers:
            id = customer[0]
            fname = customer[1]
            famname = customer[2]
            birthdate = customer[3].strftime("%d %b %Y")
            email = customer[4]
    
            display_formatted_row([id,fname,famname,birthdate,email], display_customer_formatted_column_width)     # Use the display_formatted_row() function to display each row with consistent spacing

#endregion

#region Menu 2 : List Customers and their Events

def list_customers_and_tickets():
    """
    Lists Customer details (including birth date), and the events they have purchased tickets to attend."""
    
    #Define title and Formatted Style
    display_formatted_column_width = "{: <30} {: <30} {: ^11} {: <30}"
    title = "===== List Customers and Their Events ====="
    
    #Render the title
    display_formatted_row([title], "{: ^100}")    
    
    #Sorted for customer listing ordered by family name, then first name
    customers_sorted = sorted(customers, key=lambda x: (x[2], x[1]))
    
    #Retrieve customer list
    for customer in customers_sorted:
        v_customer_id = customer[0]
        
        #Render customer info deatils 
        render_customer_detail(customer)
  
        #Render the event list bought by customer
        list_events_by_customerid("all", v_customer_id)
    
    input("\nPress Enter to return to the (Menu) list ...")     

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
    #Define title and Formatted Style
    title = "===== Buy Tickets ====="
    future_eligible_title = "\n\n[!] Here is list of upcoming events and eligibility to purchase..."
    
    #Render the title
    display_formatted_row([title], "{: ^82}")  
    
    #Show list of customer
    list_all_customers()
      
    buy_ticket_response = ""
    while buy_ticket_response != "X":
        
        v_input_customer_id = input("\nPlease enter customer id: ")
        v_pass_integer = validation("IsDigit", v_input_customer_id)

        if(v_pass_integer == False):
            print("\n[*] Please enter integer value (0-9), Try again...")
        else:
            v_found_customer = is_existing_customer(v_input_customer_id)  
            if(v_found_customer == False):
                 print(f"\n[*] Customer id [\"{v_input_customer_id}\"] is not found in the system,")
                 buy_ticket_response = input("[*] Please \"Enter\" to try again, Otherwise enter \"X\" for back to main menu :").upper() 
            else:
                while buy_ticket_response != "X": 
                    
                    #Render customer info
                    print("\n=== Customer Info ===") 
                    customer_info_detail_by_customerid(customers,v_input_customer_id)
                      
                    #Render the future event which is eligible to buy for the customer 
                    #Render the title
                    display_formatted_row([future_eligible_title], "{: <82}")                      
                    list_events_by_customerid("future_eligible",v_input_customer_id)
                    
                    #Buy ticket process
                    buy_ticket_by_customerid(v_input_customer_id)
                    
                    buy_ticket_response = input("\n[*] Please \"Enter\" to buy others event, , Otherwise enter \"X\" for back to main menu :").upper()

def buy_ticket_by_customerid(p_customer_id = "none"):
    buy_ticket_selected_eventid_response = ""
    while buy_ticket_selected_eventid_response != "done":
        event_id = input("\nPlease enter the \"Event ID\" to buy the ticket :").strip()
        v_pass_blank = validation("IsBlank",event_id)
        v_pass_int = validation("IsDigit",event_id)        
        if(v_pass_blank == False):
            print("\n[*] Event name can't be blank, Try again with some value...")
        else:
            if(v_pass_int == False):
                print("\n[*] Please enter integer value (0-9), Try again...")
            else:
                event_name = get_eventname_by_selected_eventid(event_id, p_customer_id)
                if (event_name == "Notfound"):
                    print(f"\n[!] Please select event id from the \"Upcoming events and eligibility to purchase list\" at above.")
                else:
                    while (buy_ticket_selected_eventid_response != "done"):
                        ticket_count_to_buy = input("\nPlease enter ticket count to buy :")
                        v_pass_integer = validation("IsDigit", ticket_count_to_buy)
                        if(v_pass_integer == False):
                            print("\n[*] Please enter integer value (0-9), Try again...")
                        else:
                            if (check_available_ticket(event_name, ticket_count_to_buy) == True):
                                update_ticket_by_event(event_name, p_customer_id, ticket_count_to_buy)
                                print(f"[^_^] You have successfuly purchased [{ticket_count_to_buy}] tickets for event [{event_name}], Your e-Ticket will be sent to your registered email.")
                                buy_ticket_selected_eventid_response = "done"
                            else:
                                available_ticket_number = get_available_ticket(event_name)
                                if (available_ticket_number == 0):
                                    print(f"[!] Sorry, There are no tickets available at the moment. Kindly consider purchasing tickets for another event.")  
                                    buy_ticket_selected_eventid_response = "done"
                                else:
                                    print(f"[!] Sorry, [{available_ticket_number}] tickets are currently available. You may buy up to [{available_ticket_number}] tickets at most.")

def update_ticket_by_event(event_name = "none", p_customer_id = "none", p_ticket_count_to_buy = 0) :
    #Update process
        event = events[event_name]

        # Check if customer already exists and update their ticket count
        is_existing_customer = False
        for customer in event["customers"]:
            if str(customer[0]) == str(p_customer_id): 
                customer_index = event["customers"].index(customer) 
                event["customers"][customer_index] = (customer[0], customer[1] + int(p_ticket_count_to_buy))
                is_existing_customer = True
                break  # Out from the loop as found
        
        # If customer was not found, insert new record in the event
        if not is_existing_customer:
            event["customers"].append((p_customer_id,int(p_ticket_count_to_buy)))

        # Update total tickets sold to the event 
        event["tickets_sold"] += int(p_ticket_count_to_buy)
        
        print("\n=== List of events purchased by customer ===") 
        list_events_by_customerid("all", p_customer_id)
        
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
    #TBD

#endregion

#region Custom Method

#region Customer
def is_existing_customer(p_customer_id = "none") -> bool:
    for customer in customers:
        if(p_customer_id in str(customer[0])):
            return True
    return False
    
def customer_info_detail_by_customerid(p_customer, p_customer_id):
    for customer in p_customer:
        if(str(customer[0]) == p_customer_id):
            render_customer_detail(customer)
            
def render_customer_detail(p_customer) :
        v_customer_id = p_customer[0]
        v_first_name = p_customer[1]
        v_family_name = p_customer[2]
        v_birthdate = p_customer[3]
        v_email = p_customer[4]
        v_formatted_birthdate = v_birthdate.strftime("%d %b %Y")

        #Render Customer Info
        display_formatted_row(["\nCustomer ID", f"{v_customer_id}"], "{: <20} : {: <50}") 
        display_formatted_row(["\nFirst Name", f"{v_first_name}"], "{: <20} : {: <50}") 
        display_formatted_row(["\nFamily Name", f"{v_family_name}"], "{: <20} : {: <50}") 
        display_formatted_row(["\nBirth Date", f"{v_formatted_birthdate}"], "{: <20} : {: <50}") 
        display_formatted_row(["\nEmail", f"{v_email}"], "{: <20} : {: <50}")

    
def list_events_by_customerid(list_type, p_customer_id):
    """
    for list_type = "future_eligible"
    #1- Show listing for available event respective to the selected customer 
        *(filter with 
            1) event date is future date, 
            2) customer old enough to attend
         )
    else list_type for all
    """
    
    #Variables
    total_ticket_bought = 0
    v_future_eligible = False
    
    #Define Formatted Style
    display_customer_event_formatted_column_width = "{: <30} {: ^15} {: >14} {: >8} {: >14}"
        
    #Render the header
    if (list_type == "future_eligible"):    
        #Define Formatted Style
        display_customer_event_formatted_column_width = "{: <8} {: <30} {: ^15} {: >14} {: >8} {: >14} {: >20}"        
        display_formatted_row([double_underline_style*8, double_underline_style*30, double_underline_style*14, double_underline_style*15,  double_underline_style*8, double_underline_style*14, double_underline_style*20 ], display_customer_event_formatted_column_width) 
        display_formatted_row(["Event ID"              , "Event Name"             , "Event Date"             , "Age Restriction"        ,  "Capacity"              , "Ticket Sold"            , "Ticket Available Now"    ], display_customer_event_formatted_column_width)
        display_formatted_row([double_underline_style*8, double_underline_style*30, double_underline_style*14, double_underline_style*15,  double_underline_style*8, double_underline_style*14, double_underline_style*20 ], display_customer_event_formatted_column_width) 
    else:
        display_formatted_row([double_underline_style*30, double_underline_style*14, double_underline_style*15,  double_underline_style*8, double_underline_style*14 ], display_customer_event_formatted_column_width) 
        display_formatted_row(["Event Name"             , "Event Date"             , "Age Restriction"        ,  "Capacity"              , "Ticket Bought"           ], display_customer_event_formatted_column_width)
        display_formatted_row([double_underline_style*30, double_underline_style*14, double_underline_style*15,  double_underline_style*8, double_underline_style*14 ], display_customer_event_formatted_column_width) 
                
    #Sorted by Event Name
    sorted_events = sorted(events.items(), key=lambda x: x[0])
   
    #Get the list of event bought by customer
    event_id = 0
    for event_name, details in sorted_events:
        for customer_id, tickets_bought in details["customers"]:
            #Check customer bought the event
            if str(customer_id) == str(p_customer_id): 
                
                #Set Value
                v_event_name = event_name
                v_event_date = details['event_date'].strftime("%d %b %Y")
                v_age_restriction = details['age_restriction']
                v_capacity = details['capacity']
                v_tickets_bought = tickets_bought
 
                #Render the list of event
                if (list_type == "future_eligible"):
                    v_pass_age_restriction = is_pass_age_restriction(v_age_restriction, customer_id)
                    v_future_event_date = is_existing_future_event(v_event_name)

                    if (v_pass_age_restriction and v_future_event_date):
                        v_future_eligible = True
                        #Render the list of event which are future and eligible for selected customer
                        event_id = event_id + 1                          
                        display_formatted_row([event_id, v_event_name, v_event_date, v_age_restriction, v_capacity, v_tickets_bought, (v_capacity - v_tickets_bought) ], display_customer_event_formatted_column_width)
                else:
                    #Render the list of event purchased by customer
                    #Get the total ticket 
                    total_ticket_bought = total_ticket_bought + v_tickets_bought                    
                    display_formatted_row([v_event_name, v_event_date, v_age_restriction, v_capacity, v_tickets_bought], display_customer_event_formatted_column_width)
    

       
    #Check total ticket value is 0 then show No ticket bought else show the total ticket value bought by customer                
    if(v_future_eligible):
        if (event_id == 0):
            display_formatted_row(["\n[!] Currently, no events are available for you. Please contact our event customer service for further assistance."], "{: ^86}")  
    else:
        #Render the sub group break line
        display_formatted_row([single_underline_style*85], "{: ^85}")           
        
        if (total_ticket_bought>0):
            display_formatted_row([f"Total tickets bought : {total_ticket_bought}" ], "{:>85}")
        else:
            display_formatted_row(["*** No ticket bought ***"], "{: ^86}")                 

        #Render the sub group break line
        display_formatted_row([single_underline_style*85], "{: ^85}")   
    
def is_pass_age_restriction(p_event_age_restriction, p_customer_id) -> bool:
    for customer in customers:
        if(str(customer[0]) == str(p_customer_id)):
            customer_birthdate = customer[3]
            age_restriction_date = date(v_today.year - p_event_age_restriction, v_today.month, v_today.day)
            return (age_restriction_date > customer_birthdate)
    return False 

def get_eventname_by_selected_eventid(p_selected_eventId, p_customer_id):
    future_eligible_events = []
    #Sorted by Event Name
    sorted_events = sorted(events.items(), key=lambda x: x[0])
   
    #Get the list of eligible and future event list by customer
    event_id = 0
    for event_name, details in sorted_events:
        for customer_id, tickets_bought in details["customers"]:
            #Check customer bought the event
            if str(customer_id) == str(p_customer_id): 
                #Set Value
                v_event_name = event_name
                v_age_restriction = details['age_restriction']

                #Get the result
                v_pass_age_restriction = is_pass_age_restriction(v_age_restriction, customer_id)
                v_future_event_date = is_existing_future_event(v_event_name)
                
                #Check
                if (v_pass_age_restriction and v_future_event_date):
                    future_eligible_events.append({
                        "event_id": event_id+1,
                        "event_name": event_name
                    })

    #get the selected event name from the list
    event_name = get_event_name_by_id(p_selected_eventId, future_eligible_events)

    return event_name  

def get_event_name_by_id(event_id, events):
    for event in events:
        if str(event['event_id']) == str(event_id):
            return event['event_name']
    return "Notfound"
                        
#endregion             

#region Event
def check_available_ticket(event_name = "none", p_ticket_count_to_buy = 0) -> bool:
    #TBD - testing for available ticket
    available_ticket_number = get_available_ticket(event_name)
    if (int(p_ticket_count_to_buy) > available_ticket_number):
        return False
    else:
        return True
    
def get_available_ticket(p_event_name = "none") -> int:
    #Get available by event name
    available_ticket = 0
    for event_name, event_details in events.items():
        if(str(p_event_name).upper() == str(event_name).upper()):
            available_ticket =  event_details["capacity"] - event_details["tickets_sold"]
    return available_ticket


def is_existing_future_event(p_event_name = "none") -> bool:
    #Check event are existing event and event date is future date
    for event_name, event_details in events.items():
        if(str(p_event_name).upper() == str(event_name).upper()):
            if(date.today() <= event_details["event_date"]):
                return True
     
    return False  
   
#endregion

#region Validation
def validation(p_validation_type = "none", p_validation_value = "none") -> bool:
    match p_validation_type:
        case "IsDigit":
            if(p_validation_value.isdigit()):
                return True
            else:
                return False
        case "IsBlank":
                    if(p_validation_value.strip()):
                        return True
                    else:
                        return False
            
#endregion

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
        input("\nPress Enter to continue.")
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

