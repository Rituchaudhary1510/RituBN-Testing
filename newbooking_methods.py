from newbooking_selector import waiverpageselctors, newbookingpageselectors,loginselectors,confirmationselectors
from selenium.webdriver.support.ui import Select
import time
import allure
import pytest
import names
from v2_staff_methods import find_element_by_text,execute_click_by_text
from allure_commons.types import AttachmentType
from datetime import datetime
from datetime import timedelta

@allure.step("Select site:{1}")
def site_selection(driver,site):
            By_name= driver.find_element_by_name
            Select(By_name(newbookingpageselectors.site_name)).select_by_visible_text(site)

@allure.step("Select date:{1}")
def date_picker(driver,date):
    try:
        By_xpath= driver.find_element_by_xpath
        try:
            By_xpath(newbookingpageselectors.datepicker).click()
        except:
            By_xpath(newbookingpageselectors.date_picker2).click()
        time.sleep(3)
        day =driver.find_elements_by_xpath(newbookingpageselectors.day_container)
        for d in day:
            item = d.find_element_by_xpath(".//span[@aria-label='{}']".format(date))
            print(item.text)
            time.sleep(2)
            item.click()
            time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'selected_site_and_date_screen', attachment_type = AttachmentType.PNG)
    except Exception as ex:
        print(ex)
        raise ex

@allure.step("Home login with username: {1} and password: {2}")
def home_login(driver, username, password):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(loginselectors.login_logo).click()
        time.sleep(2)
        By_xpath(loginselectors.email1_xpath).send_keys(username)
        By_xpath(loginselectors.password1_xpath).send_keys(password)
        By_xpath(loginselectors.login_button1_xpath).click()
        time.sleep(5)
        # By_xpath(loginselectors.close_xpath).click()
        # time.sleep(5)
        print("hello")
    except Exception as ex:
        raise ex

@allure.step("reset password")
def reset_password(driver, email):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(loginselectors.login_logo).click()
        time.sleep(2)
        By_xpath(loginselectors.forget_password_link).click()
        time.sleep(4)
        # title= driver.title
        # print(title)
        # assert title =="Reset Password"
        By_xpath(loginselectors.reset_password_email).send_keys(email)
        time.sleep(2)
        By_xpath(loginselectors.reset_password_button).click()
        time.sleep(2)
        heading_msg=By_xpath(loginselectors.change_password_msg).txt
        assert heading_msg == "PASSWORD RESET!"
    except Exception as ex:
        raise ex


@allure.step("Add {1}/{2} to the cart with quantity: {3} and time:{4}")
def add_to_sale(driver,product_type,product,quantity,timeslot):
    By_ID = driver.find_element_by_id
    By_xpath= driver.find_element_by_xpath
    try:
        if product_type=="Parties" or product_type =="Birthday":
            qty=1
        else:
            qty=int(quantity)
            print(qty)
        for i in range(1,qty):
            print(i)
            By_xpath(newbookingpageselectors.quantity_plus_xpath).click() 
            time.sleep(1)  
        print(timeslot)
        Select(By_xpath(newbookingpageselectors.time_slot_xpath)).select_by_value(timeslot)
        print("time done")
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'cart_screen', attachment_type = AttachmentType.PNG)
        By_ID(newbookingpageselectors.add_to_cart_id).click()
        time.sleep(2)
        # cart=By_xpath(loginselectors.cart).text
        # assert product in cart
    except Exception as ex:
        raise ex   

@allure.step("Add {1} to the cart and time:{2}")
def add_to_sale_capacity(driver,product,timeslot):
        By_ID = driver.find_element_by_id
        By_xpath= driver.find_element_by_xpath
        i=1
        while(i<=76):
                By_xpath(newbookingpageselectors.quantity_plus_xpath).click()
                i= i+1
        # By_xpath(newbookingpageselectors.quantity_plus_xpath).click()
        # time.sleep(1)
        # By_xpath(newbookingpageselectors.quantity_plus_xpath).click()
        print(i)
        time.sleep(5)
        Select(By_xpath(newbookingpageselectors.time_slot_xpath)).select_by_value(timeslot)
        time.sleep(3)
        By_ID(newbookingpageselectors.add_to_cart_id).click()
        time.sleep(7)
        allure.attach(driver.get_screenshot_as_png(), name = 'add_to_cart_screen', attachment_type = AttachmentType.PNG)

@allure.step("Making Card payment")          
def card_payment(driver,name,number,month,year,cvc):
    By_xpath = driver.find_element_by_xpath
    By_name = driver.find_element_by_name
    amount= By_xpath(confirmationselectors.amount_xpath).text
    try:
        try:
            By_name(newbookingpageselectors.name_on_card_name).send_keys(name)
        except:
            By_xpath(newbookingpageselectors.name_on_card_xpath).send_keys(name)
        try:
            By_name(newbookingpageselectors.card_number_name).send_keys(number)
        except:
            By_xpath(newbookingpageselectors.card_number_xpath).send_keys(number)
        try:
            By_name(newbookingpageselectors.expiry_month_name).send_keys(month)
        except:
            By_xpath(newbookingpageselectors.expiry_month_xpath).send_keys(month)
        try:
            Select(By_name(newbookingpageselectors.expiry_year_name)).select_by_visible_text(year)
        except:
            Select(By_xpath(newbookingpageselectors.expiry_year_xpath)).select_by_visible_text(year)
        try:
            By_name(newbookingpageselectors.security_code_name).send_keys(cvc)
        except:
            By_xpath(newbookingpageselectors.security_code_xpath).send_keys(cvc)
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name = 'card_payment_screen', attachment_type = AttachmentType.PNG)
        try:
            By_name(newbookingpageselectors.checkout_name).click()
        except:
            By_xpath(newbookingpageselectors.checkout_xpath).click()
        time.sleep(5)
    except:
        try:
            By_name(newbookingpageselectors.checkout_name).click()
        except:
            By_xpath(newbookingpageselectors.checkout_xpath).click()
        time.sleep(20)
    return amount

@allure.step("Add Promotional code:{1}")     
def promocode(driver,promotionalcode):
    By_xpath= driver.find_element_by_xpath
    By_name = driver.find_element_by_name
    By_name(newbookingpageselectors.promotional_code_name).send_keys(promotionalcode)
    By_name(newbookingpageselectors.add_button_name).click()
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'Promotional_code_screen', attachment_type = AttachmentType.PNG)
    try:
        amount= By_xpath(confirmationselectors.amount_xpath).text
    except:
        amount= By_xpath(confirmationselectors.amount_xpath2).text
    return amount
            
@allure.step("Adding birthday person name and age")  
def birthday_module(driver,studentname,age,text):
    try:
        studentname= names.get_full_name()
        By_xpath= driver.find_element_by_xpath
        # By_name = driver.find_element_by_name
        try:
            By_xpath(newbookingpageselectors.student_plus_xpath).click()
        except:
            By_xpath(newbookingpageselectors.student_plus_xpath2).click()
        time.sleep(4)
        By_xpath(newbookingpageselectors.student_name_field_xpath).send_keys(studentname)
        time.sleep(1)
        try:
            find_element_by_text(driver,"Save").click()
        except:
            By_xpath(newbookingpageselectors.savebtn_xpath).click()
        time.sleep(4)
        Select(By_xpath(newbookingpageselectors.birthday_age_xpath)).select_by_value(age)
        By_xpath(newbookingpageselectors.dietry_requirement_xpath).send_keys(text)
        allure.attach(driver.get_screenshot_as_png(), name = 'birthdayperson_details_screen', attachment_type = AttachmentType.PNG)
        time.sleep(5)
    except:
        print("No birthday module present")

def adding_notes(driver,notes):
    driver.find_element_by_xpath(newbookingpageselectors.notes_xpath3).send_keys(notes)
    time.sleep(2)
            
@allure.step("Adding additionl items")
def additionalitems(driver):
    By_name = driver.find_element_by_name
    try:
        try:
            Select(By_name(newbookingpageselectors.additional_item1_name)).select_by_value('2')
        except:
            Select(By_name(newbookingpageselectors.additional_item1_name2)).select_by_value('2')
            time.sleep(2)
        try:
            try:
                Select(By_name(newbookingpageselectors.additional_item2_name)).select_by_value('3')
                time.sleep(2)
            except:
                Select(By_name(newbookingpageselectors.additional_item2_name2)).select_by_value('3')
                time.sleep(2)
            try:
                try:
                    Select(By_name(newbookingpageselectors.additional_item3_name)).select_by_value('2')
                    time.sleep(4)
                except:
                    Select(By_name(newbookingpageselectors.additional_item3_name2)).select_by_value('2')
                    time.sleep(4)
                try:
                    try:
                        Select(By_name(newbookingpageselectors.additional_item4_name)).select_by_value('2')
                        time.sleep(4)
                    except:
                        Select(By_name(newbookingpageselectors.additional_item4_name2)).select_by_value('2')
                        time.sleep(4)
                    try:
                        try:
                            Select(By_name(newbookingpageselectors.additional_item5_name)).select_by_value('2')
                            time.sleep(4)
                        except:
                            Select(By_name(newbookingpageselectors.additional_item5_name2)).select_by_value('2')
                            time.sleep(4)
                    except:
                        print("no 5th item found")
                        allure.attach(driver.get_screenshot_as_png(), name = 'additional_item_screen', attachment_type = AttachmentType.PNG)
                except:
                    print("no 4th item found")
                    allure.attach(driver.get_screenshot_as_png(), name = 'additional_item_screen', attachment_type = AttachmentType.PNG)
            except:
                print("no 3rd  item found")
                allure.attach(driver.get_screenshot_as_png(), name = 'additional_item_screen', attachment_type = AttachmentType.PNG)
        except:
            print("no 2nd item found")
            allure.attach(driver.get_screenshot_as_png(), name = 'additional_item_screen', attachment_type = AttachmentType.PNG)
    except:
            print("no additional item with this product")

@allure.step("Login with existing account: ")
def login_checkout(driver,username,password2):
    try:
        By_xpath= driver.find_element_by_xpath
        try:
            find_element_by_text(driver,"Create Account / Login").click()
        except:
            print("direct login")
        time.sleep(2)
        try:
            By_xpath(loginselectors.login_email_address_xpath).send_keys(username)
        except:
            By_xpath(loginselectors.login_email_address_xpath2).send_keys(username)
        try:
            By_xpath(loginselectors.login_password_xpath).send_keys(password2)
        except:
            By_xpath(loginselectors.login_password_xpath2).send_keys(password2)
        allure.attach(driver.get_screenshot_as_png(), name = 'exsisting_login_screen', attachment_type = AttachmentType.PNG)
        try:
            By_xpath(loginselectors.login_button_xpath).click()
        except:
            By_xpath(loginselectors.login_button_xpath2).click()
        time.sleep(3)
    except:
        print("skip login")

@allure.step("select dob:")
def dob(driver):
    try:
        By_xpath= driver.find_element_by_xpath
        time.sleep(5)
        # By_xpath(loginselectors.dob_xpath2).send_keys("2000-10-08")
        By_xpath(loginselectors.dob_xpath2).click()
        time.sleep(23)
        By_xpath(loginselectors.date).click()
        # day =driver.find_elements_by_xpath(newbookingpageselectors.dob_day_container)
        # print(day)
        # for d in day:
        #     item = d.find_element_by_xpath(".//span[@aria-label='October 1, 2020']")
        #     print(item.text)
        #     time.sleep(1)
        #     item.click()
        #     time.sleep(2)
        #     print("done")
        # prev=driver.find_element_by_css_selector("body > div.flatpickr-calendar.animate.arrowLeft.arrowTop.open > div.flatpickr-months > span.flatpickr-prev-month")
        # print(prev)
        # prev.click()
        # By_xpath(loginselectors.left_arrow).click()
        # By_xpath(loginselectors.left_arrow).click()
        
       
        # By_xpath(loginselectors.date).click()
        # time.sleep(2)
        # Select(By_xpath(loginselectors.month_selection)).select_by_visible_text("March")
        # time.sleep(12)
        print("date selected")
        
    except Exception as ex:
        print(ex)
        raise ex

@allure.step("Create Account")
def create_new_account(driver,firstname,lastname,phone):
        By_xpath= driver.find_element_by_xpath
        try:
            find_element_by_text(driver,"Create Account / Login").click()
            time.sleep(2)
        except:
            print("direct account")
        try:
            find_element_by_text(driver,"I dont have an account").click()
        except:
            find_element_by_text(driver,"Create New Account").click()
        time.sleep(2)
        try:
            By_xpath(loginselectors.first_name_xpath).send_keys(firstname)
            By_xpath(loginselectors.last_name_xpath).send_keys(lastname)
            By_xpath(loginselectors.dob_xpath).click()
            time.sleep(2)
            By_xpath(loginselectors.dob).click()
            By_xpath(loginselectors.email_xpath).clear()
            By_xpath(loginselectors.email_xpath).send_keys("{0}.{1}@BookNowTests.com".format(firstname,lastname))
            By_xpath(loginselectors.postcode_xpath).send_keys("1234")
            By_xpath(loginselectors.phone_xpath).send_keys(phone)
            By_xpath(loginselectors.password_xpath).clear()
            By_xpath(loginselectors.password_xpath).send_keys("{0}@1234".format(firstname))
            allure.attach(driver.get_screenshot_as_png(), name = 'newcustomer_login_screen', attachment_type = AttachmentType.PNG)
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), name = 'newcustomer_loginfailure_screen', attachment_type = AttachmentType.PNG)
            raise e
        time.sleep(2)

@allure.step("Guest User details:")
def express_checkout(driver,firstname, lastname, phonenumber):
            By_ID = driver.find_element_by_id
            find_element_by_text(driver, "Express Checkout").click()
            time.sleep(4)
            By_ID(newbookingpageselectors.firstname_id).send_keys(firstname)
            By_ID(newbookingpageselectors.lastname_id).send_keys(lastname)
            By_ID(newbookingpageselectors.email_id).send_keys("{firstname}.{lastname}@BookNowTests.com".format(firstname=firstname,lastname=lastname))
            By_ID(newbookingpageselectors.phone_id).send_keys(phonenumber)
            time.sleep(1)
            allure.attach(driver.get_screenshot_as_png(), name = 'express_checkout_screen', attachment_type = AttachmentType.PNG)

@allure.step("Assert Customer name as:{1} {2}")
def assertion(driver,firstname, lastname):
            By_xpath= driver.find_element_by_xpath
            element = By_xpath(newbookingpageselectors.customer_xpath).text
            if element == '{0} {1}'.format(firstname,lastname):
                assert True
                print("Test ran succesfully")
                allure.attach(driver.get_screenshot_as_png(), name = 'test_bookingconfirm_screen_010', attachment_type = AttachmentType.PNG)
            else:
                assert False
                allure.attach(driver.get_screenshot_as_png(), name = 'test_bookingconfirm_screen_failure010', attachment_type = AttachmentType.PNG)
                print("ASSERTION ERROR")
            time.sleep(5)

@allure.step("Check the promocode validations")
def promocode_error(driver):
        By_xpath= driver.find_element_by_xpath
        try:
            error= By_xpath(newbookingpageselectors.promocode_error_xpath2).text
        except:
            error= By_xpath(newbookingpageselectors.promocode_error_xpath3).text
        if error == "Sorry, that gift voucher has no funds remamining.":
            # allure.attach(driver.get_screenshot_as_png(), name = 'promocode_error_screen', attachment_type = AttachmentType.PNG)
            print("try other promocode or gift voucher")
            time.sleep(3)
            assert True
        elif error=="Sorry, that promotional code has expired.":
            # allure.attach(driver.get_screenshot_as_png(), name = 'promocode_error_screen', attachment_type = AttachmentType.PNG)
            print("try other promocode or gift voucher")
            time.sleep(3)
            assert True
        elif error=="Sorry, that promotional code does not apply to the selected site":
            # allure.attach(driver.get_screenshot_as_png(), name = 'promocode_error_screen', attachment_type = AttachmentType.PNG)
            print("try other promocode or gift voucher")
            time.sleep(3)
            assert True
        elif error=="Sorry, that promotional code has been used too many times.":
            # allure.attach(driver.get_screenshot_as_png(), name = 'promocode_error_screen', attachment_type = AttachmentType.PNG)
            print("try other promocode or gift voucher")
            time.sleep(3)
            assert True
        else:
            print("not valid card")
            time.sleep(3)
            assert True

def next_step2(driver):
    try:
            driver.find_element_by_xpath(newbookingpageselectors.next_step2_xpath).click()
    except:
            driver.find_element_by_xpath(newbookingpageselectors.next_step2_xpath2).click()
    time.sleep(3)
   
def next_step3(driver):
    try:
        try:
            driver.find_element_by_xpath(newbookingpageselectors.next_step3_xpath).click()
        except:
            driver.find_element_by_xpath(newbookingpageselectors.next_step3_xpath2).click()
        time.sleep(3)
    except:
        print("skip step")

def next_step4(driver):
    try:
        try:
            driver.find_element_by_xpath(newbookingpageselectors.next_step4_xpath).click()
        except:
            driver.find_element_by_xpath(newbookingpageselectors.next_step4_xpath1).click()
        time.sleep(3)
    except:
        print("try another path")
        try:
            driver.find_element_by_id(newbookingpageselectors.next_step4_id).click()
            time.sleep(3)
        except:
            try:
                driver.find_element_by_xpath(newbookingpageselectors.next_step4_xpath2).click()
            except:
                driver.find_element_by_xpath(newbookingpageselectors.next_step4_xpath21).click()
            time.sleep(5)
    try:
        driver.find_element_by_id(newbookingpageselectors.true_button_id).click()
        time.sleep(3)
    except:
        try:                            
            driver.find_element_by_xpath("/html/body/span[3]/main/span[2]/span[4]/div/div/form/span/span/div/div/div[3]/div/div/div[3]/input").click()
            time.sleep()
        except:
            print("skip true button step")

@allure.step("verify the booking details with the details entered by the customer")
def bookingconfirmation(driver,site,firstname,lastname,amount,product_table):
    By_xpath= driver.find_element_by_xpath
    try:
        table=By_xpath(confirmationselectors.table_xpath).text
        time.sleep(5)
        customer_name="{0} {1}".format(firstname,lastname)
        if customer_name in table:
            print("match found")
            assert True
        if site in table:
            print(site)
            assert True
        # if product_table in table:
        #     print(product_table)
        #     assert True
            allure.attach(driver.get_screenshot_as_png(), name = 'booking_verification_sucess_screen', attachment_type = AttachmentType.PNG)
    except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), name = 'booking_verification_failed_screen', attachment_type = AttachmentType.PNG)
            raise e

@allure.step("Billing details")
def billing(driver):
    try:
        By_xpath= driver.find_element_by_xpath
        By_xpath(newbookingpageselectors.billing_firstname_xpath).send_keys("John")
        By_xpath(newbookingpageselectors.billing_lastname_xpath).send_keys("Watson")
        By_xpath(newbookingpageselectors.billing_email_xpath).send_keys("John34@booknow.com")
        By_xpath(newbookingpageselectors.billing_line1_xpath).send_keys("Hn 456")
        By_xpath(newbookingpageselectors.billing_city_xpath).send_keys("Rajasthan")
        By_xpath(newbookingpageselectors.billing_postcode_xpath).send_keys("123456")
        By_xpath(newbookingpageselectors.proceed_btn_xpath).click()
        time.sleep(5)
        iframe= driver.find_element_by_id("cybersourceframe")
        driver.switch_to.frame(iframe)
        time.sleep(5)
        By_xpath(newbookingpageselectors.billing_radio_btn_xpath).click()
        By_xpath(newbookingpageselectors.billing_card_number).send_keys("4976000000003436")
        Select(By_xpath(newbookingpageselectors.billing_expiry_month)).select_by_value("12")
        Select(By_xpath(newbookingpageselectors.billing_expiry_year)).select_by_value("2021")
        allure.attach(driver.get_screenshot_as_png(), name = 'billing_screen', attachment_type = AttachmentType.PNG)
        By_xpath(newbookingpageselectors.billing_pay_btn).click()
        success= False 
        count= 0
        max_tries= 20
        while success == False and count<max_tries:
            try:
                driver.switch_to.parent_frame()
                success= True
                print("clicked")
            except Exception as ex:
                print(ex)
                count=count+1
        if (success== True):
            time.sleep(10)
            print("out from frame")
        else:
            print("wasn't successful after 20 tries")
        
    except Exception as ex:
        print(ex)
        raise ex

@allure.step("Filling up waiver form ")
def waiverform(driver,site,firstname,lastname, phone):
    try:
        By_xpath=driver.find_element_by_xpath
        Select(By_xpath(waiverpageselctors.selectsite)).select_by_visible_text(site)
        time.sleep(3)
        By_xpath(waiverpageselctors.accept_button_xpath).click()
        time.sleep(2)

        By_xpath(waiverpageselctors.firstname).clear()
        By_xpath(waiverpageselctors.firstname).send_keys(firstname)
        By_xpath(waiverpageselctors.lastname).clear()
        By_xpath(waiverpageselctors.lastname).send_keys(lastname)
        Select(By_xpath(waiverpageselctors.dob_date)).select_by_value("10")
        Select(By_xpath(waiverpageselctors.dob_month)).select_by_visible_text("March")
        Select(By_xpath(waiverpageselctors.dob_year)).select_by_value("1996")
        By_xpath(waiverpageselctors.phone).send_keys(phone)
        By_xpath(waiverpageselctors.email_address).send_keys('{0}.{1}@Booknowtest.com'.format(firstname, lastname))
        Select(By_xpath(waiverpageselctors.location)).select_by_value("-- Please Select --")
        try:
            Select(By_xpath(waiverpageselctors.valid_day)).select_by_value("12")
            Select(By_xpath(waiverpageselctors.valid_month)).select_by_visible_text("October")
            Select(By_xpath(waiverpageselctors.valid_year)).select_by_value("2020")
            print("24 hours waiver")
        except:
            print("12 month waiver")
        # find_element_by_text(driver, "Accept Terms").click()
        By_xpath(waiverpageselctors.accept_terms_checkbox).click()
        time.sleep(2)
        By_xpath(waiverpageselctors.canvas).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'minor_waiver_screen', attachment_type = AttachmentType.PNG)
        
        find_element_by_text(driver,"Submit Waiver(s)").click()
        time.sleep(14)
    except Exception as ex:
        print (ex)
        raise ex
    

@allure.step("Filling waiver form for minor")
def childwaiverform(driver,site,firstname,lastname, phone,minorfirstname,minorlastname):
    try:
        By_xpath=driver.find_element_by_xpath
        Select(By_xpath(waiverpageselctors.selectsite)).select_by_visible_text(site)
        time.sleep(3)
        By_xpath(waiverpageselctors.accept_button_xpath).click()
        time.sleep(2)
        By_xpath(waiverpageselctors.child_waiver_tick_xpath).click()
        time.sleep(2)
        By_xpath(waiverpageselctors.firstname).clear()
        By_xpath(waiverpageselctors.firstname).send_keys(firstname)
        By_xpath(waiverpageselctors.lastname).clear()
        By_xpath(waiverpageselctors.lastname).send_keys(lastname)
        Select(By_xpath(waiverpageselctors.dob_date)).select_by_value("10")
        Select(By_xpath(waiverpageselctors.dob_month)).select_by_visible_text("March")
        Select(By_xpath(waiverpageselctors.dob_year)).select_by_value("1996")
        By_xpath(waiverpageselctors.phone).send_keys(phone)
        By_xpath(waiverpageselctors.email_address).send_keys('{0}.{1}@Booknowtest.com'.format(firstname, lastname))
        Select(By_xpath(waiverpageselctors.location)).select_by_value("-- Please Select --")
        try:
            Select(By_xpath(waiverpageselctors.valid_day)).select_by_value("12")
            Select(By_xpath(waiverpageselctors.valid_month)).select_by_visible_text("October")
            Select(By_xpath(waiverpageselctors.valid_year)).select_by_value("2020")
            print("24 hours waiver")
        except:
            print("12 month waiver")
        By_xpath(waiverpageselctors.minor_firstname).send_keys(minorfirstname)
        By_xpath(waiverpageselctors.minor_lastname).send_keys(minorlastname)
        Select(By_xpath(waiverpageselctors.minor_dob_day)).select_by_value("12")
        Select(By_xpath(waiverpageselctors.minor_dob_month)).select_by_value("4")
        Select(By_xpath(waiverpageselctors.minor_dob_year)).select_by_value("2010")
        By_xpath(waiverpageselctors.accept_terms_checkbox).click()
        time.sleep(2)
        By_xpath(waiverpageselctors.canvas).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'minor_waiver_screen', attachment_type = AttachmentType.PNG)
        
        find_element_by_text(driver,"Submit Waiver(s)").click()
        time.sleep(14)
    except Exception as ex:
        print (ex)
        raise ex

@allure.step("It confirms the new waiver with correct name has been created")
def waiver_completion(driver, name):
    By_xpath= driver.find_element_by_xpath
    msg=By_xpath(waiverpageselctors.completion_msg).text
    waiver_msg="This waiver was signed for: {0}".format(name)
    allure.attach(driver.get_screenshot_as_png(), name = 'waiver_screen_screenshot', attachment_type = AttachmentType.PNG)
    assert msg== waiver_msg
    time.sleep(2)

@allure.step("It confirms the new waiver with correct name has been created")
def child_waiver_completion(driver, name, minorname):
    By_xpath= driver.find_element_by_xpath
    msg=By_xpath(waiverpageselctors.completion_msg).text
    waiver_msg="This waiver was signed for: {0}".format(name)
    waiver_msg2="This waiver was signed for: {0}, {1}".format(name, minorname)
    allure.attach(driver.get_screenshot_as_png(), name = 'waiver_screen_screenshot', attachment_type = AttachmentType.PNG)
    assert msg== waiver_msg or msg== waiver_msg2
    time.sleep(2)

