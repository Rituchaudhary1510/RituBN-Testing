import allure
import pytest
import time
import unittest
import names
import os
import json 
from selenium.webdriver.chrome.options import Options
from random import randint
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from newbooking_selector import newbookingpageselectors,loginselectors
from v2_staff_methods import find_element_by_text, execute_click_by_text_on
from selenium.webdriver.support.ui import Select
from v2_staff_selector import commonpath
from newbooking_methods import billing, confirmationselectors, bookingconfirmation, site_selection, date_picker,next_step2, next_step3, next_step4, add_to_sale
from newbooking_methods import additionalitems, birthday_module, adding_notes, login_checkout,create_new_account
from newbooking_methods import card_payment,promocode, promocode_error, express_checkout, assertion
from newbooking_methods import waiverform, childwaiverform, home_login, reset_password

class TestBookNowBase(unittest.TestCase):
    
    def setUp(self):

        self.driver= webdriver.Chrome(commonpath.path)
        f = open('v2.json',"r") 
        data = json.loads(f.read()) 
        self.driver.get(data["url_newbooking"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        f.close()

    def tearDown(self):
        self.driver.quit()

class TestCustomerBooking(TestBookNowBase): 

    @allure.description("This test case is to test site selection, booking date, selected product in cart,login with existing customer account and payment with promocode")
    def test_01_existing_user_login_with_promocode(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            birthdayperson_name=names.get_first_name()
            time.sleep(3)

            site_selection(self.driver,data["site"])
            time.sleep(7)
            date_picker(self.driver,data["date"])
            By_name(newbookingpageselectors.nextstep_name).click()
            time.sleep(3)
            for aa in data["productlist"]:
                    print (aa)
                    execute_click_by_text_on(self.driver,aa)
                    time.sleep(2)
                    add_to_sale(self.driver,aa["producttype"],aa["productname"],aa["quantity"],aa["time"])
                    time.sleep(4)
            time.sleep(2)
            next_step2(self.driver)
            # birthday_module(self.driver,birthdayperson_name,data["birthdayperson_age"],data["text"])
            # additionalitems(self.driver)
            # time.sleep(3)
            # next_step3(self.driver)
            # time.sleep(2)
            login_checkout(self.driver,data["username"],data["password"])
            # create_new_account(self.driver,customerfirstname,customerlastname,cusomterphonenumber)
            time.sleep(2)
            next_step4(self.driver)
            customername= By_xpath(newbookingpageselectors.name_of_customer).text
            assert customername == "Luke Sims"
            product_table=By_xpath(confirmationselectors.cart_item).text
            adding_notes(self.driver,data["note"])
            # amount=card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            amount=promocode(self.driver,data["promotionalcode"])
            time.sleep(5)
            try:
                try:
                    By_name(newbookingpageselectors.promocode_checkout_name).click()
                    assert True
                except:
                    By_xpath(newbookingpageselectors.promocode_checkout_name2).click()
            except:
                promocode_error(self.driver)
                assert False
                # card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            time.sleep(5)
            bookingconfirmation(self.driver,data["site"],data["customerfirstname"],data["customerlastname"],amount,product_table)
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception-error_screenshot', attachment_type = AttachmentType.PNG)
            raise ex
    
    
    @allure.description("This test is to verify product booking with new customer account and payment through card")
    def test_02_new_account(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            customerfirstname= names.get_first_name()
            customerlastname= names.get_last_name()
            customer_name='{0} {1}'.format(customerfirstname, customerlastname)
            birthdayperson_name=names.get_first_name()
            cusomterphonenumber= ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
            time.sleep(3)
            
            site_selection(self.driver,data["site"])
            time.sleep(5)
            date_picker(self.driver,data["date"])
            By_name(newbookingpageselectors.nextstep_name).click()
            time.sleep(3)
            for aa in data["productlist2"]:
                # if aa["producttype"] == "Bundles":
                    print (aa)
                    execute_click_by_text_on(self.driver,aa)
                    time.sleep(2)
                    add_to_sale(self.driver,aa["producttype"],aa["productname"],aa["quantity"],aa["time"])
                    time.sleep(4)
            time.sleep(2)
            next_step2(self.driver)
            # birthday_module(self.driver,birthdayperson_name,data["birthdayperson_age"],data["text"])
            # additionalitems(self.driver)
            # time.sleep(3)
            # next_step3(self.driver)
            time.sleep(2)
            create_new_account(self.driver,customerfirstname,customerlastname,cusomterphonenumber)
            time.sleep(2)
            next_step4(self.driver)
            customername= By_xpath(newbookingpageselectors.name_of_customer).text
            assert customername == customer_name
            product_table=By_xpath(confirmationselectors.cart_item).text
            adding_notes(self.driver,data["note"])
            # amount=card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            # time.sleep(15)
            # bookingconfirmation(self.driver,data["site"],customerfirstname,customerlastname,amount,product_table)        
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception-error_screenshot', attachment_type = AttachmentType.PNG)
            raise ex
    
    @allure.description("This test is to test express checkout login")
    def test_03_expresscheckout(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            customerfirstname= names.get_first_name()
            customerlastname= names.get_last_name()
            customer_name='{0} {1}'.format(customerfirstname, customerlastname)
            birthdayperson_name=names.get_first_name()
            cusomterphonenumber= ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
            time.sleep(3)
            site_selection(self.driver,data["site"])
            time.sleep(5)
            date_picker(self.driver,data["date"])
            By_name(newbookingpageselectors.nextstep_name).click()
            time.sleep(3)
            for aa in data["productlist3"]:
                # if data['producttype'] == aa["producttype"]:
                    print (aa)
                    time.sleep(5)
                    execute_click_by_text_on(self.driver,aa)
                    time.sleep(2)
                    add_to_sale(self.driver,aa["producttype"],aa["productname"],aa["quantity"],aa["time"])
                    time.sleep(4)
            time.sleep(5)
            next_step2(self.driver)
            # birthday_module(self.driver,birthdayperson_name,data["birthdayperson_age"],data["text"])
            # additionalitems(self.driver)
            # time.sleep(3)
            # next_step3(self.driver)
            time.sleep(2)
            # login_checkout(self.driver,data["username"],data["password"])
            express_checkout(self.driver, customerfirstname,customerlastname,cusomterphonenumber)
            # create_new_account(self.driver,customerfirstname,customerlastname,cusomterphonenumber)
            time.sleep(3)
            next_step4(self.driver)
            time.sleep(3)
            customername= By_xpath(newbookingpageselectors.name_of_customer).text
            assert customername == customer_name
            # product_table=By_xpath(confirmationselectors.cart_item).text
            # adding_notes(self.driver,data["note"])
            # amount=card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            # time.sleep(15)
            # bookingconfirmation(self.driver,data["site"],customerfirstname,customerlastname,amount,product_table)        
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception-error_screenshot', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To verify adding an invalid promocode gives the correct error messages.")    
    def test_04_invalid_promocode_error_msgs(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            customerfirstname= names.get_first_name()
            customerlastname= names.get_last_name()
            customer_name='{0} {1}'.format(customerfirstname, customerlastname)
            birthdayperson_name=names.get_first_name()
            cusomterphonenumber= ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
            time.sleep(3)
           
            site_selection(self.driver,data["site"])
            time.sleep(5)
            date_picker(self.driver,data["date"])
            By_name(newbookingpageselectors.nextstep_name).click()
            time.sleep(3)
            for aa in data["productlist2"]:
                # if data['producttype'] == aa["producttype"]:
                    print (aa)
                    # By_xpath("/html/body/span[2]/main/span[2]/span[4]/div[3]/div/div[1]/div[5]/div/div/h4").click()
                    time.sleep(5)
                    execute_click_by_text_on(self.driver,aa)
                    time.sleep(2)
                    add_to_sale(self.driver,aa["producttype"],aa["productname"],aa["quantity"],aa["time"])
                    time.sleep(4)
            time.sleep(5)
            next_step2(self.driver)
            # birthday_module(self.driver,birthdayperson_name,data["birthdayperson_age"],data["text"])
            # additionalitems(self.driver)
            time.sleep(3)
            next_step3(self.driver)
            time.sleep(2)
            login_checkout(self.driver,data["username"],data["password"])
            # express_checkout(self.driver, customerfirstname,customerlastname,cusomterphonenumber)
            # create_new_account(self.driver,customerfirstname,customerlastname,cusomterphonenumber)
            time.sleep(4)
            next_step4(self.driver)
            time.sleep(4)
            customername= By_xpath(newbookingpageselectors.name_of_customer).text
            assert customername == "Luke Sims"
            try:
                product_table=By_xpath(confirmationselectors.cart_item).text
            except:
                # product_table="Unit Price Quantity Total BookingDate BookingTime"
                product_table=By_xpath(confirmationselectors.cart_item2).text
            # adding_notes(self.driver,data["note"])
            # amount=card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            amount=promocode(self.driver,data["promotionalcode2"])
            time.sleep(2)
            promocode_error(self.driver)
            By_name(newbookingpageselectors.promotional_code_name).clear()
            promocode(self.driver,"Test100")
            try:
                By_name(newbookingpageselectors.promocode_checkout_name).click()
                assert False
            except:
                promocode_error(self.driver)
                By_name(newbookingpageselectors.promotional_code_name).clear()
                promocode(self.driver,"100dis")
                try:
                    By_name(newbookingpageselectors.promocode_checkout_name).click()
                except:
                    promocode_error(self.driver)
                    time.sleep(2)
                # card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
                # time.sleep(5)
                # bookingconfirmation(self.driver,data["site"],data["customerfirstname"],data["customerlastname"],amount,product_table) 
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception-error_screenshot', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To verify adding an invalid promocode gives the correct error messages.")    
    def test_05_invalid_giftvoucher_n_checkout(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            customerfirstname= names.get_first_name()
            customerlastname= names.get_last_name()
            customer_name='{0} {1}'.format(customerfirstname, customerlastname)
            cusomterphonenumber= ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
            time.sleep(3)
           
            site_selection(self.driver,data["site"])
            time.sleep(5)
            date_picker(self.driver,data["date"])
            By_name(newbookingpageselectors.nextstep_name).click()
            time.sleep(3)
            for aa in data["productlist2"]:
                    print (aa)
                    # By_xpath("/html/body/span[2]/main/span[2]/span[4]/div[3]/div/div[1]/div[5]/div/div/h4").click()
                    time.sleep(5)
                    execute_click_by_text_on(self.driver,aa)
                    time.sleep(2)
                    add_to_sale(self.driver,aa["producttype"],aa["productname"],aa["quantity"],aa["time"])
                    time.sleep(4)
            next_step2(self.driver)
            time.sleep(3)
            # login_checkout(self.driver,data["username"],data["password"])
            express_checkout(self.driver, customerfirstname,customerlastname,cusomterphonenumber)
            time.sleep(4)
            next_step4(self.driver)
            time.sleep(4)
            customername= By_xpath(newbookingpageselectors.name_of_customer).text
            assert customername == customer_name
            try:
                product_table=By_xpath(confirmationselectors.cart_item).text
            except:
                # product_table="Unit Price Quantity Total BookingDate BookingTime"
                product_table=By_xpath(confirmationselectors.cart_item2).text
            amount=promocode(self.driver,data["promotionalcode3"])
            time.sleep(2)            
            promocode_error(self.driver)
            By_name(newbookingpageselectors.promotional_code_name).clear()
            promocode(self.driver,"Expvoucher")
            try:
                By_name(newbookingpageselectors.promocode_checkout_name).click()
                assert False
            except:
                promocode_error(self.driver)
                By_name(newbookingpageselectors.promotional_code_name).clear()
                promocode(self.driver,"Testv2")
                try:
                    self.driver.execute_script("window.scroll(0, 0)")
                    By_name(newbookingpageselectors.promocode_checkout_name).click()
                except:
                    promocode_error(self.driver)
                time.sleep(2)
                # bookingconfirmation(self.driver,data["site"],data["customerfirstname"],data["customerlastname"],amount,product_table)
                bookingconfirmation(self.driver,data["site"],customerfirstname,customerlastname,amount,product_table)        
                # self.driver.find_element_by_link_text("Waivers need to be completed for all participants – Click here to fill out your waiver now!").click()
                # time.sleep(4)
                # try:
                #     find_element_by_text(self.driver, "Accept").click()
                # except:
                #     print("skip accept button")
                # # find_element_by_text(self.driver,"24 Hour Waiver").click()
                # time.sleep(2)
                # childwaiverform(self.driver,firstname,lastname,phone,minorfirstname,lastname)
                # waiverform(self.driver,firstname,lastname,phone)
                # find_element_by_text(self.driver,"Ok").click()
                time.sleep(2)
            
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception-error_screenshot', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To verify adding an invalid promocode gives the correct error messages.")    
    def test_06_card_payment(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read())
            time.sleep(3)
            site_selection(self.driver,data["site"])
            time.sleep(5)
            date_picker(self.driver,data["date"])
            By_name(newbookingpageselectors.nextstep_name).click()
            time.sleep(3)
            for aa in data["productlist2"]:
                # if data['producttype'] == aa["producttype"]:
                    print (aa)
                    # By_xpath("/html/body/span[2]/main/span[2]/span[4]/div[3]/div/div[1]/div[5]/div/div/h4").click()
                    time.sleep(5)
                    execute_click_by_text_on(self.driver,aa)
                    time.sleep(2)
                    add_to_sale(self.driver,aa["producttype"],aa["productname"],aa["quantity"],aa["time"])
                    time.sleep(4)
            time.sleep(5)
            next_step2(self.driver)
            time.sleep(2)
            login_checkout(self.driver,data["username"],data["password"])
            time.sleep(4)
            next_step4(self.driver)
            time.sleep(4)
            customername= By_xpath(newbookingpageselectors.name_of_customer).text
            assert customername == "Luke Sims"
            try:
                product_table=By_xpath(confirmationselectors.cart_item).text
            except:
                # product_table="Unit Price Quantity Total BookingDate BookingTime"
                product_table=By_xpath(confirmationselectors.cart_item2).text
            adding_notes(self.driver,data["note"])
            amount=card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            bookingconfirmation(self.driver,data["site"],data["customerfirstname"],data["customerlastname"],amount,product_table) 
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception-error_screenshot', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To test promocode readded")
    def test_07_promocode_readd(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            birthdayperson_name=names.get_first_name()
            time.sleep(3)

            site_selection(self.driver,data["site"])
            time.sleep(7)
            date_picker(self.driver,data["date"])
            By_name(newbookingpageselectors.nextstep_name).click()
            time.sleep(3)
            for aa in data["productlist"]:
                    print (aa)
                    execute_click_by_text_on(self.driver,aa)
                    time.sleep(2)
                    add_to_sale(self.driver,aa["producttype"],aa["productname"],aa["quantity"],aa["time"])
                    time.sleep(4)
            time.sleep(2)
            next_step2(self.driver)
            birthday_module(self.driver,birthdayperson_name,data["birthdayperson_age"],data["text"])
            additionalitems(self.driver)
            time.sleep(3)
            next_step3(self.driver)
            time.sleep(2)
            login_checkout(self.driver,data["username"],data["password"])
            # create_new_account(self.driver,customerfirstname,customerlastname,cusomterphonenumber)
            time.sleep(2)
            next_step4(self.driver)
            customername= By_xpath(newbookingpageselectors.name_of_customer).text
            assert customername == "Luke Sims"
            product_table=By_xpath(confirmationselectors.cart_item).text
            adding_notes(self.driver,data["note"])
            amount=promocode(self.driver,data["promotionalcode"])
            time.sleep(2)
            By_xpath("/html/body/span[2]/main/span[2]/span[3]/div/div/form/span[4]/div/div/div[1]/input").click()
            time.sleep(4)
            By_xpath("/html/body/span[2]/main/span[2]/span[4]/div/div/form/span/span/div/div/div[2]/input").click()
            time.sleep(2)
            amount=promocode(self.driver,data["promotionalcode"])
            time.sleep(2)
            try:
                By_xpath("/html/body/span[2]/main/span[2]/span[3]/div/div/form/span[4]/div/div/div[2]/input").click()
            except:
                promocode_error(self.driver)
                # card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            time.sleep(5)
            bookingconfirmation(self.driver,data["site"],data["customerfirstname"],data["customerlastname"],amount,product_table)
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception-error_screenshot', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To test readdition of giftvouchers")
    def test_08_giftvoucher_readd(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            f = open('v2.json',"r") 
            data = json.loads(f.read()) 
            birthdayperson_name=names.get_first_name()
            time.sleep(3)

            site_selection(self.driver,data["site"])
            time.sleep(7)
            date_picker(self.driver,data["date"])
            By_name(newbookingpageselectors.nextstep_name).click()
            time.sleep(3)
            for aa in data["productlist"]:
                    print (aa)
                    execute_click_by_text_on(self.driver,aa)
                    time.sleep(2)
                    add_to_sale(self.driver,aa["producttype"],aa["productname"],aa["quantity"],aa["time"])
                    time.sleep(4)
            time.sleep(2)
            next_step2(self.driver)
            birthday_module(self.driver,birthdayperson_name,data["birthdayperson_age"],data["text"])
            additionalitems(self.driver)
            time.sleep(3)
            next_step3(self.driver)
            time.sleep(2)
            login_checkout(self.driver,data["username"],data["password"])
            # create_new_account(self.driver,customerfirstname,customerlastname,cusomterphonenumber)
            time.sleep(2)
            next_step4(self.driver)
            customername= By_xpath(newbookingpageselectors.name_of_customer).text
            assert customername == "Luke Sims"
            product_table=By_xpath(confirmationselectors.cart_item).text
            adding_notes(self.driver,data["note"])
            amount=promocode(self.driver,data["giftvoucher"])
            time.sleep(2)
            By_xpath("/html/body/span[2]/main/span[2]/span[3]/div/div/form/span[4]/div/div/div[1]/input").click()
            time.sleep(4)
            By_xpath("/html/body/span[2]/main/span[2]/span[4]/div/div/form/span/span/div/div/div[2]/input").click()
            time.sleep(2)
            amount=promocode(self.driver,data["giftvoucher"])
            time.sleep(2)
            try:
                By_xpath("/html/body/span[2]/main/span[2]/span[3]/div/div/form/span[4]/div/div/div[2]/input").click()
            except:
                promocode_error(self.driver)
                # card_payment(self.driver,data["cardholdername"],data["cardnumber"],data["expirymonth"],data["expiryyear"],data["cvc"])
            time.sleep(5)
            bookingconfirmation(self.driver,data["site"],data["customerfirstname"],data["customerlastname"],amount,product_table)
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception-error_screenshot', attachment_type = AttachmentType.PNG)
            raise ex

if __name__ == '__main__':
        unittest.main()


