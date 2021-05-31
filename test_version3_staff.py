import unittest
import time
import names
import allure
import pytest
import json
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selector import commonpath, confirmationpageselectors, customersearchselectors
from selector import loginselectors, bookingpageselectors, paymentselectors
from methods import remove_from_cart, giftvoucher, card_payment,epos_payment, skip_payment, send_payment_link, assertion, discount, checkout
from methods import date_picker, time_picker,existing_customer,adding_newcustomer,additionalitem_add_to_sale
from methods import date_and_time_verification,invalid_promocode,promocode,site_selection, birthday_product, login, skate_product, birthday_product2, details_verfication
from methods import pay_balance,pay_balance_online, execute_click_by_text_on,find_element_by_text, birthday_submodule,add_to_sale,find_element_by_text_input,find_element_by_text_div
from selenium.webdriver.chrome.options import Options

class TestBookNowBase(unittest.TestCase):
    
    def setUp(self):
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('data2.json',"r") 
        data = json.loads(f.read()) 
        self.driver.get(data["url_staffbooking"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        login(self.driver,data["username"],data["password"],data["register"])
        f.close()
        
    def tearDown(self):
        self.driver.quit()

class TestV3StaffBooking(TestBookNowBase):

    # @allure.description("To test creating new user account")
    # def test_01_new_account(self):
    #     try:
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # @allure.description("To login with existing user")
    # def test_02_existing_account(self):
    #     try:
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         customer_name=existing_customer(self.driver,data["existing_user"])
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  
    
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("Booking a  Product and adding additional item. And Payment through card")
    # def test_03_online(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         booking_detail={}
    #         booking_detail["customer_firstname"]=first_name
    #         booking_detail["customer_lastname"]= last_name
    #         booking_detail["customer_name"]=customer_name
    #         booking_detail["site_name"]= data["site"]
    #         booking_detail["products"]=[]
    #         amount='0'
    #         # site_selection(self.driver,data["site"])
            
    #         for aa in data["productlist"]:
    #             # # if data["product"]==aa["productname"]:
    #             # if data["producttype"]==aa["producttype"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     birthday_submodule(self.driver,birthdaypersonname,aa["quantity"],data["foodoption"],data["birthdayperson_age"])
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]
    #                 # product1["name"]= aa["productname"]
    #                 # product1["qty"]= aa["quantity"]
    #                 # product1["time"]= aa["time"]
    #                 # product1["date"]= aa["date"]
    #                 # booking_detail["products"].append(product1)

    #         print(product_quantity)
    #         print(timeslot)

    #         for bb in data["additionalitemlist"]:
    #                 print (bb)
    #                 execute_click_by_text_on(self.driver,bb)
    #                 time.sleep(3)
    #                 additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
    #                 itemname= bb["itemname"]
    #                 item_quantity= bb["quantity"]
        
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
    #         print(product_price)
    #         checkout(self.driver)
    #         amount= card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
    #         time.sleep(5)
    #         booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
    #         print(booking_number)
    #         customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
    #         print(customer_name)
    #         details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
    #         time.sleep(4)
    #         # # self.driver.refresh()
    #         # # time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("Booking a  Product, applying a discount and payment via Epos")
    # def test_04_epos_discount(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         product_price=0
    #         # site_selection(self.driver,data["site"])
            

    #         for aa in data["productlist2"]:
    #             # # if data["product"]==aa["productname"]:
    #             # if data["producttype"]==aa["producttype"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     time.sleep(3)
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     # pp= int(pp)
    #                     # pr_price= product_price + pp     
    #                     # print(pr_price)               
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]


    #         print(product_quantity)
    #         print(timeslot)

    #         for bb in data["additionalitemlist"]:
    #             if data["itemtype"]== bb["itemgroup"]:
    #                 print (bb)
    #                 execute_click_by_text_on(self.driver,bb)
    #                 time.sleep(3)
    #                 additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
    #                 itemname= bb["itemname"]
    #                 item_quantity= bb["quantity"]
        
    #         # customer_name=existing_customer(self.driver,data["existing_user"])
    #         # time.sleep(3)
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         # giftvoucher(self.driver, data["promotionalcode"])
    #         # discount(self.driver, data["discount"])
    #         checkout(self.driver)
    #         #amount= card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
    #         amount= epos_payment(self.driver)
    #         time.sleep(7)
    #         booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
    #         print(booking_number)
    #         customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
    #         print(customer_name)
    #         details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
    #         time.sleep(4)
    #         # self.driver.refresh()
    #         # time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # @allure.description("Booking a  Product and adding a giftvoucher")
    # def test_05_giftvoucher(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         product_price=0
    #         # site_selection(self.driver,data["site"])
            

    #         for aa in data["productlist3"]:
               
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     # pp= int(pp)
    #                     # pr_price= product_price + pp     
    #                     # print(pr_price)   
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     # pp= int(pp)
    #                     # pr_price= product_price + pp     
    #                     # print(pr_price)   
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     # pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     # pp= int(pp)
    #                     # pr_price= product_price + pp     
    #                     # print(pr_price)   
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]

    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         giftvoucher(self.driver, data["giftvoucher"])
    #         time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  
    
    # @allure.description("Booking a  Product and adding a promovode")
    # def test_06_promocode(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         product_price=0
    #         # site_selection(self.driver,data["site"])
    #         for aa in data["productlist4"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     pp= int(pp)
    #                     pr_price= product_price + pp     
    #                     print(pr_price)   
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     # pp= int(pp)
    #                     # pr_price= product_price + pp     
    #                     # print(pr_price)   
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]

    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         promocode(self.driver, data["promotionalcode"])
    #         time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex 

    # @allure.description("Booking a  Product and adding an invalid promocode")
    # def test_07_invalid_promocode(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         product_price=0
    #         # site_selection(self.driver,data["site"])
    #         for aa in data["productlist5"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     # pp= int(pp)
    #                     # pr_price= product_price + pp     
    #                     # print(pr_price)   
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     # pp= int(pp)
    #                     # pr_price= product_price + pp     
    #                     # print(pr_price)   
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]

    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         invalid_promocode(self.driver, data["promotionalcode2"])
    #         time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex 

    # def test_08_removing_product_from_the_cart(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         product_price=0
    #         # site_selection(self.driver,data["site"])
    #         for aa in data["productlistA"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                     # pp= int(pp)
    #                     # pr_price= product_price + pp     
    #                     # print(pr_price)               
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]

    #         for bb in data["additionalitemlist"]:
    #                 print (bb)
    #                 execute_click_by_text_on(self.driver,bb)
    #                 time.sleep(3)
    #                 additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
    #                 itemname= bb["itemname"]
    #                 item_quantity= bb["quantity"]
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         remove_from_cart(self.driver)
    #         checkout(self.driver)
    #         #amount= card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
    #         # amount= epos_payment(self.driver)
    #         skip_payment(self.driver)
    #         # send_payment_link(self.driver)
    #         time.sleep(7)
    #         # assertion(self.driver)
    #         booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
    #         print(booking_number)
    #         customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
    #         print(customer_name)
    #         details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
    #         time.sleep(4)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # def test_09_date_verification(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         for aa in data["productlistA1"]:
    #             execute_click_by_text_on(self.driver, aa)
    #             date_picker(self.driver,aa["date"],aa["quantity"])
    #             time_picker(self.driver,aa["time"])
    #             date_and_time_verification(self.driver, aa["productname"],aa["date"],aa["time"])             
    #         time.sleep(4)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # def test_10_checkout_after_removing_product(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         product_price=0
    #         # site_selection(self.driver,data["site"])
    #         for aa in data["productlistA1"]:
    #             execute_click_by_text_on(self.driver, aa)
    #             date_picker(self.driver,aa["date"],aa["quantity"])
    #             time_picker(self.driver,aa["time"])
    #             pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])             
                    
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         remove_from_cart(self.driver)
    #         checkout(self.driver)
    #         notification= By_ID(bookingpageselectors.failure_error).text
    #         error_msg ="Please add a customer and items to the cart."
    #         assert error_msg in notification
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("Booking a Tax Product and Payment through card and finally refunding it.")
    # def test_11_tax_product_refund_epos(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
            
    #         for aa in data["productlist"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     birthday_submodule(self.driver,birthdaypersonname,aa["quantity"],data["foodoption"],data["birthdayperson_age"])
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]

    #         print(product_quantity)
    #         print(timeslot)

    #         for bb in data["additionalitemlist"]:
    #                 print (bb)
    #                 execute_click_by_text_on(self.driver,bb)
    #                 time.sleep(3)
    #                 additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
        #             itemname= bb["itemname"]
        #             item_quantity= bb["quantity"]
        
        #     adding_newcustomer(self.driver,first_name,last_name,phone_number)
        #     product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
        #     print(product_price)
        #     checkout(self.driver)
        #     skip_payment(self.driver)
        #     # amount= card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
        #     time.sleep(5)
        #     booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
        #     print(booking_number)
        #     customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
        #     print(customer_name)
        #     details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
        #     time.sleep(4)
            
        #     f.close()
        
        #     try:
        #         self.driver.find_element_by_link_text("Check In") .click()
        #     except:
        #         By_xpath(customersearchselectors.checkin_btn).click()
        #     time.sleep(8)
        #     By_xpath(customersearchselectors.search_box).send_keys(booking_number)
        #     time.sleep(4)
        #     pay_balance(self.driver,booking_number)
        #     f.close()
        
        # except Exception as ex:
        #     allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
        #     raise ex  

    # @allure.description("Booking a  Product with half payment and then paying with card")
    # def test_12_tax_product_balance_online(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
            
    #         for aa in data["productlist"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     birthday_submodule(self.driver,birthdaypersonname,aa["quantity"],data["foodoption"],data["birthdayperson_age"])
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     date_picker(self.driver,aa["date"],aa["quantity"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]

    #         print(product_quantity)
    #         print(timeslot)

    #         for bb in data["additionalitemlist"]:
    #                 print (bb)
    #                 execute_click_by_text_on(self.driver,bb)
    #                 time.sleep(3)
    #                 additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
    #                 itemname= bb["itemname"]
    #                 item_quantity= bb["quantity"]
        
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
    #         print(product_price)
    #         checkout(self.driver)
    #         skip_payment(self.driver)
    #         # amount= card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
    #         time.sleep(5)
    #         booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
    #         print(booking_number)
    #         customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
    #         print(customer_name)
    #         details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
    #         time.sleep(4)
            
    #         f.close()
        
    #         try:
    #             self.driver.find_element_by_link_text("Check In") .click()
    #         except:
    #             By_xpath(customersearchselectors.checkin_btn).click()
    #         time.sleep(8)
    #         By_xpath(customersearchselectors.search_box).send_keys(booking_number)
    #         time.sleep(4)    
    #         pay_balance_online(self.driver,booking_number,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["year"],data["cvc"])
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # # def test_13_tax_product_with_giftvoucher(self):
    # #     try:
    # #         By_ID = self.driver.find_element_by_id
    # #         By_xpath= self.driver.find_element_by_xpath
    # #         first_name= names.get_first_name()
    # #         last_name = names.get_last_name()
    # #         customer_name="{0} {1}".format(first_name,last_name)
    # #         birthdaypersonname=names.get_first_name()
    # #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    # #         f = open('data2.json',"r") 
    # #         data = json.loads(f.read()) 
    # #         amount='0'
            
    # #         for aa in data["productlist"]:
    # #             print(aa)
    # #             execute_click_by_text_on(self.driver, aa)
    # #             date_picker(self.driver,aa["date"],aa["quantity"])
    # #             time_picker(self.driver,aa["time"])
    # #             add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    # #             product= aa["productname"]   
    # #             product_quantity=aa["quantity"]
    # #             timeslot=aa["time"]

    # #         print(product_quantity)
    # #         print(timeslot)

    # #         for bb in data["additionalitemlist"]:
    # #                 print (bb)
    # #                 execute_click_by_text_on(self.driver,bb)
    # #                 time.sleep(3)
    # #                 additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
    # #                 itemname= bb["itemname"]
    # #                 item_quantity= bb["quantity"]
        
    # #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    # #         giftvoucher(self.driver, data["giftvoucher"])
    # #         product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
    # #         print(product_price)
    # #         assert product_price =="0.00"
    # #         checkout(self.driver)       
    # #         booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
    # #         print(booking_number)
    # #         customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
    # #         print(customer_name)
    # #         details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
    # #         time.sleep(4)    
    # #         f.close()
    
    # #     except Exception as ex:
    # #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    # #         raise ex  

    # def test_14_tax_product_with_promocode(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
            
    #         for aa in data["productlist"]:
    #             print(aa)
    #             execute_click_by_text_on(self.driver, aa)
    #             date_picker(self.driver,aa["date"],aa["quantity"])
    #             time_picker(self.driver,aa["time"])
    #             add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
    #             product= aa["productname"]   
    #             product_quantity=aa["quantity"]
    #             timeslot=aa["time"]

    #         print(product_quantity)
    #         print(timeslot)

    #         for bb in data["additionalitemlist"]:
    #                 print (bb)
    #                 execute_click_by_text_on(self.driver,bb)
    #                 time.sleep(3)
    #                 additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
    #                 itemname= bb["itemname"]
    #                 item_quantity= bb["quantity"]
        
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         promocode(self.driver, data["promotionalcode"])
    #         product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
    #         print(product_price)
    #         checkout(self.driver)       
    #         booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
    #         print(booking_number)
    #         customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
    #         print(customer_name)
    #         details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
    #         time.sleep(4)    
    #         f.close()
    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  


    @allure.description("Booking a Product with booking charges and adding a giftvoucher")
    def test_15_booking_fee_product_with_giftvoucher(self):
        try:
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            first_name= names.get_first_name()
            last_name = names.get_last_name()
            customer_name="{0} {1}".format(first_name,last_name)
            birthdaypersonname=names.get_first_name()
            phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 
            amount='0'
            product_price=0
            # site_selection(self.driver,data["site"])
            

            for aa in data["product_fee"]:
               
                    print(aa)
                    if aa["producttype"]=="Other":
                        try:
                            By_xpath(bookingpageselectors.other_productgroup).click()
                            time.sleep(2)
                        except:
                            print("already open")
                        find_element_by_text(self.driver,aa["productname"]).click()
                        date_picker(self.driver,aa["date"],aa["quantity"])
                        time_picker(self.driver,aa["time"])
                        pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
                        # pp= int(pp)
                        # pr_price= product_price + pp     
                        # print(pr_price)   
                    elif aa["producttype"]=="Birthday":
                        try:
                            By_xpath(bookingpageselectors.birthday_product).click()
                            time.sleep(2)
                        except:
                            print("already open")
                        find_element_by_text(self.driver,aa["productname"]).click()
                        date_picker(self.driver,aa["date"],aa["quantity"])
                        time_picker(self.driver,aa["time"])
                        pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
                        # pp= int(pp)
                        # pr_price= product_price + pp     
                        # print(pr_price)   
                        # break
                    else:
                        execute_click_by_text_on(self.driver, aa)
                        date_picker(self.driver,aa["date"],aa["quantity"])
                        time_picker(self.driver,aa["time"])
                        # pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
                        # pp= int(pp)
                        # pr_price= product_price + pp     
                        # print(pr_price)   
                    product= aa["productname"]   
                    product_quantity=aa["quantity"]
                    timeslot=aa["time"]

            adding_newcustomer(self.driver,first_name,last_name,phone_number)
            giftvoucher(self.driver, data["giftvoucher"])
            time.sleep(5)
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
            raise ex 

if __name__ == '__main__':
    unittest.main()



