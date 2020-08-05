from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
import glob
import os

#download the purchase data in csv form from Ricemill to the same file that contains this program
#you need to have selenium package to run the program.
"""
This program will automatically fill in the order information in Dropshipzone using csv data from 
Ricemill. 
When running the program, it will fill in the data (e.g. name of the customer, postal address) from the latest csv 
that is downloaded to the same file as the program. 
I believe a human-check is still necessary for placing an order, so this program will pause before you
mannually place the order. 
After placing an order, please don't close the order tab, the program will ask you whether to fill in the 
information for the subsequent order in the csv file, yes for yes, no for no, and then press enter.
If you enter yes, a new order form will be filled in.
If you enter no, the program will terminate.
Please Modify the code indicated by the comments before running the program.
"""
list_of_files = glob.glob(r'C:\Users\Apple\Desktop\new\*.csv') #Enter your file location, \*.csv selects all csv files
latest_file = max(list_of_files, key=os.path.getctime)


def parse():
    with open(latest_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        data = list(csv_reader)
    return data

data = parse()
chromedriver_location = r"C:\Users\Apple\Downloads\chromedriver_win32\chromedriver.exe" #Enter your chrome driver location
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://www.dropshipzone.com.au/customer/account/login/')
email = "" #Enter your email
password = "" #Enter your password
email_xpath = '//*[@id="email"]'
password_xpath = '//*[@id="pass"]'
driver.find_element_by_xpath(email_xpath).send_keys(email)
driver.find_element_by_xpath(password_xpath).send_keys(password)
login_button = '//*[@id="send2"]/span/span'
driver.find_element_by_xpath(login_button).click()

#////////////////////////////////////////////////////////////////////
#fill form information 
order_no = '//*[@id="serial_number"]'
sku = '//*[@id="sku_0"]'
quantity = '//*[@id="qty_0"]'
firstname = '//*[@id="firstname"]'
lastname = '//*[@id="lastname"]'
address_line_1 = '//*[@id="address1"]'
address_line_2 = '//*[@id="address2"]'
suburb = '//*[@id="city"]'
postcode = '//*[@id="zip"]'
state = '//*[@id="region_id-input"]'
nsw = '//*[@id="region_id-input-2"]'
act = '//*[@id="region_id-input-1"]'
nt = '//*[@id="region_id-input-3"]'
qld = '//*[@id="region_id-input-4"]'
sa = '//*[@id="region_id-input-5"]'
tas = '//*[@id="region_id-input-6"]'
vic = '//*[@id="region_id-input-7"]'
wa = '//*[@id="region_id-input-8"]'
phone = '//*[@id="telephone"]'


#////////////////////////////////////////////////////////////////////
j = 1
while j < len(data):
    i = data[j]
    driver.get('https://www.dropshipzone.com.au/rsds/order/new/')
    order_no_in = i[1]
    sku_in = i[5]
    quantity_in = i[7]
    firstname_in = i[27]
    lastname_in = i[28]
    if len(i[29]) == 0:
        address_line_1_in = i[30]
    else:
        address_line_1_in = ' '.join([i[29],i[30]])
    address_line_2_in = i[31]
    suburb_in = i[32]
    state_in =  i[33]
    postcode_in = i[34]
    phone_in = i[36]
    driver.find_element_by_xpath(order_no).send_keys(order_no_in)
    driver.find_element_by_xpath(sku).send_keys(sku_in)
    driver.find_element_by_xpath(quantity).clear()
    driver.find_element_by_xpath(quantity).send_keys(quantity_in)
    driver.find_element_by_xpath(firstname).send_keys(firstname_in)
    driver.find_element_by_xpath(lastname).send_keys(lastname_in)
    driver.find_element_by_xpath(address_line_1).send_keys(address_line_1_in)
    driver.find_element_by_xpath(address_line_2).send_keys(address_line_2_in)
    driver.find_element_by_xpath(suburb).send_keys(suburb_in)
    driver.find_element_by_xpath(postcode).send_keys(postcode_in)
    driver.find_element_by_xpath(state).click()
    if state_in == "NSW" or state_in == "New South Wales":
        driver.find_element_by_xpath(nsw).click()
    elif state_in == "ACT" or state_in == "Australian Capital Territory":
        driver.find_element_by_xpath(act).click()
    elif state_in == "NT" or state_in == "Nothern Territory":
        driver.find_element_by_xpath(nt).click()
    elif state_in == "QLD" or state_in == "Queensland":
        driver.find_element_by_xpath(qld).click()
    elif state_in == "SA" or state_in == "South Australia":
        driver.find_element_by_xpath(sa).click()
    elif state_in == "TAS" or state_in == "Tasmania":
        driver.find_element_by_xpath(tas).click()
    elif state_in == "VIC" or state_in == "Victoria":
        driver.find_element_by_xpath(vic).click()
    elif state_in == "WA" or state_in == "Western Australia":
        driver.find_element_by_xpath(wa).click()
    else:
        print("invalid state name.")
        exit()
    driver.find_element_by_xpath(phone).send_keys(phone_in)
    while True:
        x = input("Continue? ")
        if x == "no":
            exit()
        if x == "yes":
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
    j += 1




