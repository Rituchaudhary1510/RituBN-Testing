import allure,pytest, time, unittest, names, json, warnings
from random import randint
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selfservice_selectors import commonpath, homepageselector,confirmationpageselectors
from selenium.webdriver.support.ui import Select
from selfservice_methods import changemethod, plusquantity,minusquantity,productprice,add_to_cart, quantity_selection,time_selection, payment_mode, share_payment,datepicker, login,loginhere,siteselection,checkout_as_guest,create_account,find_element_by_text
from selfservice_methods import promocode,delete_cart_item, invalidgiftcard, verification, card_payment, add_ons,checkout, execute_click_by_text

class TestBookNowBase(unittest.TestCase):
    @allure.step("First Step to open the browser with title: {0}".format("Home"))
    def setUp(self):
        self.driver= webdriver.Chrome(commonpath.path)
        f = open('selfservice_data.json',"r") 
        data = json.loads(f.read()) 
        self.driver.get(data["url_kitchen"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        f.close()

    @allure.step("Close the browser")
    def tearDown(self):
        self.driver.quit()


@allure.severity(allure.severity_level.CRITICAL)
class TestSelfService(TestBookNowBase):

    @allure.description("Place an order with existing user login")
    def test_01_login(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath

            f = open('selfservice_data.json',"r") 
            data = json.loads(f.read()) 
            time.sleep(5)

            for kk in data["kitchenproduct"]:
                print(kk)
                if kk["productname"]=="AppleJuice" or kk["productname"]=="Coffee":
                    last_height = self.driver.execute_script("return document.body.scrollHeight")
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(5)
                else:
                    print("no change")
                plusquantity(self.driver, kk["productname"],kk["quantity"])
                minusquantity(self.driver, kk["productname"],kk["minusquantity"])
                pdctprice=productprice(self.driver,kk["productname"])
                add_to_cart(self.driver,kk["productname"])
                time.sleep(2)
            
            # promocode(self.driver, data["promocode"])
            amount= checkout(self.driver)
            login(self.driver, data["existinguser_id"], data["existinguser_password"])
            # find_element_by_text(self.driver," use this account").click()
            try:
                cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
                print(cart_item)
            except:
                print("elements not in cart")
            subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
            print(subtotal)
            payment_mode(self.driver, data["payment_via"])
            # share_payment(self.driver)
            # time.sleep(5)
            card_payment(self.driver,data["cardholdername"], data["cardnumber"],data["expirymonth"],data["expiryyear"], data["cvc"])
            verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,data["existing_customer_name"],data["table"]) 
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
            raise ex

    
    @allure.description("Place an order with guest user login with promocode")
    def test_02_guestlogin_promocode(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            firstname= names.get_first_name()
            lastname= names.get_last_name()
            customer_name= "{0} {1}".format(firstname,lastname)
            phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
            
            f = open('selfservice_data.json',"r") 
            data = json.loads(f.read()) 
            time.sleep(5)
            for kk in data["kitchenproduct2"]:
                print(kk)
                if kk["productname"]=="AppleJuice" or kk["productname"]=="Coffee":
                    last_height = self.driver.execute_script("return document.body.scrollHeight")
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(5)
                else:
                    print("no change")
                plusquantity(self.driver, kk["productname"],kk["quantity"])
                minusquantity(self.driver, kk["productname"],kk["minusquantity"])
                pdctprice=productprice(self.driver,kk["productname"])
                add_to_cart(self.driver,kk["productname"])
                time.sleep(2)
            
            promocode(self.driver, data["promocode"])

            amount= checkout(self.driver)
            # login(self.driver, data["existinguser_id"], data["existinguser_password"])
            # find_element_by_text(self.driver," use this account").click()
            try:
                cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
                print(cart_item)
            except:
                print("elements not in cart")
            subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
            print(subtotal)
           
            checkout_as_guest(self.driver,firstname,lastname,phone)
            payment_mode(self.driver, data["payment_via"])
            # share_payment(self.driver)
            # time.sleep(5)
            allure.attach(self.driver.get_screenshot_as_png(), name = 'payment__screen', attachment_type = AttachmentType.PNG)
            find_element_by_text(self.driver," Checkout").click()
            verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name,data["table"]) 
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
            raise ex   

    
    @allure.description("Place an order with new user account with invalid promocode")
    def test_03_newaccount_invalid_promocode(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            firstname= names.get_first_name()
            lastname= names.get_last_name()
            customer_name= "{0} {1}".format(firstname,lastname)
            phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
            
            f = open('selfservice_data.json',"r") 
            data = json.loads(f.read()) 
            time.sleep(5)
           
            for kk in data["kitchenproduct3"]:
                print(kk)
                if kk["productname"]=="AppleJuice" or kk["productname"]=="Coffee":
                    last_height = self.driver.execute_script("return document.body.scrollHeight")
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(5)
                else:
                    print("no change")
                plusquantity(self.driver, kk["productname"],kk["quantity"])
                minusquantity(self.driver, kk["productname"],kk["minusquantity"])
                pdctprice=productprice(self.driver,kk["productname"])
                add_to_cart(self.driver,kk["productname"])
                time.sleep(2)
            
            invalidgiftcard(self.driver, data["npromocode"])
        
            amount= checkout(self.driver)
            
            try:
                cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
                print(cart_item)
            except:
                print("elements not in cart")
            subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
            print(subtotal)
           
            create_account(self.driver,firstname,lastname,phone)
            payment_mode(self.driver, data["payment_via"])
            # share_payment(self.driver)
            # time.sleep(5)
            card_payment(self.driver,data["cardholdername"], data["cardnumber"],data["expirymonth"],data["expiryyear"], data["cvc"])
            verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,customer_name,data["table"]) 
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
            raise ex

    @allure.description("Place an order with loginhere button on homepage with promocode")
    def test_04_loginhere(self):
        try:
            By_name = self.driver.find_element_by_name
            By_ID = self.driver.find_element_by_id
            By_xpath= self.driver.find_element_by_xpath
            firstname= names.get_first_name()
            lastname= names.get_last_name()
            customer_name= "{0} {1}".format(firstname,lastname)
            phone= ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
            
            f = open('selfservice_data.json',"r") 
            data = json.loads(f.read()) 
            time.sleep(5)
            loginhere(self.driver, data["existinguser_id"], data["existinguser_password"])
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            print(last_height)
            for kk in data["kitchenproduct2"]:
                print(kk)
                if kk["productname"]=="AppleJuice" or kk["productname"]=="Coffee":
                    last_height = self.driver.execute_script("return document.body.scrollHeight")
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(5)
                else:
                    print("no change")
                plusquantity(self.driver, kk["productname"],kk["quantity"])
                minusquantity(self.driver, kk["productname"],kk["minusquantity"])
                pdctprice=productprice(self.driver,kk["productname"])
                add_to_cart(self.driver,kk["productname"])
                time.sleep(2)

            amount= checkout(self.driver)
            # find_element_by_text(self.driver,"use this account").click()
            try:
                cart_item= self.driver.find_element_by_xpath("//*[@aria-label='Cart Items']").text
                print(cart_item)
            except:
                print("elements not in cart")
            try:
                subtotal= self.driver.find_element_by_xpath("//*[contains(text(),'Sub Total')]/ancestor::tr").text
                print(subtotal)
            except:
                print(" no subtotal")
            # vat= self.driver.find_element_by_xpath("//*[contains(text(),'VAT')]/ancestor::tr").text
            card_payment(self.driver,data["cardholdername"], data["cardnumber"],data["expirymonth"],data["expiryyear"], data["cvc"])
            # verification(self.driver,data["site"],data["booking_date"],cart_item,subtotal,amount,customer_name,data["table"]) 
            verification(self.driver,data["site"],data["date"],cart_item,subtotal,amount,data["existing_customer_name"],data["table"]) 
            f.close()
        
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
            raise ex

    def test_05_delete_item_from_cart(self):
        try:
            f = open('selfservice_data.json',"r") 
            data = json.loads(f.read()) 
            time.sleep(5)
            for kk in data["kitchenproduct"]:
                print(kk)
                if kk["productname"]=="AppleJuice" or kk["productname"]=="Coffee":
                    last_height = self.driver.execute_script("return document.body.scrollHeight")
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(5)
                else:
                    print("no change")
                plusquantity(self.driver, kk["productname"],kk["quantity"])
                minusquantity(self.driver, kk["productname"],kk["minusquantity"])
                pdctprice=productprice(self.driver,kk["productname"])
                add_to_cart(self.driver,kk["productname"])
                time.sleep(2)
            time.sleep(4)
            delete_cart_item(self.driver, data["item_to_delete_2"])
            time.sleep(2)
            f.close()    
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'exceptionerror_screen', attachment_type = AttachmentType.PNG)
            raise ex


if __name__ == '__main__':
    unittest.main()

