# Created by: Younes Elfeitori
# Created on: Nov 2017
# Created for:ICS3U
# This program asks the person for his address information

def postage (address, city, postal_code, province, apartment = ''):
    if(apartment == ''):
        print ( address, city, postal_code, province)
    else:
        print(address, city, postal_code, province, apartment)

user_address = raw_input("insert your address: ")
user_apartment = raw_input("insert your apartment number if you want: ")
user_city = raw_input("Insert your city: ")
user_postal_code = raw_input("Insert your postal code: ")
user_province = raw_input("Insert your province: ")

postage(user_address, user_apartment, user_city, user_postal_code,user_province)
