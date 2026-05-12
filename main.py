"""
The main part of the application where everything comes together.
"""
from src.user_interface import get_airtime_amount, get_sms_count, get_network_choice
from src.calculator import fetch_network_rate, calculate_airtime_cost, calculate_sms_count
from src.views import display_airtime_amount, display_sms_count

def main():
    """Wrapping the entire Application to tell python this is the main script for which this application is run from."""
    
    while True:
        print("======================================================")
        print("             NIGERIAN SMS CALCULATOR V1.0         ")
        print("======================================================")
        print("Welcome! What will you like to calculate today?")
        try:
            print("1. Calculate number of SMS you can send from airtime")
            print("2. Calculate how much airtime needed to send messages")
            print("3. Exit application")
            select_option = int(input("Select an option: "))
            if select_option == 1:
                #Get, Calculate and Display the Number of Messages you send from airtime 
                airtime_amount = get_airtime_amount()
                network = get_network_choice()
                network_rate = fetch_network_rate(network)
                if network_rate is None:
                    print('Invalid network. Enter a correct network.')
                    continue
                else:
                    total_sms = calculate_sms_count(airtime_amount, network_rate)
                
                display_sms_count(airtime_amount, total_sms,network)
            
            elif select_option == 2:
                #Get, Calculate and Display the amount needed to send messages
                sms_count = get_sms_count()
                network = get_network_choice()
                network_rate = fetch_network_rate(network)
                if network_rate is None:
                    print('Invalid network. Enter a correct network.')
                    continue
                else:
                    total_airtime_needed = calculate_airtime_cost(sms_count, network_rate)
                
                display_airtime_amount(sms_count, network, total_airtime_needed)
            
            elif select_option == 3:
                break
            
            else:
                print("Invalid input! Please select 1 or 2.")
            
        except ValueError:
            print('Invalid input! Please select 1 or 2.')
        


if __name__ == "__main__":
    main()
