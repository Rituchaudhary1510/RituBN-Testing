import unittest, time, names
import allure, pytest , json
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from v2_staff_selector import commonpath, confirmationpageselectors, customersearchselectors
from v2_staff_selector import loginselectors, bookingpageselectors, paymentselectors
from v2_checkin_methods import room_verification, select_booking
from v2_staff_methods import invalid_giftvoucher,giftvoucher,promocode, card_payment,epos_payment, skip_payment, send_payment_link, assertion, discount, checkout
from v2_staff_methods import date_verification,date_picker, time_picker,existing_customer,adding_newcustomer,additionalitem_add_to_sale
from v2_staff_methods import site_selection, login, details_verfication
from v2_staff_methods import pay_balance,pay_balance_online,remove_from_cart,promocode2,execute_click_by_text_on,find_element_by_text, birthday_submodule,add_to_sale,find_element_by_text_input,find_element_by_text_div
from selenium.webdriver.chrome.options import Options

class TestBookNowBase(unittest.TestCase):
    
    def setUp(self):
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('v2.json',"r") 
        data = json.loads(f.read()) 
        self.driver.get(data["url_staffbooking"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        login(self.driver,data["username"],data["password"],data["register"])
        assert self.driver.title == "Book"
        f.close()
        
    def tearDown(self):
        self.driver.quit()

class TestV2StaffBooking(TestBookNowBase):

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
    #         f = open('v2.json',"r") 
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
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 
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
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"], aa["productname"])
    #                 # if aa["producttype"]=="Parties" or aa["producttype"]=="Birthday Parties":
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     birthday_submodule(self.driver,birthdaypersonname,aa["quantity"],data["foodoption"],data["birthdayperson_age"])
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]

    #         print(product_quantity)
    #         print(timeslot)

    #         for bb in data["additionalitemlist"]:
    #             # if data["itemtype"]== bb["itemgroup"]:
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
    #         product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
    #         print(product_price)
    #         checkout(self.driver)
    #         card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
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
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 
    #         booking_detail={}
    #         booking_detail["customer_firstname"]=first_name
    #         booking_detail["customer_lastname"]= last_name
    #         booking_detail["customer_name"]=customer_name
    #         booking_detail["site_name"]= data["site"]
    #         booking_detail["products"]=[]
            
    #         amount='0'
    #         # site_selection(self.driver,data["site"])
            

    #         for aa in data["productlist2"]:
    #             print(aa)
    #             product1={}
    #             execute_click_by_text_on(self.driver, aa)
    #             # date_picker(self.driver,aa["date"])
    #             time_picker(self.driver,aa["time"])
    #             add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
    #             product= aa["productname"]   
    #             product_quantity=aa["quantity"]
    #             timeslot=aa["time"]
    #             product1["name"]= aa["productname"]
    #             product1["qty"]= aa["quantity"]
    #             product1["time"]= aa["time"]
    #             product1["date"]= aa["date"]
    #             booking_detail["products"].append(product1)
                

    #         print(product_quantity)
    #         print(timeslot)

    #         for bb in data["additionalitemlist"]:
    #             if data["itemtype"]== bb["itemgroup"]:
    #                 print (bb)
    #                 item1={}
    #                 execute_click_by_text_on(self.driver,bb)
    #                 time.sleep(3)
    #                 additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
    #                 itemname= bb["itemname"]
    #                 item_quantity= bb["quantity"]
    #                 item1["name"]= bb["itemname"]
    #                 item1["qty"]= bb["quantity"]
    #                 booking_detail["products"].append(item1)
    #         # customer_name=existing_customer(self.driver,data["existing_user"])
    #         # time.sleep(3)
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         # giftvoucher(self.driver, data["promotionalcode"])
    #         # discount(self.driver, data["discount"])
    #         product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
    #         print(product_price)
    #         checkout(self.driver)
    #         # card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
    #         amount= epos_payment(self.driver)
    #         booking_detail["total_amount"]=amount
    #         # skip_payment(self.driver)
    #         # send_payment_link(self.driver)
    #         time.sleep(4)
    #         # assertion(self.driver)
    #         booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
    #         print(booking_number)
    #         booking_detail["booking_number"]= booking_number
    #         customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
    #         print(customer_name)
    #         details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
    #         time.sleep(4)
    #         jsondata=json.dumps(booking_detail,ensure_ascii=False, indent=4)
    #         print(jsondata)

    #         with open('data.txt', 'w') as outfile:
    #             json.dump(booking_detail, outfile)
    #         # self.driver.refresh()
    #         time.sleep(5)
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
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         # site_selection(self.driver,data["site"])
            

    #         for aa in data["productlist3"]:
    #             if data["product"]==aa["productname"]:
    #             # if data["producttype"]==aa["producttype"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"], aa["productname"])
    #                 # if aa["producttype"]=="Parties" or aa["producttype"]=="Birthday Parties":
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
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
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
        
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         giftvoucher(self.driver, data["giftvoucher"])
    #         time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # @allure.description("Booking a  Product and adding a invalid giftvoucher")
    # def test_06_invalid_giftvoucher(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         # site_selection(self.driver,data["site"])
            

    #         for aa in data["productlist3"]:
    #             if data["product"]==aa["productname"]:
    #             # if data["producttype"]==aa["producttype"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"], aa["productname"])
    #                 # if aa["producttype"]=="Parties" or aa["producttype"]=="Birthday Parties":
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
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]
      
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         invalid_giftvoucher(self.driver, data["giftvoucher2"])
    #         time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # @allure.description("Booking a  Product and adding a promocode")
    # def test_07_promocode(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         # site_selection(self.driver,data["site"])
            

    #         for aa in data["productlist"]:
    #             if data["product"]==aa["productname"]:
    #             # if data["producttype"]==aa["producttype"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"], aa["productname"])
    #                 # if aa["producttype"]=="Parties" or aa["producttype"]=="Birthday Parties":
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
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
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
        
    #         adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         promocode(self.driver, data["promotionalcode"])
    #         time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex 

    # @allure.description("Booking a  Product and adding a invalid promocode")
    # def test_08_invalid_promocode(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         # site_selection(self.driver,data["site"])
            

    #         for aa in data["productlist2"]:
    #             if data["product"]==aa["productname"]:
    #             # if data["producttype"]==aa["producttype"]:
    #                 print(aa)
    #                 if aa["producttype"]=="Other":
    #                     try:
    #                         By_xpath(bookingpageselectors.other_productgroup).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"], aa["productname"])
    #                 # if aa["producttype"]=="Parties" or aa["producttype"]=="Birthday Parties":
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
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
    #                 product= aa["productname"]   
    #                 product_quantity=aa["quantity"]
    #                 timeslot=aa["time"]

    #         print(product_quantity)
    #         print(timeslot)
        
    #         # adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         promocode2(self.driver, data["promotionalcode2"])
    #         time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex 
  
   

    # @allure.description("Booking a  Product and adding additional item. And Payment through skip payment")
    # def test_09_skip_payment(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
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
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"], aa["productname"])
    #                 # if aa["producttype"]=="Parties" or aa["producttype"]=="Birthday Parties":
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     birthday_submodule(self.driver,birthdaypersonname,aa["quantity"],data["foodoption"],data["birthdayperson_age"])
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
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
                
    #         customer_name=existing_customer(self.driver,data["existing_user"])
    #         time.sleep(3)
    #         # adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         # giftvoucher(self.driver, data["promotionalcode"])
    #         # discount(self.driver, data["discount"])
    #         product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
    #         print(product_price)
    #         checkout(self.driver)
    #         # card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
    #         skip_payment(self.driver)
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

    # @allure.description("Booking a  Product and adding additional item. And Payment through sendpayment link")
    # def test_10_send_payment_link(self):
    #     try:
    #         By_ID = self.driver.find_element_by_id
    #         By_xpath= self.driver.find_element_by_xpath
    #         first_name= names.get_first_name()
    #         last_name = names.get_last_name()
    #         customer_name="{0} {1}".format(first_name,last_name)
    #         birthdaypersonname=names.get_first_name()
    #         phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 
    #         amount='0'
    #         # site_selection(self.driver,data["site"])
            

    #         for aa in data["productlist3"]:
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
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"], aa["productname"])
    #                 # if aa["producttype"]=="Parties" or aa["producttype"]=="Birthday Parties":
    #                 elif aa["producttype"]=="Birthday":
    #                     try:
    #                         By_xpath(bookingpageselectors.birthday_product).click()
    #                         time.sleep(2)
    #                     except:
    #                         print("already open")
    #                     find_element_by_text(self.driver,aa["productname"]).click()
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     birthday_submodule(self.driver,birthdaypersonname,aa["quantity"],data["foodoption"],data["birthdayperson_age"])
    #                     # break
    #                 else:
    #                     execute_click_by_text_on(self.driver, aa)
    #                     # date_picker(self.driver,aa["date"])
    #                     time_picker(self.driver,aa["time"])
    #                     add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
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
                        
    #         customer_name=existing_customer(self.driver,data["existing_user"])
    #         time.sleep(3)
    #         # adding_newcustomer(self.driver,first_name,last_name,phone_number)
    #         # giftvoucher(self.driver, data["promotionalcode"])
    #         # discount(self.driver, data["discount"])
    #         product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
    #         print(product_price)
    #         checkout(self.driver)
    #         # card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
    #         send_payment_link(self.driver)
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

    @allure.description("Verify a product correct date and time in cart")
    def test_11_date_time_verification(self):
        try:
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 

            for aa in data["productlist2"]:
                execute_click_by_text_on(self.driver, aa)
                product_date=date_picker(self.driver,aa["date"])
                time_picker(self.driver,aa["time"])
                add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
                date_verification(self.driver, aa["productname"], product_date,aa["time"])

        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
            raise ex  

    @allure.description("Removing a product from the cart")
    def test_12_remove_product_from_cart(self):
        try:
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            first_name= names.get_first_name()
            last_name = names.get_last_name()
            customer_name="{0} {1}".format(first_name,last_name)
            birthdaypersonname=names.get_first_name()
            phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            
            for aa in data["productlist3"]:
             
                execute_click_by_text_on(self.driver, aa)
                # date_picker(self.driver,aa["date"])
                time_picker(self.driver,aa["time"])
                add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
                   
            for bb in data["additionalitemlist"]:
                # if data["itemtype"]== bb["itemgroup"]:
                    print (bb)
                    execute_click_by_text_on(self.driver,bb)
                    time.sleep(3)
                    additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
                    itemname= bb["itemname"]
                    item_quantity= bb["quantity"]
                        
            customer_name=existing_customer(self.driver,data["existing_user"])
            time.sleep(3)
            remove_from_cart(self.driver)
            product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
            print(product_price)
            checkout(self.driver)
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
            raise ex  

    @allure.description("Try to checkout directly")
    def test_13_checkout_without_adding_product(self):
        try:
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            first_name= names.get_first_name()
            last_name = names.get_last_name()
            customer_name="{0} {1}".format(first_name,last_name)
            birthdaypersonname=names.get_first_name()
            phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            
            for aa in data["productlist2"]:
             
                execute_click_by_text_on(self.driver, aa)
                date_picker(self.driver,aa["date"])
                time_picker(self.driver,aa["time"])
                add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
                        
            customer_name=existing_customer(self.driver,data["existing_user"])
            time.sleep(3)
            remove_from_cart(self.driver)
            checkout(self.driver)
            notification= By_ID(bookingpageselectors.failure_error).text
            error_msg ="Please add a customer and items to the cart."
            assert error_msg in notification
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
            raise ex  


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Booking a  Product and adding additional item. And Payment through card")
    def test_14_birthday_product_with_room(self):
        try:
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            first_name= names.get_first_name()
            last_name = names.get_last_name()
            customer_name="{0} {1}".format(first_name,last_name)
            birthdaypersonname=names.get_first_name()
            phone_number = ''.join(["{}".format(randint(0,9)) for num in range(0, 10)])  
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            amount='0'
            
            for aa in data["productlist4"]:
                    print(aa)
                    if aa["producttype"]=="Birthday":
                        By_xpath(bookingpageselectors.birthday_product).click()
                        time.sleep(2)
                        find_element_by_text(self.driver,aa["productname"]).click()
                        date_picker(self.driver,aa["date"])
                        time_picker(self.driver,aa["time"])
                        add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
                        product= aa["productname"]   
                        product_quantity=aa["quantity"]
                        timeslot=aa["time"]
            
            for bb in data["additionalitemlist"]:
                print (bb)
                execute_click_by_text_on(self.driver,bb)
                time.sleep(3)
                additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
                itemname= bb["itemname"]
                item_quantity= bb["quantity"]

            print(product_quantity)
            print(timeslot)
            adding_newcustomer(self.driver,first_name,last_name,phone_number)
            product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
            print(product_price)
            checkout(self.driver)
            card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
            booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
            print(booking_number)
            customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
            print(customer_name)
            details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
            time.sleep(4)
            try:
                self.driver.find_element_by_link_text("Find Customer") .click()
            except:
                By_xpath(customersearchselectors.find_customer).click()
            time.sleep(3)
            select_booking(self.driver, customer_name, booking_number)
            time.sleep(2)
            room_verification(self.driver)
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
            raise ex  

    

if __name__ == '__main__':
    unittest.main()



