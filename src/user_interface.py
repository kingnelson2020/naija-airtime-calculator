""" 
User interface module for the application. This module contains functions that takes airtime amount and network name from the user
"""

def get_airtime_amount():
    """ Function to get airtime amount from the user. It validates the input to ensure it's a positive number.
    Returns:
        A positive number representing the airtime amount
    """
    while True:
        try:
            airtime = float(input('Enter the amount of airtime you have: '))
            if airtime <= 0:
                print('Airtime amount must be greater than zero. Please enter a valid airtime amount.')
                continue
            return airtime
        
        except ValueError:
            print('Invalid input. Please enter a valid number for airtime amount.')
            continue
        
def get_sms_count():
    """ 
    Function to get number of sms from the user. It validates the input to ensure it's a positive number.
    Returns:
        A positive number representing the sms count.
    """
    while True:
        try:
            number_of_messages = int(input('Enter the number of messages: '))
            if number_of_messages <= 0:
                print('Number of messages must be greater than zero. Please enter a valid number.')
                continue
            return number_of_messages
            
        except ValueError:
            print('Invalid, please enter a valid number for SMS.')
            continue

def get_network_choice():
    """ Function to get network choice from the user. It validates the input to ensure it's a non-empty string.
    Returns:
        A non-empty string representing the network choice
    """
    networks = ['mtn', 'airtel', 'glo', '9mobile']
    while True:
        network_choice = input('Enter the name of your network (e.g. MTN, Airtel, Glo, 9mobile): ').lower().strip()
        if network_choice in networks:
            return network_choice
        else:
            print('Invalid network choice. Please enter a valid network name.')
        