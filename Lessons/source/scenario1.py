'''Scenario 1: One-time route cost check
You have a carrier route list with 100,000 (100K) entries (in arbitrary order)
and a single phone number. How quickly can you find the cost of calling this number?'''
# Check the book for number and get the price
# Open the file put file info into a list
# Loop through it
# Check if the number makes the given number
# if it does return the set second value
# Else phone number not found

#!python
from pprint import pprint
from hashtable import HashTable

def load_data():
    """
    Returns a list of phone numbers and prices from a file.
    """
    route_costs = []
    with open('../../project/data/route-costs-4.txt', 'r') as f:
        for line in f:
            prefix, price = line.split(',')
            route_costs.append((prefix, price))
    return route_costs

def init_hashtable(route_costs):
    """
    Add phone number (key) and price (value) in the hashtable and return
    hashtable items to proven the data is inserted correctly.
    """
    output_list = []
    num_buckets = len(route_costs)
    ht = HashTable(num_buckets)
    for prefix, price in route_costs: # number gives up +
        print("Phone number and price:", prefix, price)
        ht.set(prefix, price)

    # Check if have a prefix that matches the start of a phone_num

    return ht



def is_prefix_match_and_get_price(ht, phone_num):
    """
    Return True if the prefix we have on record is the start of a phone we give
    as input otherwise return False
    """
    print("Phone Number:", phone_num)
    #check if the phone number is in the HashTable
    if not phone_num:
        raise ValueError('phone number does not exist')
    if ht.contains(phone_num):
        # if yes, return the price
        return print("Route Cost for {}: ${}".format(phone_num, ht.get(phone_num)))
    #if not, pop off the last digit of the phone number
    else:
        phone_num = phone_num[:-1]
        return is_prefix_match_and_get_price(ht, phone_num)

    # you've got a phone do we have a prefix that matches it
    # contains
    # get the price
    #
    # if self.contains(phone_num):
    #     self.get()


#check if the phone number is in the HashTable
    # if yes, return the price
    #if not, pop off the last digit of the phone number
        #store the popped off phone number into a variable
    # call the function recursivley
    # return recursive function





if __name__ == '__main__':
    route_costs = load_data()
    print("Phone Numbers and Prices:", route_costs)
    print("***")
    ht = init_hashtable(route_costs)
    print(is_prefix_match_and_get_price(ht, '+15124156620'))
