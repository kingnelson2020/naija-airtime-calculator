""" 
Display module for the application. This module contains functions that displays result from the logic to the user.
"""

def display_sms_count(airtime, number_of_sms, network):
    """ 
    Display the number of messages that you can send given the amount and network.
    Args:
        airtime: amount of airtime available
        number_of_sms: the number of messages the airtime can send
        network: the particular network the airtime is on
    Returns:
        Displays the number of messages a certain amount of airtime can send via a given network
    """
    
    print(f"With ₦{airtime}, you can send {number_of_sms} messages on {network.capitalize()} network.")
    
def display_airtime_amount(sms_count, network, airtime):
    """ 
    Display the cost of sending a certain amount of messages with a given network.
    Args:
        sms_count: number of messages a certain amount of airtime can send
        network: the particular network the messages will be sent on
        airtime: the amount of airtime
    Returns: Displays the cost of sending a certain number of messages via a given network 
    """
    
    print(f'To send {sms_count} messages with your {network.capitalize()} network, you will need ₦{airtime} worth of airtime.')
