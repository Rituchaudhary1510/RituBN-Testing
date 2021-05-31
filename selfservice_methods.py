from selfservice_selectors import filterselectors,productpageselectors,homepageselector,bookingselectors,loginselectors, paymentselectors,commonpath,confirmationpageselectors
import names
import time
import calendar
from random import randint
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType

def find_timeslot(driver,product_name):
    timeslot= driver.find_element_by_xpath("//*[contains(text(),'{}')]//ancestor::div//ancestor::div//ancestor::div//ancestor::div//div//div[2][@id='openProduct-01t1v00000Eyt7CAAR']//div[@class='row row-cols-3']//div[5]//div//p//lightning-formatted-date-time".format(product_name))
    return timeslot

def find_element_by_text(driver,element_text):
    item = driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(element_text))
    return item

def execute_click_by_text(driver, itemdict):
            # item = find_element_by_text(driver, itemdict["productgroup"])
            # time.sleep(2)
            # item.click()
            # time.sleep(2)
            # driver.execute_script("return document.body.scrollHeight")
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            item = find_element_by_text(driver, itemdict["productname"])
            time.sleep(1)
            item.click()
            time.sleep(1)

@allure.step("Selecting the date:{1}")  
def datepicker(driver,date):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(productpageselectors.date_xpath).clear()
    except:
        try:
            By_xpath(productpageselectors.date_xpath3).clear()
        except:
            By_xpath(productpageselectors.date2_xpath).clear()
    time.sleep(1)
    try:
        By_xpath(productpageselectors.date_xpath).send_keys(date)
    except:
        try:
            By_xpath(productpageselectors.date_xpath3).send_keys(date)
        except:
            By_xpath(productpageselectors.date2_xpath).send_keys(date)
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height/2," mid heigt")
    mid_height= (last_height/2)
    driver.execute_script("window.scrollTo(0, 464)")
    time.sleep(2)
    
@allure.step("Select average guest age as: {1}")
def guest_avg_age(driver, age):
    By_xpath= driver.find_element_by_xpath
    Select(By_xpath(productpageselectors.guest_age)).select_by_value(age)

@allure.step("Select adult and child participant quantity")
def quantity_selection(driver, adult):
        By_xpath= driver.find_element_by_xpath
        try:
            Select(By_xpath(productpageselectors.adult_selection_xpath)).select_by_value(adult)
        except:          
            try:
                Select(By_xpath(productpageselectors.adult_selection_xpath2)).select_by_value(adult)
            except:
                Select(By_xpath(productpageselectors.adult_selection2)).select_by_value(adult)
        time.sleep(1)
        try:    
            By_xpath(productpageselectors.search_button_xpath).click()
        except:
            try:
                By_xpath(productpageselectors.search_button_xpath2).click()
            except:
                By_xpath(productpageselectors.search_button_xpath3).click()
        time.sleep(1)
    
@allure.step("Select adult and child participant quantity")
def quantity_selection4(driver, adult):
    By_xpath= driver.find_element_by_xpath
    try:
        Select(By_xpath(productpageselectors.adult_selection4)).select_by_value(adult)
        time.sleep(1)
        By_xpath(productpageselectors.search_button_xpath4).click()
        time.sleep(1)
    except Exception as ex:
        raise ex
    

@allure.step("Select time={1}")
def time_selection4(driver,timeslot):
    try:
        driver.execute_script("return document.body.scrollHeight")
        # driver.execute_script("window.scrollTo(0, -100)")
        selected_timeslot=find_element_by_text(driver, timeslot)
        print(selected_timeslot.text)
        time.sleep(3)
        selected_timeslot.click()
    except Exception as ex:
        raise ex


@allure.step("Select time={1}")
def time_selection(driver,timeslot):
    try:
        last_height = driver.execute_script("return document.body.scrollHeight")
        print(last_height)
        driver.execute_script("window.scrollTo(0, -100)")
        selected_timeslot=find_element_by_text(driver, timeslot)
        print(selected_timeslot.text)
        time.sleep(3)
        selected_timeslot.click()
    except Exception as ex:
        raise ex

@allure.step("Select basic details: Date={1} No of People={2} Site={3}")
def Selectsite(driver,date,no_of_people,site):
    By_xpath= driver.find_element_by_xpath
    By_xpath(homepageselector.booking_date).clear()
    By_xpath(homepageselector.booking_date).send_keys(date)
    time.sleep(1)
    Select(By_xpath(homepageselector.no_of_bays)).select_by_value(no_of_people)
    time.sleep(1)
    Select(By_xpath(homepageselector.site_xpath)).select_by_visible_text(site)
    allure.attach(driver.get_screenshot_as_png(), name = 'selected_site_screen', attachment_type = AttachmentType.PNG)
    By_xpath(homepageselector.next_step2_xpath).click()
    time.sleep(2)
    login_label=By_xpath(loginselectors.login_label_text)
    login_label= login_label.text
    print(login_label)
    assert login_label=="LOGIN HERE"

@allure.step("Select site={1}")
def siteselection(driver,site,timeslot,no_of_people):
    By_xpath= driver.find_element_by_xpath
    By_name= driver.find_element_by_name
    time2= By_xpath(homepageselector.time_xpath)
    time2.clear()
    time2.send_keys(timeslot)
    By_xpath(homepageselector.modal_xpath).click() 
    Select(By_xpath(homepageselector.guest_xpath)).select_by_value(no_of_people)
    time.sleep(1)
    Select(By_name(homepageselector.venue_name)).select_by_visible_text(site)
    allure.attach(driver.get_screenshot_as_png(), name = 'selected_site_screen', attachment_type = AttachmentType.PNG)
    By_xpath(homepageselector.next_step_xpath).click()
    time.sleep(2)

@allure.step("Increase quantity of {1} by{2}")
def plusquantity(driver,product,qty):
    By_xpath= driver.find_element_by_xpath
    plusbtn=By_xpath("//*[contains(text(),'{0}')]//ancestor::div[@class='mdc-card my-4 demo-ui-control']//button[@title='Add Quantity']".format(product))
    qty= int(qty)
    time.sleep(2)
    while(qty>0):
        plusbtn.click()
        time.sleep(1)
        qty=qty-1

@allure.step("Decrease quantity of {1} by {2}")
def minusquantity(driver,product,qty):
    By_xpath= driver.find_element_by_xpath
    minusbtn=By_xpath("//*[contains(text(),'{0}')]//ancestor::div[@class='mdc-card my-4 demo-ui-control']//button[@title='Minus Quantity']".format(product))
    qty= int(qty)
    while(qty>0):
        print(qty)
        minusbtn.click()
        qty=qty-1
 
@allure.step("total price of item")
def productprice(driver,product):
    By_xpath= driver.find_element_by_xpath
    value=By_xpath("//*[contains(text(),'{}')]//ancestor::div[@class='mdc-card my-4 demo-ui-control']//lightning-formatted-number".format(product))
    price=value.text
    print(price)
    number=By_xpath("//*[contains(text(),'{}')]//ancestor::div[@class='mdc-card my-4 demo-ui-control']//div[@class='mdc-card__action-icons']//div[@class='mdc-chip  mdc-top-app-bar__action-item--unbounded']//span[@class='mdc-chip__text']".format(product))
    quantity= int(number.text)
    print(quantity)
    totalprice=3.40 * quantity
    print(totalprice)
    return totalprice


@allure.step("Add {1} to cart")
def add_to_cart(driver,product):
    By_xpath= driver.find_element_by_xpath
    addbtn=By_xpath("//*[contains(text(),'{0}')]//ancestor::div[@class='mdc-card my-4 demo-ui-control']//div[@class='mdc-card__action-icons']//button[@class='mdc-button mdc-button--raised']".format(product))
    addbtn.click()
    print("added to cart")
    allure.attach(driver.get_screenshot_as_png(), name = 'Add_to_cart_screen', attachment_type = AttachmentType.PNG)


@allure.step("Select product and add to the cart")
def add_ons(driver,a2,b2):
    By_xpath= driver.find_element_by_xpath
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # print(last_height)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    try:
        a=int(a2)
        print(a)
        time.sleep(2)
        while (a>0):
            By_xpath(bookingselectors.add_quantity_xpath).click()
            time.sleep(1)
            a=a-1
        allure.attach(driver.get_screenshot_as_png(), name = 'add_on_screen', attachment_type = AttachmentType.PNG)
    except:
        print("Add-ons are not available")
    try:
        Select(By_xpath(bookingselectors.select_option_xpath)).select_by_value("Option 2")
    except:
        print("no option available")
    time.sleep(1)
   

@allure.step("add to cart")
def add_product_to_cart(driver, productname):
    By_xpath=driver.find_element_by_xpath
    try:
        add_on_name=By_xpath(productpageselectors.add_on_name1).text
        print(add_on_name)   
    except:
        print("no add_on")    
    By_xpath(bookingselectors.add_to_cart_button_xpath).click()
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'add_to_cart_screen', attachment_type = AttachmentType.PNG)
    cart_table= By_xpath(confirmationpageselectors.cart_area_xpath)
    cart_table= cart_table.text  
    assert productname in cart_table
    try:
        assert add_on_name in cart_table
    except:
        print("no add_on")

@allure.step("select asset:")
def asset(driver, asset_name):
    assets=find_element_by_text(driver, asset_name)
    time.sleep(2)
    assets.click()


@allure.step("Adding Promocode:{1}")
def promocode(driver, promocode):
    try:
        By_xpath= driver.find_element_by_xpath
        last_height = driver.execute_script("return document.body.scrollHeight")
        print(last_height)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(10)
        By_xpath(productpageselectors.promocode_field).send_keys(promocode)
        time.sleep(2)
        By_xpath(productpageselectors.add_promocode_button).click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name = 'promocode/giftvoucher_screen', attachment_type = AttachmentType.PNG)
        # totalamount= By_xpath(productpageselectors.total_value).text
        total_amount= By_xpath("//*[contains(text(),'Total')]/ancestor::tr//ancestor::table//tr[3]/td[3]/lightning-formatted-number").text
        print(total_amount)
        assert total_amount== "£0.00"
    except Exception as ex:
        raise ex

@allure.step("Adding Gift Voucher:{1}")
def giftcard(driver, giftcard):
    By_xpath= driver.find_element_by_xpath
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(10)
    By_xpath(productpageselectors.promocode_field).send_keys(giftcard)
    time.sleep(2)
    By_xpath(productpageselectors.add_promocode_button).click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name = 'promocode/giftvoucher_screen', attachment_type = AttachmentType.PNG)
    # totalamount= By_xpath(productpageselectors.total_value).text
    total_amount= By_xpath("//*[contains(text(),'Total')]/ancestor::tr//ancestor::table//tr[3]/td[3]/lightning-formatted-number").text
    print(total_amount)
    assert total_amount== "£0.00"

@allure.step("Adding Gift Voucher/Promocode:")
def invalidgiftcard(driver, giftcard):
    By_xpath= driver.find_element_by_xpath
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(10)
    By_xpath(productpageselectors.promocode_field).send_keys(giftcard)
    time.sleep(2)
    By_xpath(productpageselectors.add_promocode_button).click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name = 'promocode/giftvoucher_screen', attachment_type = AttachmentType.PNG)
    # totalamount= By_xpath(productpageselectors.total_value).text
    total_amount= By_xpath("//*[contains(text(),'Total')]/ancestor::tr//ancestor::table//tr[3]/td[3]/lightning-formatted-number").text
    print(total_amount)
    assert total_amount != "£0.00"
    
@allure.step("To delete cart item")
def delete_cart_item(driver, itemname):
    By_xpath= driver.find_element_by_xpath
    try:
        driver.execute_script("window.scroll(0, 0)")
        total=By_xpath(bookingselectors.total_xpath).text
        print(total)
        crx_btn=By_xpath("//*[contains(text(),'{0}')]/ancestor::tr//ancestor::table//tr//td[1]//button".format(itemname))
        crx_btn.click()
        time.sleep(2)
        cart_table= By_xpath(confirmationpageselectors.cart_area_xpath)
        cart_table= cart_table.text 
        allure.attach(driver.get_screenshot_as_png(), name = 'Cart_after_delete_screen', attachment_type = AttachmentType.PNG) 
        newtotal=By_xpath(bookingselectors.total_xpath).text
        print(newtotal)
        assert total != newtotal
        # assert itemname not in cart_table
    except Exception as ex:
        raise ex


@allure.step("Click on 'Proceed to cart' and 'Accept Terms'")  
def checkout(driver):
    By_xpath= driver.find_element_by_xpath
    total=By_xpath(bookingselectors.total_xpath).text
    print(total)
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(4)
    By_xpath(bookingselectors.proceed_to_cart_xpath).click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name = 'Checkout_screen', attachment_type = AttachmentType.PNG)
    try:
        try:
            driver.find_element_by_text("Accept Terms").click()
        except:
            By_xpath(bookingselectors.accept_terms_button_xpath).click()
        time.sleep(2)
    except:
        print("skip")
    return total

@allure.step("On Homepage Login with username: lsim and password: 123")
def loginhere(driver,email,password):
    By_xpath= driver.find_element_by_xpath
    find_element_by_text(driver,"Login Here").click()
    time.sleep(2) 
    By_xpath(loginselectors.loginhere_email).send_keys(email)
    time.sleep(1)
    By_xpath(loginselectors.loginhere_password).send_keys(password)
    time.sleep(1)
    By_xpath(loginselectors.loginhere_button).click()
    try:
        heading=By_xpath(loginselectors.logged_in_heading).text
        print(heading)
        allure.attach(driver.get_screenshot_as_png(), name = 'login_sucess_screen', attachment_type = AttachmentType.PNG)
        assert True
    except:
        allure.attach(driver.get_screenshot_as_png(), name = 'login_failed_screen', attachment_type = AttachmentType.PNG)
        assert False
    # By_xpath(loginselectors.reset_password).click()
    # time.sleep(2)
    By_xpath(loginselectors.logged_in_as_xpath).click()
    # By_xpath(loginselectors.forgot_password).click()
    # time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(), name = 'resetpassword_screen', attachment_type = AttachmentType.PNG)
    # assert driver.title =="Reset Password"
    # print("test fail")

    time.sleep(5)

@allure.step("On Homepage Login with creating new account")
def loginhere_new_account(driver,firstname,lastname,phone):
    By_xpath= driver.find_element_by_xpath
    customer="{0} {1}".format(firstname, lastname)
    customer= customer.upper()
    print(customer)
    find_element_by_text(driver,"Login Here").click()
    time.sleep(2)
    find_element_by_text(driver,"Create Account").click()
    time.sleep(2)
    By_xpath(loginselectors.login_firstname_xpath).send_keys(firstname)
    time.sleep(1)
    By_xpath(loginselectors.login_lastname_xpath).send_keys(lastname)
    time.sleep(1)
    By_xpath(loginselectors.login_email_xpath).send_keys("{0}.{1}@Booknowtests.com".format(firstname, lastname))
    time.sleep(1)
    By_xpath(loginselectors.login_dob_xpath).send_keys("05/03/1995")
    time.sleep(1)
    By_xpath(loginselectors.login_phone_xpath).send_keys(phone)
    time.sleep(1)
    By_xpath(loginselectors.login_password_xpath).send_keys("{0}@1234".format(firstname))
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'new_account_details_screen', attachment_type = AttachmentType.PNG)
    find_element_by_text(driver,"Continue").click()
    time.sleep(5)
    driver.execute_script("window.scroll(0, 0)")
    new_customer=By_xpath(loginselectors.new_cust_name).text
    print(new_customer)
    assert customer in new_customer

@allure.step("Login with username: {1} and password:{2}")
def login(driver,email,password):
    By_xpath= driver.find_element_by_xpath
    By_xpath(loginselectors.login_email1).send_keys(email)
    time.sleep(1)
    By_xpath(loginselectors.login_password1).send_keys(password)
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'login_details_screen', attachment_type = AttachmentType.PNG)
    By_xpath(loginselectors.login_button_xpath).click()
    time.sleep(3)
    payment_label=By_xpath(loginselectors.payment_method_label).text
    print(payment_label)
    assert payment_label=="Payment Method"

@allure.step("Guest Login details: firstname={1},lastname={2},email= {1}.{2}@gmail.com, phonenumber= {3}")
def checkout_as_guest(driver,firstname,lastname,phone):
    By_xpath= driver.find_element_by_xpath
    find_element_by_text(driver,"Checkout as Guest").click()
    time.sleep(2)
    By_xpath(loginselectors.login_firstname_xpath).send_keys(firstname)
    time.sleep(1)
    By_xpath(loginselectors.login_lastname_xpath).send_keys(lastname)
    time.sleep(1)
    By_xpath(loginselectors.login_email_xpath).send_keys("{0}.{1}@Booknowtests.com".format(firstname, lastname))
    time.sleep(1)
    By_xpath(loginselectors.login_phone1_xpath).send_keys(phone)
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'login_details_screen', attachment_type = AttachmentType.PNG)
    find_element_by_text(driver,"Continue").click()
    time.sleep(2)
    # find_element_by_text(driver," Cancel").click()
    # time.sleep(2)
    payment_label=By_xpath(loginselectors.payment_method_label).text
    print(payment_label)
    assert payment_label=="Payment Method"

@allure.step("Create account with details: firstname={1},lastname={2}, email= {1}.{2}@gmail.com, phonenumber= {3}")
def create_account(driver,firstname,lastname,phone):
    By_xpath= driver.find_element_by_xpath
    find_element_by_text(driver,"Create Account").click()
    time.sleep(2)
    By_xpath(loginselectors.login_firstname_xpath).send_keys(firstname)
    time.sleep(1)
    By_xpath(loginselectors.login_lastname_xpath).send_keys(lastname)
    time.sleep(1)
    By_xpath(loginselectors.login_email_xpath).send_keys("{0}.{1}@Booknowtests.com".format(firstname, lastname))
    time.sleep(1)
    By_xpath(loginselectors.login_dob_xpath).send_keys("05/03/1995")
    time.sleep(1)
    By_xpath(loginselectors.login_phone_xpath).send_keys(phone)
    time.sleep(1)
    By_xpath(loginselectors.login_password_xpath).send_keys("{0}@1234".format(firstname))
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'new_account_details_screen', attachment_type = AttachmentType.PNG)
    find_element_by_text(driver,"Continue").click()
    time.sleep(2)
    # find_element_by_text(driver," Cancel").click()
    # time.sleep(2)
    payment_label=By_xpath(loginselectors.payment_method_label).text
    print(payment_label)
    assert payment_label=="Payment Method"
    
def payment_mode(driver,mode):
    try:
        find_element_by_text(driver,mode).click()
        time.sleep(5)
    except:
        print("direct payment")
    
def changemethod(driver,mode):
    By_xpath= driver.find_element_by_xpath
    By_xpath(paymentselectors.change_method_xpath).click()
    time.sleep(3)
    payment_mode(driver,mode)
        

@allure.step("proceed to payment")  
def share_payment(driver):
    # By_xpath= driver.find_element_by_xpath
    find_element_by_text(driver,"Add").click()
    time.sleep(3)
    driver.find_element_by_xpath(paymentselectors.share_payment_name_xpath).send_keys("Ronnie")
    driver.find_element_by_xpath(paymentselectors.share_payment_email_xpath).send_keys("ronnie@Booknowtests.com")
    allure.attach(driver.get_screenshot_as_png(), name = 'payment_mode_screen', attachment_type = AttachmentType.PNG)
    time.sleep(3)
    find_element_by_text(driver,"Close").click()
    # By_xpath(paymentselectors.change_method_xpath).click()
    # find_element_by_text(driver," Submit").click()
    # time.sleep(3)

@allure.step("Making payment through card with following account details:")
def card_payment(driver,name,cardnumber,month,year,code):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(paymentselectors.name_on_card_xpath).send_keys(name)
        By_xpath(paymentselectors.card_number_xpath).send_keys(cardnumber)
        Select(By_xpath(paymentselectors.expiry_month_xpath)).select_by_visible_text(month)
        x=By_xpath(paymentselectors.expiry_year_xpath)
        print(x)
        Select(By_xpath(paymentselectors.expiry_year_xpath)).select_by_visible_text(year)
        By_xpath(paymentselectors.security_code).send_keys(code)
        allure.attach(driver.get_screenshot_as_png(), name = 'payment_by_card_screen', attachment_type = AttachmentType.PNG)
        find_element_by_text(driver," Checkout").click()
    except Exception as ex:
        raise ex
        allure.attach(driver.get_screenshot_as_png(), name = 'payment__screen', attachment_type = AttachmentType.PNG)
        find_element_by_text(driver," Checkout").click()
        # By_xpath(paymentselectors.card_name).send_keys(name)
        # By_xpath(paymentselectors.card_number).send_keys(cardnumber)
        # Select(By_xpath(paymentselectors.expiry_month)).select_by_visible_text(month)
        # Select(By_xpath(paymentselectors.expiry_year)).select_by_visible_text(year)
        # By_xpath(paymentselectors.cvc_num).send_keys(code)
        # allure.attach(driver.get_screenshot_as_png(), name = 'payment_by_card_screen', attachment_type = AttachmentType.PNG)
        # find_element_by_text(driver,"Pay").click()
    time.sleep(2)

@allure.step("Verifying details:")
def verification(driver,site,date,cart_item,subtotal,total_amount,customer_name,number):
    By_xpath= driver.find_element_by_xpath
    try:
        heading=By_xpath(confirmationpageselectors.heading_xpath).text
        table= By_xpath(confirmationpageselectors.detail_area_xpath).text
        cart= By_xpath(confirmationpageselectors.cart_area_xpath).text
        
        assert "Transaction Completed" in heading or "TRANSACTION COMPLETED" in heading
        print("match found")
        assert cart_item in cart
        print("match found")
        assert subtotal in cart
        print("match found")
        assert total_amount in cart
        print("match found")
        assert site in table
        print(site)
        assert date in table
        print (date)
        assert total_amount in table
        print(total_amount)
        assert customer_name in table
        print(customer_name)
        
        print("Test ran succesfully")
        allure.attach(driver.get_screenshot_as_png(), name = 'test_bookingconfirm_screen', attachment_type = AttachmentType.PNG)
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(), name = 'test_bookingfailure_screen', attachment_type = AttachmentType.PNG)
        print("ASSERTION ERROR")
        time.sleep(2) 
        raise ex

@allure.step("To select product with filters")
def product_filter(driver, date, site, qty, min_p, max_p, typo):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(filterselectors.filter_lines).click()
        time.sleep(1)
        By_xpath(filterselectors.date).clear()
        By_xpath(filterselectors.date).send_keys(date)
        Select(By_xpath(filterselectors.location)).select_by_visible_text(site)
        By_xpath(filterselectors.quantity_num).send_keys(qty)
        By_xpath(filterselectors.min_price).send_keys(min_p)
        By_xpath(filterselectors.max_price).send_keys(max_p)
        Select(By_xpath(filterselectors.prod_type)).select_by_visible_text(typo)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        try:
            By_xpath(filterselectors.apply_btn).click()
            print("xpath")
        except:
            find_element_by_text(driver, "Apply").click()
        time.sleep(5)
    except Exception as e:
        raise e
