from selector import paymentselectors, commonpath,confirmationpageselectors
from selector import bookingpageselectors, loginselectors, customersearchselectors
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time,datetime
import names, calendar
from random import randint
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType


wait=2

def find_element_by_text(driver,element_text):
    item = driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(element_text))
    return item
def find_element_by_text_input(driver,element_text):
    item = driver.find_element_by_xpath("//*[contains(text(),'{}')]/ancestor::h3[1]//ancestor::div[1]//div[@class='text-right']//input".format(element_text))
    return item
# "//*[contains(text(),'BKN-0000008049')]/ancestor::h3[1]//ancestor::div[1]//div[@class='text-right']//div")
def find_element_by_text_div(driver,element_text):
    item = driver.find_element_by_xpath("//*[contains(text(),'{}')]/ancestor::h3[1]//ancestor::div[1]//div[@class='text-right']//div".format(element_text))
    return item

def execute_click_by_text(driver, itemlist):
    for s in itemlist:
            item = find_element_by_text(driver, s)
            time.sleep(1)
            item.click()

def execute_click_by_text_on(driver, itemdict):
    time.sleep(2)
    try:
        try:
            item = find_element_by_text(driver, itemdict["producttype"])
        except:
            item = find_element_by_text(driver, itemdict["itemgroup"])
        time.sleep(2)
        item.click()
    except:
        print("no product group")
    try:
        item = find_element_by_text(driver, itemdict["productname"])
    except:
        item = find_element_by_text(driver, itemdict["itemname"]) 
    time.sleep(2)
    item.click()

def execute_click_by_text_on2(driver, itemdict):
    time.sleep(2)
    item = find_element_by_text(driver, itemdict["category"])
    time.sleep(2)
    item.click()
    item = find_element_by_text(driver, itemdict["subcategory"])
    time.sleep(2)
    item.click()

def execute_click_by_text2(driver, itemlist):
    for s in itemlist:
        for mp in s:
            time.sleep(2)
            item = find_element_by_text(driver, mp)
            time.sleep(3)
            item.click()


@allure.step('Login into the site with username:"lsim" and password:"123" ')
def login(driver,username, password, register):
    By_name = driver.find_element_by_name
    By_ID = driver.find_element_by_id
    By_class_name= driver.find_element_by_class_name
    time.sleep(2)
    By_ID(loginselectors.username).send_keys(username)
    # time.sleep(2)
    By_ID(loginselectors.password).send_keys(password)
    # time.sleep(2)
    Select(By_class_name(loginselectors.register)).select_by_visible_text(register)
    time.sleep(2)
    By_name(loginselectors.login).click()
    time.sleep(2)

@allure.step("Select the site: {1}")  
def site_selection(driver, site):
    find_element_by_text(driver, site).click()
    time.sleep(2)

def skate_product(driver):
    By_xpath= driver.find_element_by_xpath
    find_element_by_text(driver, "Ungrouped").click()
    time.sleep(2)
    By_xpath(bookingpageselectors.skate_xpath).click()
    time.sleep(2)

def birthday_product(driver):
    By_xpath= driver.find_element_by_xpath
    By_xpath(bookingpageselectors.birthday_product).click()
    time.sleep(2)
    By_xpath(bookingpageselectors.sub_product2).click()
    time.sleep(3)

def birthday_product2(driver):
    By_xpath= driver.find_element_by_xpath
    By_xpath(bookingpageselectors.birthday_product).click()
    time.sleep(2)
    By_xpath(bookingpageselectors.birhday_product2_xpath).click()
    time.sleep(3)

@allure.step("Adding a birthday product to the cart")
def birthday_submodule(driver,birthdayperson_name,quantity,food_option,birthdayage):
    By_xpath= driver.find_element_by_xpath
    By_ID = driver.find_element_by_id
    try:
        Select(By_ID(bookingpageselectors.quantity)).select_by_value(quantity)
        time.sleep(2)
        try:
            Select(By_ID(bookingpageselectors.option_id)).select_by_value(food_option)
        except:
            print("No food option is available")
        try:
            By_ID(bookingpageselectors.birthday_name).send_keys(birthdayperson_name)
            By_ID(bookingpageselectors.birthday_age).send_keys(birthdayage)
        except:
            print("no module")
        By_xpath(bookingpageselectors.add_to_sale).click()
        time.sleep(2)
    except:
        print("birthday module not available")

@allure.step("Select the date as: {1}")
def date_picker(driver,date,qty):
    By_xpath= driver.find_element_by_xpath
    By_xpath(bookingpageselectors.date_xpath).clear()
    time.sleep(2)
    By_xpath(bookingpageselectors.date_xpath).send_keys(date)
    time.sleep(1)
    try:
        Select(By_xpath(bookingpageselectors.axe_qty)).select_by_value(qty)
    except:
        Select(By_xpath(bookingpageselectors.quantity)).select_by_value(qty)
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'changed_date_screen', attachment_type = AttachmentType.PNG)
    By_xpath(bookingpageselectors.search_btn).click()
    time.sleep(2)

@allure.step("Select the time as:{1}")
def time_picker(driver,timeslot):
    By_xpath= driver.find_element_by_xpath
    try:
        allure.attach(driver.get_screenshot_as_png(), name = 'changed_time_screen', attachment_type = AttachmentType.PNG)
        execute_click_by_text(driver,[timeslot])
        time.sleep(2)        
    except:
        try:
            if By_xpath(bookingpageselectors.date_time_alert_xpath).text=="No sessions available for this day, or all sessions are fully booked.":
                allure.attach(driver.get_screenshot_as_png(), name = 'No_session_available_screen', attachment_type = AttachmentType.PNG)
                By_xpath(bookingpageselectors.date_time_close_button_xpath).click()
                print("try another product or date")
                time.sleep(2)
                driver.quit()
        except:
            print("No Time Slot available")
@allure.step("To pay the remaining balance of the booking")
def pay_balance(driver,booking_number):
    By_xpath= driver.find_element_by_xpath
    try:
        eye=By_xpath("//*[contains(text(),'{0}')]//ancestor::tr//td[1]//a[2]".format(booking_number))
        eye.click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        allure.attach(driver.get_screenshot_as_png(), name = 'info_screen_image', attachment_type = AttachmentType.PNG)
        time.sleep(1)
        balance=By_xpath(customersearchselectors.balance_amt).text
        print(balance)
        By_xpath(customersearchselectors.blue_pay_btn).click()
        time.sleep(1)
        iframe = driver.find_element_by_id(paymentselectors.iframe2)
        driver.switch_to.frame(iframe)
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'epos_screen', attachment_type = AttachmentType.PNG)
        driver.find_element_by_id(paymentselectors.pay_now).click()
        time.sleep(5)
        amount=By_xpath(confirmationpageselectors.grand_total).text
        print(str(amount))
        # assert balance == amount
        time.sleep(3)
        By_xpath(paymentselectors.cash).click()
        time.sleep(5)
        try:
            By_xpath(paymentselectors.no_receipt_xpath).click()
        except:
            By_xpath(paymentselectors.no_receipt).click()
        time.sleep(3)
        driver.switch_to.default_content()
        new_balance=By_xpath(customersearchselectors.balance_amt).text
        print(new_balance)
        assert new_balance == "EUR 0,00"
    except Exception as e:
        raise e

@allure.step("To pay the remaining balance of the booking")
def pay_balance_online(driver,booking_number,name,number,date,year,cv2):
    By_xpath= driver.find_element_by_xpath
    By_name= driver.find_element_by_name
    try:
        eye=By_xpath("//*[contains(text(),'{0}')]//ancestor::tr//td[1]//a[2]".format(booking_number))
        eye.click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        allure.attach(driver.get_screenshot_as_png(), name = 'info_screen_image', attachment_type = AttachmentType.PNG)
        time.sleep(1)
        balance=By_xpath(customersearchselectors.balance_amt).text
        print(balance)
        By_name(customersearchselectors.rem_name_on_card).send_keys(name)
        By_name(customersearchselectors.rem_card_number).send_keys(number)
        Select(By_name(customersearchselectors.rem_expiry_date)).select_by_value(date)
        Select(By_name(customersearchselectors.rem_expiry_year)).select_by_value(year)
        By_name(customersearchselectors.rem_cv2).send_keys(cv2)
        allure.attach(driver.get_screenshot_as_png(), name = 'epos_screen', attachment_type = AttachmentType.PNG)
        By_name(customersearchselectors.rem_pay_btn).click()
        time.sleep(4)
        # new_balance=By_name(customersearchselectors.balance_amt).text
        # print(new_balance)
        # assert new_balance == "EUR 0,00"
    except Exception as e:
        raise e


@allure.step("Adding {1}")
def add_to_sale(driver,a,date,timeslot):
    time.sleep(3)
    By_xpath= driver.find_element_by_xpath
    date_time_str = date
    date_time_obj = datetime.datetime.strptime(date_time_str, '%d %b %Y')
    product_date= date_time_obj.strftime('%d/%m/%Y')
    print(product_date)
    # product_price=By_xpath("//*[contains(text(),'{0}')]/ancestor::div//ancestor::div//ancestor::div[@class='flip-card-inner']//div[@class='flip-card-front']//div//div[3]/b".format(a))
    # product_price=product_price.text
    # print(product_price)
    allure.attach(driver.get_screenshot_as_png(), name = 'after_adding_to_cart_screen', attachment_type = AttachmentType.PNG)
    try:
        cart= By_xpath(bookingpageselectors.cart_table).text
    except Exception as ex:
        raise ex
    assert a in cart
    assert timeslot in cart
    # return product_price

@allure.step("To pay the remaining balance of the booking")
def pay_balance(driver,booking_number):
    By_xpath= driver.find_element_by_xpath
    try:
        eye=By_xpath("//*[contains(text(),'{0}')]//ancestor::tr//td[1]//a[2]".format(booking_number))
        eye.click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        allure.attach(driver.get_screenshot_as_png(), name = 'info_screen_image', attachment_type = AttachmentType.PNG)
        time.sleep(1)
        balance=By_xpath(customersearchselectors.balance_amt).text
        print(balance)
        By_xpath(customersearchselectors.blue_pay_btn).click()
        time.sleep(1)
        iframe = driver.find_element_by_id(paymentselectors.iframe2)
        driver.switch_to.frame(iframe)
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'epos_screen', attachment_type = AttachmentType.PNG)
        driver.find_element_by_id(paymentselectors.pay_now).click()
        time.sleep(5)
        amount=By_xpath(confirmationpageselectors.grand_total).text
        print(str(amount))
        # assert balance == amount
        time.sleep(3)
        By_xpath(paymentselectors.cash).click()
        time.sleep(5)
        try:
            By_xpath(paymentselectors.no_receipt_xpath).click()
        except:
            By_xpath(paymentselectors.no_receipt).click()
        time.sleep(3)
        driver.switch_to.default_content()
        new_balance=By_xpath(customersearchselectors.balance_amt).text
        print(new_balance)
        assert new_balance == "GBP 0.00"
    except Exception as e:
        raise e


@allure.step("Adding {1}")
def date_and_time_verification(driver,a,date,timeslot):
    time.sleep(3)
    By_xpath= driver.find_element_by_xpath
    date_time_str = date
    date_time_obj = datetime.datetime.strptime(date_time_str, '%d %b %Y')
    product_date= date_time_obj.strftime('%d/%m/%Y')
    print(product_date)         
    try:
        cart= By_xpath(bookingpageselectors.cart_table).text
    except Exception as ex:
        raise ex     
    date_in_cart= By_xpath("//*[contains(text(),'{0}')]//ancestor::div//ancestor::div[@class='row']//ancestor::div[@class='flip-card-front']//div[1]//div[2]//span".format(a))
    date_in_cart= date_in_cart.text
    print(date_in_cart)
    allure.attach(driver.get_screenshot_as_png(), name = 'date_verification_in_cart_screen', attachment_type = AttachmentType.PNG)
    assert date_in_cart == product_date
    assert a in cart
    assert timeslot in cart
    
@allure.step("Adding {1} {2} as additional item")
def additionalitem_add_to_sale(driver,quantity,item):
    By_xpath= driver.find_element_by_xpath
    By_ID = driver.find_element_by_id
    try:
        Select(By_ID(bookingpageselectors.additional_quatity)).select_by_value(quantity)
        time.sleep(2)
        By_xpath(bookingpageselectors.add_to_sale2).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'after_adding_to_cart_screen', attachment_type = AttachmentType.PNG)
        driver.execute_script("window.scroll(0, 0)")
        time.sleep(2)
        cart= By_xpath(bookingpageselectors.cart_table).text
        assert item in cart
    except Exception as e:
        raise e

@allure.step("payment through card")   
def card_payment(driver,number,name,expiry,code): 
    By_xpath= driver.find_element_by_xpath
    By_name = driver.find_element_by_name
    By_xpath(paymentselectors.online).click()
    time.sleep(2)
    try:
        By_xpath(paymentselectors.pay_button).click()
        time.sleep(5)
        print("test done")
    except:
        Select(By_xpath(paymentselectors.select_method_name)).select_by_value("full")
        time.sleep(1)
        amount= str(By_xpath(paymentselectors.amount_to_pay).text)
        print(amount)
        By_name(paymentselectors.card_number).send_keys(number)
        By_name(paymentselectors.name_on_card).send_keys(name)
        By_xpath(paymentselectors.month_year).send_keys(expiry)
        By_name(paymentselectors.security_code).send_keys(code) 
        allure.attach(driver.get_screenshot_as_png(), name = 'card_payment_screen', attachment_type = AttachmentType.PNG)
        By_xpath(paymentselectors.pay).click()
        time.sleep(2)
        return amount

@allure.step("Remove selected product from the cart")
def remove_from_cart(driver):
    try:
        By_xpath= driver.find_element_by_xpath
        By_ID = driver.find_element_by_id
        product= By_xpath(bookingpageselectors.productname_in_cart).text
        print(product)
        div_element = WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li/div/div[2]/div')))
        hover = ActionChains(driver).move_to_element(div_element)   
        print(hover)
        hover.perform()

        button = WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li/div/div[2]/div/div[1]/span[2]")))
        hover = ActionChains(driver).move_to_element(button)
        hover.perform()

        button.click()
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name = 'after_removale_cart_screen', attachment_type = AttachmentType.PNG)
    except Exception as ex:
        raise ex
    try:
        cart= By_xpath(bookingpageselectors.cart_table).text
        print(cart)
    except Exception as ex:
        raise ex
    assert product not in cart
    

@allure.step("Making payment through epos")
def epos_payment(driver):
    By_xpath= driver.find_element_by_xpath
    By_ID = driver.find_element_by_id
    driver.execute_script("window.scroll(0, 0)")
    time.sleep(2)
    By_xpath(paymentselectors.epos).click()
    time.sleep(5)
    iframe = By_ID(paymentselectors.iframe)
    driver.switch_to.frame(iframe)
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'epos_screen', attachment_type = AttachmentType.PNG)
    By_ID(paymentselectors.pay_now).click()
    time.sleep(2)
    amount=By_xpath(confirmationpageselectors.grand_total).text
    print(str(amount))
    time.sleep(1)
    By_xpath(paymentselectors.cash).click()
    time.sleep(2)
    try:
        By_xpath(paymentselectors.no_receipt_xpath).click()
    except:
        # By_xpath(paymentselectors.no_receipt).click()
        print("skip receipt")
    time.sleep(3)
    driver.switch_to.default_content()
    return amount

@allure.step("Payment through skip payment")
def skip_payment(driver):
    By_xpath= driver.find_element_by_xpath
    time.sleep(2)
    By_xpath(paymentselectors.skip_payment).click()
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'skip_payment_screen', attachment_type = AttachmentType.PNG)
    By_xpath(paymentselectors.submit).click()
    time.sleep(2)

@allure.step("Payment through send_payment_link")
def send_payment_link(driver):
    By_xpath= driver.find_element_by_xpath
    By_xpath(paymentselectors.send_payment_link_xpath).click()
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'send_payment_link_screen', attachment_type = AttachmentType.PNG)
    By_xpath(paymentselectors.confirm_button_xpath).click()
    time.sleep(3)

@allure.step("Search for Existing Customer:Ritu")
def existing_customer(driver,user):
    By_xpath= driver.find_element_by_xpath
    By_ID = driver.find_element_by_id
    By_ID(bookingpageselectors.search_bar).send_keys(user)
    By_xpath(bookingpageselectors.search_button).click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name = 'customer_detail_screen', attachment_type = AttachmentType.PNG)
    try:
        By_xpath(bookingpageselectors.customer1_detail).click()
    except:
        print("single account")
    customer_name=By_xpath(bookingpageselectors.customer_name).text
    print(customer_name)
    time.sleep(2)
    if customer_name is not None:
        assert True
    return customer_name

@allure.step("Adding New Customer Account details as: First Name: {1} Last Name:{2} Email: {1}.{2}@gmail.com Phone Number:{3}")
def adding_newcustomer(driver,firstname,lastname,phone):
    try:
        By_xpath= driver.find_element_by_xpath
        # By_ID = driver.find_element_by_id
        By_xpath(bookingpageselectors.new_xpath).click()
        By_xpath(bookingpageselectors.first_name_xpath).send_keys(firstname)
        By_xpath(bookingpageselectors.last_name_xpath).send_keys(lastname)
        By_xpath(bookingpageselectors.email_xpath).send_keys("{0}.{1}@BookNowTests.com".format(firstname, lastname))
        By_xpath(bookingpageselectors.account_phone_xpath).send_keys(phone)
        # By_ID(bookingpageselectors.dob_xpath).send_keys("2000-10-10")
        allure.attach(driver.get_screenshot_as_png(), name = 'new_customer_details_screen', attachment_type = AttachmentType.PNG)
        By_xpath(bookingpageselectors.save_xpath).click()
        time.sleep(2)
        alert=By_xpath(customersearchselectors.success_alert).text
        print(alert)
        assert alert =="Created new account successfully"
        time.sleep(2)  
    except Exception as ex:
        raise ex 

def checkout(driver):
    driver.find_element_by_xpath(bookingpageselectors.checkout_button).click()
    allure.attach(driver.get_screenshot_as_png(), name = 'checkout_screen', attachment_type = AttachmentType.PNG)
    
@allure.step("Add a promocode: {1}")
def promocode(driver, promocode):
    By_xpath= driver.find_element_by_xpath
    By_xpath(bookingpageselectors.giftvoucher_text_xpath).send_keys(promocode)
    By_xpath(bookingpageselectors.giftvoucher_add_btn).click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name = 'promotionalcode_screen', attachment_type = AttachmentType.PNG)
    success_msg= driver.find_element_by_id(bookingpageselectors.promocode_success)
    if success_msg is not None:
        assert True
    new_price= By_xpath(bookingpageselectors.new_price).text
    print(new_price)
    assert new_price=="0.00"

@allure.step("Add a promocode: {1}")
def invalid_promocode(driver, promocode):
    By_xpath= driver.find_element_by_xpath
    By_xpath(bookingpageselectors.giftvoucher_text_xpath).send_keys(promocode)
    By_xpath(bookingpageselectors.giftvoucher_add_btn).click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name = 'promotionalcode_screen', attachment_type = AttachmentType.PNG)
    success_msg= driver.find_element_by_id(bookingpageselectors.promocode_success)
    if success_msg is not None:
        assert True
    if success_msg.text == "Sorry, that promotional code is not valid.":
        assert True
    new_price= By_xpath(bookingpageselectors.new_price).text
    print(new_price)
    assert new_price !="0.00"

@allure.step("Add a gift voucher: {1}")
def giftvoucher(driver, giftcard):
    By_xpath= driver.find_element_by_xpath
    By_xpath(bookingpageselectors.giftvoucher_text_xpath).send_keys(giftcard)
    By_xpath(bookingpageselectors.giftvoucher_add_btn).click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name = 'giftvoucher_screen', attachment_type = AttachmentType.PNG)
    success_msg= driver.find_element_by_id(bookingpageselectors.promocode_success)
    if success_msg is not None:
        assert True
    
@allure.step("Provide a discount of {1} %")
def discount(driver,percentage):
    By_xpath= driver.find_element_by_xpath
    By_xpath(bookingpageselectors.product_in_cart_xpath).click()
    By_xpath(bookingpageselectors.discount_xpath).clear()
    By_xpath(bookingpageselectors.discount_xpath).send_keys(percentage)
    By_xpath(bookingpageselectors.discount_save_button_xpath).click()
    time.sleep(3)

@allure.step("Verify the test")
def assertion(driver,site,firstname,lastname,product,item,quantity,amount):
    try:
        element = driver.find_element_by_xpath(paymentselectors.element_xpath).text
        assert element == 'Booking Confirmed'
        print("Test ran succesfully")
        table= driver.find_element_by_xpath(confirmationpageselectors.confirmation_table).text
        customer_name = "{0} {1}".format(firstname, lastname)
        if site in table:
            print(site)
        if customer_name in table:
            print(customer_name)
        if "Booked" in table:
            print("Booked")
        if product in table:
            print(product)
        if item in table:
            print(item)
        if quantity in table:
            print(quantity)
        allure.attach(driver.get_screenshot_as_png(), name = 'test_bookingconfirm_screen', attachment_type = AttachmentType.PNG)
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(), name = 'test_bookingconfirm_screen', attachment_type = AttachmentType.PNG)
        print("ASSERTION ERROR")
        time.sleep(2) 
        raise ex

@allure.step("Verify the details as:")
def details_verfication(driver,site,customer_name,product,item,quantity,timeslot,item_qty,amount,product_price):
        try:
            element = driver.find_element_by_xpath(paymentselectors.element_xpath).text
            assert element == 'Booking Confirmed'
            print("Test ran succesfully")
            table= driver.find_element_by_xpath(confirmationpageselectors.confirmation_table).text
            if site in table:
                print(site)
            if customer_name in table:
                print(customer_name)
            if "Booked" in table:
                print("Booked")
            if product in table:
                print(product)
            if item in table:
                print(item)
            if quantity in table:
                print(quantity)
            if item_qty in table:
                print(item_qty)
                allure.attach(driver.get_screenshot_as_png(), name = 'test_success_screen', attachment_type = AttachmentType.PNG)
            else:
                assert False
                allure.attach(driver.get_screenshot_as_png(), name = 'test_exception_screen', attachment_type = AttachmentType.PNG)
        except Exception as ex:
            print(ex)
            raise ex