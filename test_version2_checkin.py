import time, json
import allure, pytest, unittest
from allure_commons.types import AttachmentType
from selenium.webdriver.support.color import Color
from v2_staff_methods import login,find_element_by_text,find_element_by_text_div, find_element_by_text_input
from v2_staff_selector import commonpath,customersearchselectors
from selenium import webdriver
from v2_staff_methods import execute_click_by_text_on, date_picker, time_picker, add_to_sale, checkout,epos_payment
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from checkin_selector import refundpageselectors, checkinpageselectors
from checkin_methods import refund_product_via_no_refund, refund_product_via_new_giftcard, refund_product_via_giftcard, got_to_add_products
from v2_checkin_selector import loginselectors,checkinpageselectors, refundpageselectors
from v2_checkin_methods import room_verification,refund_product_via_epos, refund_product_via_credit_card, uncancel_a_booking,check_in, select_booking, change_datetime,info, adding_notes,cancel_refund,site_selection
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

class TestBookNowBase(unittest.TestCase):
    
    def setUp(self):
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('v2.json',"r") 
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


class TestV2CheckInBooking(TestBookNowBase):
    '''Checkin details: info, change date/time, checking booking details,
    cancel booking, adding notes and finally check in the customer'''

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("Checkin details: check in the customer")
    # def test_01_checkin(self):
    #     try:
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 	
    #         # site_selection(self.driver,data["site"])		
    #         select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])
    #         check_in(self.driver,data["waiver"])
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex 

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To add Notes to the booking")
    # def test_02_notes(self):
    #     try:
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 	
    #         # site_selection(self.driver,data["site"])		
    #         select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])
    #         # adding_notes(self.driver,data["note"])
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("Checkin details: info")
    # def test_03_info(self):
    #     try:
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 	
    #         # site_selection(self.driver,data["site"])		
    #         select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])
    #         info(self.driver)
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To change date/time of booking")
    # def test_04_change_datetime(self):
    #     try:
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 	
    #         # site_selection(self.driver,data["site"])		
    #         select_booking(self.driver,data["checkin_customer_name"],data["booking_number"])            
    #         change_datetime(self.driver,data["checkin_date"],data["booking_number"]) 
    #         table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
    #         print(table)
    #         assert data["booking_number"] in table           
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To cancel the booking")
    # def test_05_cancelbooking(self):
    #     try:    
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 	
    #         # site_selection(self.driver,data["site"])		
    #         select_booking(self.driver,data["checkin_customer_name3"],data["booking_number3"])    
    #         cancel_refund(self.driver, data["checkin_date"])
    #         time.sleep(2)
    #         table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
    #         print(table)
    #         assert data["booking_number3"] not in table
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex
    
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To cancel the booking")
    # def test_06_uncancelbooking(self):
    #     try:    
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 	
    #         # site_selection(self.driver,data["site"])		
    #         select_booking(self.driver,data["checkin_customer_name2"],data["booking_number2"])    
    #         uncancel_a_booking(self.driver)
    #         time.sleep(2)
    #         table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
    #         print(table)
    #         assert data["booking_number2"] in table
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex
    
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To remove and refund all the products")
    # def test_07_refund_all_via_buynow(self):
    #     try:    
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 		
    #         select_booking(self.driver,data["checkin_customer_name4"],data["booking_number4"])    
    #         refund_product_via_epos(self.driver)
    #         time.sleep(2)
    #         table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
    #         print(table)
    #         assert data["booking_number4"] not in table
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex
    
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To remove and refund all the products")
    # def test_08_refund_all_via_online_creditcard(self):
    #     try:    
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 		
    #         select_booking(self.driver,data["checkin_customer_name5"],data["booking_number5"])    
    #         refund_product_via_credit_card(self.driver)
    #         time.sleep(2)
    #         table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
    #         print(table)
    #         assert data["booking_number5"] not in table
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex

    # @allure.description("To verify room with moved booking")
    # def test_09_verify_room_with_moved_booking(self):
    #     try:    
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 		
    #         select_booking(self.driver,data["checkin_customer_name9"],data["booking_number9"])    
    #         room_verification(self.driver)
    #         change_datetime(self.driver,data["birthday_date"],data["booking_number9"]) 
    #         room_verification(self.driver)           
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex
    
    # @allure.description("To add more products to the booking via refunds section")
    # def test_10_add_more_products(self):
    #     By_xpath= self.driver.find_element_by_xpath
    #     By_ID= self.driver.find_element_by_id
    #     try:
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 		
    #         select_booking(self.driver,data["checkin_customer_name2"],data["booking_number2"])    
    #         got_to_add_products(self.driver)
    #         iframe = By_ID(refundpageselectors.iframe2)
    #         self.driver.switch_to.frame(iframe)
    #         for aa in data["productlist11"]:
    #             execute_click_by_text_on(self.driver, aa)
    #             product_date=date_picker(self.driver,aa["date"])
    #             time_picker(self.driver,aa["time"])
    #             add_to_sale(self.driver,aa["quantity"],aa["productname"]) 
        
    #         checkout(self.driver)
    #         amount= epos_payment(self.driver)
    #         time.sleep(2)
    #         self.driver.switch_to.default_content()
    #         time.sleep(5)
    #         f.close()
        
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
    #         raise ex  

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To remove and refund all the products")
    # def test_11_refund_all_via_exsisting_gift_card(self):
    #     try:    
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 		
    #         select_booking(self.driver,data["checkin_customer_name6"],data["booking_number6"])    
    #         refund_product_via_giftcard(self.driver, data["giftvoucher"])
    #         time.sleep(2)
    #         table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
    #         print(table)
    #         assert data["booking_number6"] not in table
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.description("To remove and refund all the products")
    # def test_12_refund_all_via_new_gift_card(self):
    #     try:    
    #         f = open('v2.json',"r") 
    #         data = json.loads(f.read()) 		
    #         select_booking(self.driver,data["checkin_customer_name7"],data["booking_number7"])    
    #         refund_product_via_new_giftcard(self.driver,data["new_giftcard"])
    #         time.sleep(2)
    #         table= self.driver.find_element_by_xpath(checkinpageselectors.booking_data).text
    #         print(table)
    #         assert data["booking_number7"] not in table
    #         f.close()
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'checkin_screenfailure_image', attachment_type = AttachmentType.PNG)
    #         raise ex

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("To remove and refund all the products")
    def test_13_refund_all_via_no_refund(self):
        try:    
            f = open('v2.json',"r") 
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



        