"""
This module contains functions to calculate the number of SMS messages that can be sent with a given amount of airtime and the total cost of sending those messages based on the network rate.
"""
import os
import json


def fetch_network_rate(network):
    """
    Fetch the network rate for the given network

    Args:
        network: name of the network
    Returns:
        If network is found:
            The cost per SMS in naira for the given network
        If network is not found:
            None
    """
    
    try:
        base_dir = os.path.dirname(__file__)
        json_path = os.path.join(base_dir, 'rate.json')
        
        with open(json_path, 'r') as file:
            data = json.load(file)
        rate = data[network]['rate']
        return rate
    except KeyError:
        return None

        

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