import unittest, time, names
import allure, pytest, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selector import commonpath, confirmationpageselectors, customersearchselectors,bookingpageselectors
from membership_selectors import homepageselectors,bookingpageselectors2, loginselectors, paymentselector,successpageselectors
from membership_methods import select_member,multiple_participants, participant_detail, card_payment, signup, membership_verification
from methods import login,execute_click_by_text_on,find_element_by_text, birthday_submodule,add_to_sale,find_element_by_text_input,find_element_by_text_div
from methods import remove_from_cart, giftvoucher, card_payment,epos_payment, skip_payment, send_payment_link, assertion, discount, checkout
from methods import date_picker, time_picker,existing_customer,adding_newcustomer,additionalitem_add_to_sale
from methods import date_and_time_verification,invalid_promocode,promocode,site_selection, birthday_product, login, skate_product, birthday_product2, details_verfication
from methods import execute_click_by_text_on,find_element_by_text, birthday_submodule,add_to_sale,find_element_by_text_input,find_element_by_text_div
class TestBookNowBase(unittest.TestCase):
    
    def setUp(self):
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('data2.json',"r") 
        data = json.loads(f.read()) 
        self.driver.get(data["url_customersearch"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        login(self.driver,data["username"],data["password"],data["register"])
        f.close()
        
    def tearDown(self):
        self.driver.quit()

class TestV3MembershipBooking(TestBookNowBase):

    @allure.description("To book a memebership product")
    def test_01_book_a_membership_product(self):
        try:
            By_xpath= self.driver.find_element_by_xpath
            f = open('member_data.json',"r") 
            data = json.loads(f.read())
            select_member(self.driver, data["member_name"])
            f.close()
            f= open('data2.json',"r")
            data= json.loads(f.read())
            By_xpath(bookingpageselectors2.mem_prod_btn).click()

            amount='0'
            for aa in data["productlist6"]:
                print(aa)
                By_xpath(bookingpageselectors2.membership_product).click()
                date_picker(self.driver,aa["date"],aa["quantity"])
                time_picker(self.driver,aa["time"])
                add_to_sale(self.driver, aa["productname"],aa["date"],aa["time"])
                product= aa["productname"]
                product_quantity= aa["quantity"]
                timeslot= aa["time"]
           
            itemname= ""
            item_quantity= ""
            
            product_price= str(By_xpath(bookingpageselectors.actual_amount_xpath).text)
            print(product_price)
            checkout(self.driver)
            amount= card_payment(self.driver,data["cardnumber"],data["cardholdername"],data["expiry"],data["cvc"])
            time.sleep(5)
            booking_number=self.driver.find_element_by_xpath(customersearchselectors.booking_number_xpath).text
            print(booking_number)
            customer_name= self.driver.find_element_by_xpath(customersearchselectors.customer_name_xpath).text
            print(customer_name)
            details_verfication(self.driver,data["site"],customer_name,product,itemname,product_quantity,timeslot,item_quantity,amount,product_price)
            time.sleep(4)
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_failure01', attachment_type = AttachmentType.PNG)
            raise ex

if __name__ == '__main__':
        unittest.main()