"""
This module contains functions to calculate the number of SMS messages that can be sent with a given amount of airtime and the total cost of sending those messages based on the network rate.
"""

def calculate_sms_count(airtime, network_rate):
    """ 
    Calculate the number of SMS messages that can be sent with the given airtime and network rate
    
    Args:
        airtime: amount of airtime available
        network_rate: cost per SMS message

    Returns:
        Number of SMS messages that can be sent
    """
    number_of_sms = airtime // network_rate
    return number_of_sms
    
def calculate_airtime_cost(sms_count, network_rate):
     """ 
     Calculate the total cost of sending the given number of SMS messages based on the network rate 
     
     Args:
        sms_count: number of SMS messages
        network_rate: cost per SMS message

    Returns:
        Total cost of sending the SMS messages
     """
     airtime_cost = sms_count * network_rate
     return airtime_cost