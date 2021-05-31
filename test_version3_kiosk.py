import allure
import pytest
import time
import unittest
import names
import json
# import HtmlTestRunner
from random import randint
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selfservice_selectors import filterselectors, commonpath, homepageselector,confirmationpageselectors, productpageselectors
from selenium.webdriver.support.ui import Select
from selfservice_methods import quantity_selection4,time_selection4, delete_cart_item,product_filter, invalidgiftcard,guest_avg_age,giftcard, add_product_to_cart,loginhere,quantity_selection, quantity_selection4,time_selection, payment_mode, share_payment,datepicker, login,Selectsite,checkout_as_guest,create_account,find_element_by_text, time_selection4
from selfservice_methods import loginhere_new_account,asset, promocode, verification, card_payment, add_ons,checkout, execute_click_by_text

class TestBookNowBase(unittest.TestCase):
    @allure.step("First Step to open the browser with title: {0}".format("Home"))
    def setUp(self):
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('data3.json',"r") 
        data = json.loads(f.read()) 
        self.driver.get(data["url_version3"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        f.close()

    @allure.step("Close the browser")
    def tearDown(self):
        self.driver.quit()


@allure.severity(allure.severity_level.CRITICAL)
class TestV3NewBooking(TestBookNowBase):

    # def test_01_Loginhere(self):
    #     try:
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         # Selectsite(self.driver, data["booking_date"], data["no_of_people"],data["site"])
    #         loginhere(self.driver, data["existinguser_id"], data["existinguser_password"])
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_02_giftvoucher(self):
    #     try:
    #             f = open('data3.json',"r") 
    #             data = json.loads(f.read()) 
    #             for aa in data["productlist"]:
    #                 print(aa)
    #                 execute_click_by_text(self.driver,aa)
    #                 datepicker(self.driver, data["date"])
    #                 quantity_selection(self.driver, data["no._of_adults"])
    #                 time_selection(self.driver,aa["timeslot"])
    #                 add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #                 add_product_to_cart(self.driver, aa["productname"])
    #             giftcard(self.driver, data["giftcard"])
    #             f.close()    
    #     except Exception as ex:
    #             allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #             raise ex

    # def test_03_promocode(self):
    #     try:
    #         firstname= names.get_first_name()
    #         lastname= names.get_last_name()
    #         customer_name='{0} {1}'.format(firstname,lastname)
    #         phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         for aa in data["productlistA"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             # add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #         promocode(self.driver, data["promocode"])
    #         amount= checkout(self.driver)
    #         # try:
    #         #     cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
    #         #     print(cart_item)
    #         # except:
    #         #     print("elements not in cart")
    #         # subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
    #         # print(subtotal)
    #         # create_account(self.driver,firstname,lastname,phone)
    #         # # payment_mode(self.driver, data["payment_via"])
    #         # share_payment(self.driver)
    #         # time.sleep(5)
    #         # allure.attach(self.driver.get_screenshot_as_png(), name = 'payment__screen', attachment_type = AttachmentType.PNG)
    #         # find_element_by_text(self.driver," Checkout").click()
    #         # card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
    #         # verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name,data["dummy"]) 
    #         f.close()    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_04_existing_login(self):
    #     try:
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         # Selectsite(self.driver, data["booking_date"], data["no_of_people"],data["site"])
    #         time.sleep(2)
    #         for aa in data["productlist1"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             # add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #         amount= checkout(self.driver)
    #         login(self.driver,data["existinguser_id"],data["existinguser_password"])
    #         f.close()    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_05_guest_checkout(self):
    #     try:
    #         firstname= names.get_first_name()
    #         lastname= names.get_last_name()
    #         customer_name='{0} {1}'.format(firstname,lastname)
    #         phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         cart_item=""
    #         subtotal=""
    #         # Selectsite(self.driver, data["booking_date"], data["no_of_people"],data["site"]) 
    #         time.sleep(2)
    #         for aa in data["productlist2"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             guest_avg_age(self.driver, data["avg_age"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             # add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #         amount= checkout(self.driver)
    #         checkout_as_guest(self.driver,firstname,lastname,phone)
    #         card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
    #         verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name, data["dummy"]) 
    #         f.close()    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_06_new_account_payment(self):
    #     try:
    #         firstname= names.get_first_name()
    #         lastname= names.get_last_name()
    #         customer_name='{0} {1}'.format(firstname,lastname)
    #         phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         # Selectsite(self.driver, data["booking_date"], data["no_of_people"],data["site"])
    #         time.sleep(2)
    #         for aa in data["productlist3"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #             time.sleep(8)
    #         amount= checkout(self.driver)
    #         try:
    #             cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
    #             print(cart_item)
    #         except:
    #             print("elements not in cart")
    #         subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
    #         print(subtotal)
    #         create_account(self.driver,firstname,lastname,phone)
    #         payment_mode(self.driver, data["payment_via"])
    #         card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
    #         verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name, data["dummy"]) 
    #         f.close()    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_07_invalid_promocode_giftvoucher(self):
    #     try:
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         for aa in data["productlistB"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #         invalidgiftcard(self.driver, data["npromocode"])
    #         f.close()    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex
    
    # def test_08_delete_item_from_cart(self):
    #     try:
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         time.sleep(5)
    #         for aa in data["productlistC"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #         time.sleep(4)
    #         delete_cart_item(self.driver, data["item_to_delete"])
    #         time.sleep(2)
    #         f.close()    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # @allure.description("To place an order with user logged in before checkout.")
    # def test_09_login_before_checkout(self):
    #     try:
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         # Selectsite(self.driver, data["booking_date"], data["no_of_people"],data["site"])
    #         loginhere(self.driver, data["existinguser_id"], data["existinguser_password"])
    #         time.sleep(2)
    #         for aa in data["productlist4"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #             time.sleep(2)
    #         amount= checkout(self.driver)
    #         try:
    #             cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
    #             print(cart_item)
    #         except:
    #             print("elements not in cart")
    #         subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
    #         print(subtotal)
    #         card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
    #         # verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name, data["dummy"]) 
    #         verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,data["existing_customer_name"],data["dummy"]) 
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # @allure.description("To selct a desired product with the help of filters")
    # def test_10_filter_products(self):
    #     try:
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         time.sleep(5)
    #         product_filter(self.driver, data["filter_date"], data["site"],"2","0","20", "Bundles")
    #         book_date= self.driver.find_element_by_xpath(filterselectors.pro_date).text
    #         assert book_date == data["filter_date"]
    #         for aa in data["productlistC"]:
    #             print(aa)
    #             item = find_element_by_text(self.driver, aa["productname"])
    #             print(item.text)
    #             assert item.text == "Beer-Pong" or item.text == "Rock Climbing"
    #             time.sleep(2)
    #         f.close()    

    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # @allure.description("To selct a desired product with the help of filters")
    # def test_11_filter_products_2(self):
    #     try:
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         time.sleep(5)
    #         product_filter(self.driver, data["filter_date"], data["site"],"2","20","100", "Other")
    #         book_date= self.driver.find_element_by_xpath(filterselectors.pro_date).text
    #         assert book_date == data["filter_date"]
    #         for aa in data["productlist2"]:
    #             print(aa)
    #             item = find_element_by_text(self.driver, aa["productname"])
    #             print(item.text)
    #             assert item.text == "Axe Throwing"
    #             time.sleep(2)
    #         f.close()    

    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_12_new_account_homepage(self):
    #     try:
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         firstname= names.get_first_name()
    #         lastname= names.get_last_name()
    #         customer_name='{0} {1}'.format(firstname,lastname)
    #         phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
    #         loginhere_new_account(self.driver, firstname, lastname, phone)
    #         for aa in data["productlist3"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #             time.sleep(8)
    #         amount= checkout(self.driver)
    #         try:
    #             cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
    #             print(cart_item)
    #         except:
    #             print("elements not in cart")
    #         subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
    #         print(subtotal)
    #         card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
    #         verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name, data["dummy"]) 
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_13_promocode_on_bookingfee(self):
    #     try:
    #         firstname= names.get_first_name()
    #         lastname= names.get_last_name()
    #         customer_name='{0} {1}'.format(firstname,lastname)
    #         phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         for aa in data["productlist2A"]:
    #             print(aa)
    #             execute_click_by_text(self.driver,aa)
    #             datepicker(self.driver, data["date"])
    #             quantity_selection(self.driver, data["no._of_adults"])
    #             time_selection(self.driver,aa["timeslot"])
    #             # add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #         promocode(self.driver, data["promocode"])
    #         amount= checkout(self.driver)
    #         try:
    #             cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
    #             print(cart_item)
    #         except:
    #             print("elements not in cart")
    #         subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
    #         print(subtotal)
    #         create_account(self.driver,firstname,lastname,phone)
    #         time.sleep(5)
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'payment__screen', attachment_type = AttachmentType.PNG)
    #         find_element_by_text(self.driver," Checkout").click()
    #         # card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
    #         verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name,data["dummy"]) 
    #         f.close()    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_14_giftvoucher_with_bookingfee(self):
    #     try:
    #             f = open('data3.json',"r") 
    #             data = json.loads(f.read()) 
    #             for aa in data["productlist2A"]:
    #                 print(aa)
    #                 execute_click_by_text(self.driver,aa)
    #                 datepicker(self.driver, data["date"])
    #                 quantity_selection(self.driver, data["no._of_adults"])
    #                 time_selection(self.driver,aa["timeslot"])
    #                 add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #                 add_product_to_cart(self.driver, aa["productname"])
    #             giftcard(self.driver, data["giftcard"])
    #             f.close()    
    #     except Exception as ex:
    #             allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #             raise 

    # def test_15_promocode_on_tax_product(self):
    #     try:
    #         firstname= names.get_first_name()
    #         lastname= names.get_last_name()
    #         customer_name='{0} {1}'.format(firstname,lastname)
    #         phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
    #         f = open('data3.json',"r") 
    #         data = json.loads(f.read()) 
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #         time.sleep(5)
    #         for aa in data["productlistTT"]:
    #             print(aa)
    #             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #             execute_click_by_text(self.driver,aa)
    #             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #             time.sleep(5)
    #             # datepicker(self.driver, data["date"])
    #             quantity_selection4(self.driver, data["no._of_adults"])
    #             time_selection4(self.driver,aa["timeslot"])
    #             # add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #             add_product_to_cart(self.driver, aa["productname"])
    #         promocode(self.driver, data["promocode"])
    #         amount= checkout(self.driver)
    #         try:
    #             cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
    #             print(cart_item)
    #         except:
    #             print("elements not in cart")
    #         subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
    #         print(subtotal)
    #         create_account(self.driver,firstname,lastname,phone)
    #         time.sleep(5)
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'payment__screen', attachment_type = AttachmentType.PNG)
    #         find_element_by_text(self.driver," Checkout").click()
    #         # card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
    #         verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name,data["dummy"]) 
    #         f.close()    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_16_giftvoucher_with_tax_product(self):
    #     try:
    #             f = open('data3.json',"r") 
    #             data = json.loads(f.read()) 
    #             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #             time.sleep(5)
    #             for aa in data["productlistTT"]:
    #                 print(aa)
    #                 self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #                 execute_click_by_text(self.driver,aa)
    #                 self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #                 time.sleep(5)
    #                 # datepicker(self.driver, data["date"])
    #                 quantity_selection4(self.driver, data["no._of_adults"])
    #                 time_selection(self.driver,aa["timeslot"])
    #                 add_ons(self.driver,data["quantity_add_on1"], data["quantity_add_on2"])
    #                 add_product_to_cart(self.driver, aa["productname"])
    #             giftcard(self.driver, data["giftcard"])
    #             f.close()    
    #     except Exception as ex:
    #             allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
    #             raise 

    def test_17_promocode_plus_giftvoucher(self):
        try:
            f = open('data3.json',"r") 
            data = json.loads(f.read()) 
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(5)
            for aa in data["productlist1"]:
                print(aa)
                execute_click_by_text(self.driver,aa)
                time.sleep(5)
                # datepicker(self.driver, data["date"])
                quantity_selection(self.driver, data["no._of_adults"])
                time_selection(self.driver,aa["timeslot"])
                add_product_to_cart(self.driver, aa["productname"])
            promocode(self.driver, data["promocode"])
            giftcard(self.driver, data["giftcard"])
            amount= checkout(self.driver)
            assert amount== "0.00"
            # try:
            #     cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
            #     print(cart_item)
            # except:
            #     print("elements not in cart")
            # subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
            # print(subtotal)
            # create_account(self.driver,firstname,lastname,phone)
            # time.sleep(5)
            # allure.attach(self.driver.get_screenshot_as_png(), name = 'payment__screen', attachment_type = AttachmentType.PNG)
            # find_element_by_text(self.driver," Checkout").click()
            # # card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            # verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name,data["dummy"]) 
            f.close()    
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
            raise ex


if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
    unittest.main()
