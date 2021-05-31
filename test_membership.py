import unittest, time, names
import allure, pytest, json
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
from membership_selectors import homepageselectors, loginselectors
from membership_methods import multiple_participants,login, participant_detail, card_payment, signup, membership_verification
from methods import execute_click_by_text_on,find_element_by_text, birthday_submodule,add_to_sale,find_element_by_text_input,find_element_by_text_div

class TestBookNowBase(unittest.TestCase):
    
    def setUp(self):
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('data2.json',"r") 
        data = json.loads(f.read()) 
        self.driver.get(data["url_membership"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        # login(self.driver,data["username"],data["password"],data["register"])
        assert self.driver.title == "Memberships"
        f.close()
        
    def tearDown(self):
        self.driver.quit()

class TestV3Membership(TestBookNowBase):

    @allure.description("To select desirted site")
    def test_01_select_site(self):
        By_xpath= self.driver.find_element_by_xpath
        try:
            By_xpath(homepageselectors.select_site_btn).click()
            time.sleep(2)
            By_xpath(homepageselectors.site_xpath).click()
            time.sleep(5)
            site=By_xpath(homepageselectors.step1_heading).text
            assert site== "Activity Centre"
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_screen', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To select desirted membership")
    def test_02_onetime_membership_with_login(self):
        By_xpath= self.driver.find_element_by_xpath
        firstname= names.get_first_name()
        lastname= names.get_last_name()
        # customer_name='{0} {1}'.format(customerfirstname, customerlastname)
        dob="13/09/2000"
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 
            By_xpath(homepageselectors.select_site_btn).click()
            time.sleep(2)
            find_element_by_text(self.driver,data["site"]).click()
            # By_xpath(homepageselectors.site_xpath).click()
            time.sleep(5)
            site=By_xpath(homepageselectors.step1_heading).text
            assert site== "Activity Centre"
            if data["memebership_type"]== "One Time Membership":
                By_xpath(homepageselectors.membership_btn1).click()
            else:
                By_xpath(homepageselectors.membership_btn2).click()
            find_element_by_text(self.driver,"- £50.00").click()
            time.sleep(5)
            members_value=By_xpath(homepageselectors.step2_heading).text
            assert "- £50.00" in members_value
            # By_xpath(homepageselectors.payment_btn).click()
            # find_element_by_text(self.driver,"Annually").click()
            # time.sleep(5)
            membership_type=By_xpath(homepageselectors.step3_heading).text
            assert membership_type=="One Time"
            login(self.driver, data["username"], data["password"])
            # participant_detail(self.driver, firstname, lastname, dob)
            # find_element_by_text(self.driver,"Agree to T&Cs").click()
            # time.sleep(2)
            # find_element_by_text(self.driver, "Accept Terms").click()
            # time.sleep(2)
            # card_payment(self.driver, data["cardholdername"], data["cardnumber"], data["expirymonth"], data["year"], data["cvc"])
            # membership_verification(self.driver, customername,data["memebership_type"])
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_screen', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To select desirted membership")
    def test_03_onetime_membership_with_new_account(self):
        By_xpath= self.driver.find_element_by_xpath
        firstname= names.get_first_name()
        lastname= names.get_last_name()
        customer_name= "{0} {1}".format(firstname,lastname)
        email='{0}.{1}@booknow.com'.format(firstname,lastname)
        phone="6785432567"
        password= "{0}@1234".format(firstname)
        dob="12/12/2000"
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 
            By_xpath(homepageselectors.select_site_btn).click()
            time.sleep(2)
            find_element_by_text(self.driver,data["site"]).click()
            # By_xpath(homepageselectors.site_xpath).click()
            time.sleep(5)
            site=By_xpath(homepageselectors.step1_heading).text
            assert site==data["site"]
            if data["memebership_type"]== "One Time Membership":
                By_xpath(homepageselectors.membership_btn1).click()
            else:
                By_xpath(homepageselectors.membership_btn2).click()
            find_element_by_text(self.driver,"- £50.00").click()
            time.sleep(5)
            members_value=By_xpath(homepageselectors.step2_heading).text
            assert "- £50.00" in members_value
            # By_xpath(homepageselectors.payment_btn).click()
            # find_element_by_text(self.driver,"Annually").click()
            # time.sleep(5)
            membership_type=By_xpath(homepageselectors.step3_heading).text
            assert membership_type=="One Time"
            signup(self.driver, firstname,lastname, email, phone,password)
            participant_detail(self.driver, firstname, lastname, dob)
            find_element_by_text(self.driver,"Agree to T&Cs").click()
            time.sleep(2)
            find_element_by_text(self.driver, "Accept Terms").click()
            time.sleep(2)
            card_payment(self.driver, data["cardholdername"], data["cardnumber"], data["expirymonth"], data["year"], data["cvc"])
            time.sleep(2)
            membership_verification(self.driver, customer_name,data["memebership_type"])
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_screen', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To select desirted membership")
    def test_05_membership_with_multiple_participants(self):
        By_xpath= self.driver.find_element_by_xpath
        firstname= names.get_first_name()
        lastname= names.get_last_name()
        customer_name= "{0} {1}".format(firstname,lastname)
        email='{0}.{1}@booknow.com'.format(firstname,lastname)
        phone="6785432567"
        password= "{0}@1234".format(firstname)
        dob="12/12/2000"
        member_detail={}
        member_detail["member_name"]=customer_name
        
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 
            By_xpath(homepageselectors.select_site_btn).click()
            time.sleep(2)
            find_element_by_text(self.driver,data["site"]).click()
            # By_xpath(homepageselectors.site_xpath).click()
            time.sleep(5)
            site=By_xpath(homepageselectors.step1_heading).text
            assert site==data["site"]
            if data["memebership_type"]== "One Time Membership":
                By_xpath(homepageselectors.membership_btn1).click()
            else:
                By_xpath(homepageselectors.membership_btn2).click()
            if data["no_of_participants"]=="2":
                find_element_by_text(self.driver,"- £100.00").click()
            elif data["no_of_participants"]=="3":
                find_element_by_text(self.driver,"- £150.00").click()
            else:
                find_element_by_text(self.driver,"- £200.00").click()
            time.sleep(5)
            members_value=By_xpath(homepageselectors.step2_heading).text
            assert data["no_of_participants"] in members_value
            # By_xpath(homepageselectors.payment_btn).click()
            # find_element_by_text(self.driver,"Annually").click()
            # time.sleep(5)
            membership_type=By_xpath(homepageselectors.step3_heading).text
            assert membership_type=="One Time"
            signup(self.driver, firstname,lastname, email, phone,password)
            multiple_participants(self.driver, firstname, lastname, dob)
            find_element_by_text(self.driver,"Agree to T&Cs").click()
            time.sleep(2)
            find_element_by_text(self.driver, "Accept Terms").click()
            time.sleep(2)
            card_payment(self.driver, data["cardholdername"], data["cardnumber"], data["expirymonth"], data["year"], data["cvc"])
            membership_verification(self.driver, customer_name,data["memebership_type"])
            jsondata=json.dumps(member_detail,ensure_ascii=False, indent=4)
            print(jsondata)
            with open('member_data.json', 'w') as outfile:
                json.dump(member_detail, outfile)
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_screen', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("To select desirted membership")
    def test_04_select_monthly_membership(self):
        By_xpath= self.driver.find_element_by_xpath
        firstname= names.get_first_name()
        lastname= names.get_last_name()
        # customer_name='{0} {1}'.format(customerfirstname, customerlastname)
        dob="13/09/2000"
        try:
            f = open('data2.json',"r") 
            data = json.loads(f.read()) 
            By_xpath(homepageselectors.select_site_btn).click()
            time.sleep(2)
            find_element_by_text(self.driver,data["site"]).click()
            # By_xpath(homepageselectors.site_xpath).click()
            time.sleep(5)
            site=By_xpath(homepageselectors.step1_heading).text
            assert site== "Activity Centre"
            By_xpath(homepageselectors.membership_btn2).click()
            try:
                find_element_by_text(self.driver," - £50.00").click()
            except:
                By_xpath(homepageselectors.fiftymem).click()
            time.sleep(5)
            members_value=By_xpath(homepageselectors.step2_heading).text
            # assert "£600.00 (Annually)" in members_value
            By_xpath(homepageselectors.payment_btn).click()
            find_element_by_text(self.driver,"Annually").click()
            time.sleep(5)
            membership_type=By_xpath(homepageselectors.step3_heading).text
            assert membership_type=="Annually"
            # login(self.driver, data["username"], data["password"])
            # participant_detail(self.driver, firstname, lastname, dob)
            # find_element_by_text(self.driver,"Agree to T&Cs").click()
            # time.sleep(2)
            # find_element_by_text(self.driver, "Accept Terms").click()
            # time.sleep(2)
            # card_payment(self.driver, data["cardholdername"], data["cardnumber"], data["expirymonth"], data["year"], data["cvc"])
            # print("ok")
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exception_screen', attachment_type = AttachmentType.PNG)
            raise ex

    

if __name__ == '__main__':
        unittest.main()