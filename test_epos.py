import time
import allure
import pytest
import json, names
from random import randint
from allure_commons.types import AttachmentType
import unittest
from selector import commonpath
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from methods import execute_click_by_text_on, find_element_by_text,login,execute_click_by_text_on2
from epos_method import itemselection, search_customer,select_table,increase_quantity,decrease_quantity
from epos_method import editing_saleitems, assertion,present_pastorder_navigation,payment,total_price_verification
from epos_method import zero_price_checkout,cancel_order,edit_parkedsale, new_account, table_assertion,giftcard,modify_cartitem
from epos_selector import loginselectors,epospageselector, paymentselectors
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

class TestBookNowBase(unittest.TestCase):
    
    def setUp(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver= webdriver.Chrome(commonpath.path,chrome_options=chrome_options)
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('data2.json',"r") 
        data = json.loads(f.read()) 
        self.driver.get(data["url_epos"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        login(self.driver,data["username"],data["password"],data["register"])
        f.close()
        
    def tearDown(self):
        self.driver.quit()

class TestEposBooking(TestBookNowBase):

    
    # @allure.description("Adding epos products to the cart without table selection")
    # def test_epos_01_item_selection(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
            
    #         total_price=itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)
    #         modify_cartitem(self.driver,data["item_to_modify"], data["epos_item_price"],data["epos_item_qty"], data["epos_item_dis"])
    #         total_price_verification(self.driver,data["firstepositem"],data["secondepositem"])
            
    #         # increase_quantity(self.driver)
    #         # decrease_quantity(self.driver)
    #         # time.sleep(4)
    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_02_gift_card(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
            
    #         total_price=itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)

    #         giftcard(self.driver, data["giftvoucher"])
    #         time.sleep(4)
            
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_03_promocode(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
            
    #         total_price=itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)

    #         giftcard(self.driver, data["promotionalcode"])
    #         time.sleep(4)
           
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex


    # def test_epos_04_table_selection(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
            
    #         total_price = itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)
    #         select_table(self.driver, "1")
    #         time.sleep(4)
    #         # table_assertion(self.driver,"Table 1")
            
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_05_order_placement(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         time.sleep(2)
    #         payment(self.driver,"1")
    #         assertion(self.driver)
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_06_existing_customer_search(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         search_customer(self.driver,data["existing_user"])
    #         time.sleep(2)
            
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_07_new_account(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         customerfirstname= names.get_first_name()
    #         customerlastname= names.get_last_name()
    #         cusomterphonenumber= ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
    #         time.sleep(3)
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         new_account(self.driver,customerfirstname, customerlastname, cusomterphonenumber)
    #         time.sleep(2)
            
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex


    # def test_epos_08_edit_parkedsale_item(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         time.sleep(2)
    #         total_price = itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)
    #         select_table(self.driver, "6")
    #         time.sleep(4)
    #         edit_parkedsale(self.driver,"6", "£6.00",data["newproductlist"])
    
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_09_moving_backnforth_from_payments_to_editsale(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
            
    #         total_price=itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)
    #         editing_saleitems(self.driver, data["newproductlist"])
    #         assertion(self.driver)

    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_10_cancel_an_order(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         time.sleep(2)
    #         total_price = itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)
    #         select_table(self.driver, "10")
    #         time.sleep(4)
    #         cancel_order(self.driver,"10")
            
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_11_kitchen_orders(self):
    #     try:
        
    #         present_pastorder_navigation(self.driver)
            
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    @allure.description("To create and modify parked sale items")
    def test_epos_12_creating_n_modifying_parked_sale(self):
        try:
            By_xpath= self.driver.find_element_by_xpath
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 
            
            total_price=itemselection(self.driver, data["epositem2"])      
            time.sleep(4)
            select_table(self.driver,"2")
            edit_parkedsale(self.driver,"2", "£6.00",data["newproductlist"])
            # assertion(self.driver)

        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
            raise ex

    # def test_epos_13_zero_price_checkout_promocode(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         total_price=itemselection(self.driver, data["epositem2"])      
    #         time.sleep(4)
    #         giftcard(self.driver, data["promotionalcode"])
    #         time.sleep(2)
    #         zero_price_checkout(self.driver)
    #         assertion(self.driver)
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_14_zero_price_checkout_giftcard(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         total_price=itemselection(self.driver, data["epositem2"])      
    #         time.sleep(4)
    #         giftcard(self.driver, data["giftvoucher"])
    #         time.sleep(2)
    #         zero_price_checkout(self.driver)
    #         assertion(self.driver)
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_15_zero_price_checkout_promocode_parkedsale(self):
    #     try:
    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         table_orders = By_xpath(epospageselector.table_xpath).text
    #         By_xpath("/html/body/span[2]/div[12]/div[1]/div/div/div[2]/div/div/div/table/tbody/tr[1]").click()
    #         time.sleep(2)
    #         giftcard(self.driver, data["promotionalcode"])
    #         time.sleep(2)
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'editsale_screen', attachment_type = AttachmentType.PNG)
    #         self.driver.find_element_by_id(epospageselector.save_yellow_btn).click()
    #         time.sleep(3)
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'modified_parkedsale_screen', attachment_type = AttachmentType.PNG)
    #         table_orders = By_xpath(epospageselector.table_xpath).text
    #         print(table_orders)
    #         assert "£0.00" in table_orders
    #         find_element_by_text(self.driver,"£0.00").click()
    #         time.sleep(4)
    #         zero_price_checkout(self.driver)
    #         assertion(self.driver)
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex

    # def test_epos_16_order_placement_with_duplicate_tablenumber(self):
    #     try:

    #         By_xpath= self.driver.find_element_by_xpath
    #         f = open('data2.json',"r") 
    #         data = json.loads(f.read()) 
    #         time.sleep(2)
    #         total_price = itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)
    #         select_table(self.driver, "1")
    #         time.sleep(1)
    #         total_price = itemselection(self.driver, data["epositem"])      
    #         time.sleep(4)
    #         select_table(self.driver, "1")
    #         time.sleep(1)
    #         table_err= By_xpath(epospageselector.table_number_error).text 
    #         print(table_err)      
    #         assert table_err == "There is already a parked sale saved to this table."

    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_error_screen', attachment_type = AttachmentType.PNG)
    #         raise ex


if __name__ == '__main__':
    unittest.main()
