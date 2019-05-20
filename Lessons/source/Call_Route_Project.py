'''
Pair programmed with Marianna Campbell :) !
This solution works with all three scenarios.
'''


#!python
import time
from pprint import pprint
from hashtable import HashTable

def load_data():
    """
    Returns a list of phone prefixes and prices from a file.
    """
    route_costs = []
    with open('../../project/data/route-costs-4.txt', 'r') as f:
        for line in f:
            prefix, price = line.split(',')
            pprice = price.replace("\n", "")
            route_costs.append((prefix, pprice))
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
        # print("Phone number and price:", prefix, price)
        ht.set(prefix, price)

    # Check if have a prefix that matches the start of a phone_num

    return ht



def is_prefix_match_and_get_price(ht, phone_num):
    """
    Return True if the prefix we have on record is the start of a phone we give
    as input otherwise return False
    """
    # print("Phone Number:", phone_num)
    #check if the phone number is in the HashTable
    if not phone_num:
        # raise ValueError('phone number does not exist')
        return 0
    if ht.contains(phone_num):
        # if yes, return the price
        # return print("Route Cost for {}: ${}".format(phone_num, ht.get(phone_num)))
        return ht.get(phone_num)
    #if not, pop off the last digit of the phone number
    else:
        phone_num = phone_num[:-1]
        return is_prefix_match_and_get_price(ht, phone_num)

def get_prices(phone_numbers, is_prefix_match_and_get_price, ht):
    #create prices list
    price_list = []

    #loop through the phone numbers
    for number in phone_numbers:
    #pass one phone number into the prefix match function
    #append price to the list
        price = is_prefix_match_and_get_price(ht, number)
        with open('HELLO_route-costs.txt', 'a') as f:
            f.write("%s, %s \n" % (number, str(price) ))
        # price_list.append(is_prefix_match_and_get_price(ht, phone_num))

    return price_list


def load_phone_nums():
    """
    Returns a list of phone numbers.
    """
    phone_numbers = []

    with open('../../project/data/phone-numbers-3.txt', 'r') as f:
        for line in f:
            # print(line)
            individual_phone_num = line.replace("\n", "")
            phone_numbers.append(individual_phone_num)

    return phone_numbers


if __name__ == '__main__':
    start = time.time()
    route_costs = load_data()

    ht = init_hashtable(route_costs)
    phone_numbers = load_phone_nums()
    price_list = get_prices(phone_numbers, is_prefix_match_and_get_price, ht)
    print(get_prices(phone_numbers, is_prefix_match_and_get_price, ht))
    print(price_list)
    end = time.time()
    print(end - start)
    # print(is_prefix_match_and_get_price(ht, phone_numbers))
    # print(load_phone_nums())

#Psuedocode
# Check the book for number and get the price
# Open the file put file info into a list
# Loop through it
# Check if the number makes the given number
# if it does return the set second value
# Else phone number not found

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

# open up the phone number file
    #read the first line, strip away the new line character
    #add each phone number to a list
