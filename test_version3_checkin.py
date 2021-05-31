import time
import allure
import pytest
import json
from allure_commons.types import AttachmentType
import unittest
from methods import additionalitem_add_to_sale,execute_click_by_text_on, date_picker,time_picker,add_to_sale,checkout,epos_payment,card_payment,giftvoucher, promocode,discount
from methods import login,find_element_by_text,find_element_by_text_div, find_element_by_text_input,execute_click_by_text,execute_click_by_text_on2
from selector import commonpath,customersearchselectors
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from checkin_selector import loginselectors,checkinpageselectors,refundpageselectors
from checkin_methods import got_to_add_products,uncancel_a_booking, check_in, select_booking, change_datetime,info
from checkin_methods import refund_product_via_no_refund,refund_product_via_new_giftcard,refund_product_via_giftcard,refund_product_via_credit_card,refund_product_via_epos,adding_notes,cancel_refund,site_selection
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

class TestBookNowBase(unittest.TestCase):
    
    def setUp(self):
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('data2.json',"r") 
        data = json.loads(f.read()) 
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver= webdriver.Chrome(commonpath.path,chrome_options=chrome_options)
        self.driver.get(data["url_customersearch"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        login(self.driver,data["username"],data["password"],data["register"])
        f.close()
        
    def tearDown(self):
       
        self.driver.quit()


class TestV3CheckInBooking(TestBookNowBase):
    '''Checkin details: info, change date/time, checking booking details,
    # cancel booking, adding notes and finally check in the customer'''

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Checkin details: check in the customer")
    def test_01_checkin(self):
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 	
            # site_selection(self.driver,data["site"])		
            select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])
            check_in(self.driver,data["waiver"])
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To add Notes to the booking")
    def test_02_notes(self):
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 	
            # site_selection(self.driver,data["site"])		
            select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])
            # adding_notes(self.driver,data["note"])
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Checkin details: info")
    def test_03_info(self):
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 	
            # site_selection(self.driver,data["site"])		
            select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])
            info(self.driver)
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To change date/time of booking")
    def test_04_change_datetime(self):
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 	
            # site_selection(self.driver,data["site"])		
            select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])            
            time.sleep(3)
            change_datetime(self.driver,data["checkin_date"],data["booking_number"])    
            table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
            print(table)
            assert data["booking_number"] in table        
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To cancel and then uncancel the booking")
    def test_05_cancel_uncancel_a_booking(self):
        try:    
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 	
            # site_selection(self.driver,data["site"])		
            select_booking(self.driver,data["checkin_customer_name2"],data["booking_number2"])    
            uncancel_a_booking(self.driver)
            time.sleep(2)
            table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
            print(table)
            assert data["booking_number2"] in table
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To cancel the booking")
    def test_06_cancelbooking(self):
        try:    
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 	
            # site_selection(self.driver,data["site"])		
            select_booking(self.driver,data["checkin_customer_name3"],data["booking_number3"])    
            cancel_refund(self.driver, data["checkin_date"])
            time.sleep(2)
            table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
            print(table)
            assert data["booking_number3"] not in table
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex
    
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To remove and refund all the products")
    def test_07_refund_all_via_buynow(self):
        try:    
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 		
            select_booking(self.driver,data["checkin_customer_name4"],data["booking_number4"])    
            refund_product_via_epos(self.driver)
            time.sleep(2)
            table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
            print(table)
            assert data["booking_number4"] not in table
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To remove and refund all the products")
    def test_08_refund_all_via_online_creditcard(self):
        try:    
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 		
            select_booking(self.driver,data["checkin_customer_name5"],data["booking_number5"])    
            refund_product_via_credit_card(self.driver)
            time.sleep(2)
            table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
            print(table)
            assert data["booking_number5"] not in table
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To add more products to the booking via refunds section")
    def test_09_add_more_products(self):
        By_xpath= self.driver.find_element_by_xpath
        By_ID= self.driver.find_element_by_id
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 		
            select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])    
            got_to_add_products(self.driver)
            iframe = By_ID(refundpageselectors.iframe2)
            self.driver.switch_to.frame(iframe)
            # for aa in data["productlist11"]:
            #     execute_click_by_text_on(self.driver, aa)
            #     date_picker(self.driver,aa["date"],aa["quantity"])
            #     time_picker(self.driver,aa["time"])
            #     pp=add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
                                    
            #     product= aa["productname"]   
            #     product_quantity=aa["quantity"]
            #     timeslot=aa["time"]
            # print(product_quantity)
            # print(timeslot)

            for bb in data["additionalitemlist"]:
                if data["itemtype"]== bb["itemgroup"]:
                    print (bb)
                    execute_click_by_text_on(self.driver,bb)
                    time.sleep(3)
                    additionalitem_add_to_sale(self.driver,bb["quantity"],bb["itemname"] )
                    itemname= bb["itemname"]
                    item_quantity= bb["quantity"]
        
            checkout(self.driver)
            amount= epos_payment(self.driver)
            time.sleep(2)
            self.driver.switch_to.default_content()
            time.sleep(5)
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
            raise ex  


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To remove and refund all the products")
    def test_10_refund_all_via_exsisting_gift_card(self):
        try:    
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 		
            select_booking(self.driver,data["checkin_customer_name6"],data["booking_number6"])    
            refund_product_via_giftcard(self.driver, data["giftvoucher"])
            time.sleep(2)
            table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
            print(table)
            assert data["booking_number6"] not in table
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To remove and refund all the products")
    def test_11_refund_all_via_new_gift_card(self):
        try:    
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 		
            select_booking(self.driver,data["checkin_customer_name7"],data["booking_number7"])    
            refund_product_via_new_giftcard(self.driver,data["new_giftcard"])
            time.sleep(2)
            table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
            print(table)
            assert data["booking_number7"] not in table
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To remove and refund all the products")
    def test_12_refund_all_via_no_refund(self):
        try:    
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 		
            select_booking(self.driver,data["checkin_customer_name8"],data["booking_number8"])    
            refund_product_via_no_refund(self.driver)
            time.sleep(2)
            table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
            print(table)
            assert data["booking_number8"] not in table
            f.close()
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
            raise ex
    
   
if __name__ == '__main__':
    unittest.main()



        