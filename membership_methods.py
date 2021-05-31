from selector import commonpath
from methods import find_element_by_text
from selenium.webdriver.common.keys import Keys
from membership_selectors import homepageselectors,bookingpageselectors2, loginselectors, paymentselector,successpageselectors
from selector import commonpath, confirmationpageselectors, customersearchselectors
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time,datetime
import names
from random import randint
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import allure, pytest
from allure_commons.types import AttachmentType

@allure.step(" to login with existing customer account")
def login(driver, username, password):
    By_xpath= driver.find_element_by_xpath
    By_xpath(loginselectors.login_email).send_keys(username)
    By_xpath(loginselectors.login_password).send_keys(password)
    By_xpath(loginselectors.login_btn).click()
    # login_heading= By_xpath(loginselectors.login_heading).text
    allure.attach(driver.get_screenshot_as_png(), name = 'login_screen', attachment_type = AttachmentType.PNG)
    # assert login_heading == "Logged in as Luke Sims"
    By_xpath(loginselectors.continue_btn).click()
    time.sleep(3)

@allure.step("To enter participant details")
def participant_detail(driver, firstname, lastname, dob):
    By_xpath= driver.find_element_by_xpath
    By_xpath(loginselectors.participant_firstname).send_keys(firstname)
    By_xpath(loginselectors.participant_lasttname).send_keys(lastname)
    By_xpath(loginselectors.participant_dob).send_keys(dob)
    allure.attach(driver.get_screenshot_as_png(), name = 'participant_screen', attachment_type = AttachmentType.PNG)
    By_xpath(loginselectors.continu2_btn).click()
    try:
        minimum_age_error= By_xpath(loginselectors.participant_error_message).text
        print("min age error")
    except:
        summary=By_xpath(loginselectors.summary_heading).text
        assert summary =="Summary"

@allure.step("To add multiple participants")
def multiple_participants(driver, firstname, lastname, dob):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(loginselectors.p1_firstname).send_keys(firstname)
        By_xpath(loginselectors.p1_lastname).send_keys(lastname)
        By_xpath(loginselectors.p1_dob).send_keys(dob)
        firstname2= names.get_first_name()
        lastname2= names.get_last_name()
        try:
            By_xpath(loginselectors.p2_firstname).send_keys(firstname2)
            By_xpath(loginselectors.p2_lastname).send_keys(lastname2)
            By_xpath(loginselectors.p2_dob).send_keys("09121993")
            firstname3= names.get_first_name()
            lastname3= names.get_last_name()
            try:
                By_xpath(loginselectors.p3_firstname).send_keys(firstname3)
                By_xpath(loginselectors.p3_lastname).send_keys(lastname3)
                By_xpath(loginselectors.p3_dob).send_keys("15101991")
                firstname4= names.get_first_name()
                lastname4= names.get_last_name()
                try:    
                    By_xpath(loginselectors.p4_firstname).send_keys(firstname4)
                    By_xpath(loginselectors.p4_lastname).send_keys(lastname4)
                    By_xpath(loginselectors.p4_dob).send_keys("14091986")
                except:
                    print("only 3 participants")
            except:
                print("only 2 participants")
        except:
            print("only 1 participants")
        allure.attach(driver.get_screenshot_as_png(), name = 'participant_screen', attachment_type = AttachmentType.PNG)
        By_xpath(loginselectors.continu2_btn).click()
    except Exception as ex:
        raise ex
    try:
        minimum_age_error= By_xpath(loginselectors.participant_error_message).text
        print("min age error")
    except:
        summary=By_xpath(loginselectors.summary_heading).text
        assert summary =="Summary"


@allure.step("to make payment")
def card_payment(driver, name, number, month, year,cv2):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(paymentselector.cardholder).send_keys(name)
        By_xpath(paymentselector.cardnumber).send_keys(number)
        Select(By_xpath(paymentselector.expirymonth)).select_by_value(month)
        Select(By_xpath(paymentselector.expiryyear)).select_by_value(year)
        By_xpath(paymentselector.cv2).send_keys(cv2)
        allure.attach(driver.get_screenshot_as_png(), name = 'payment_screen', attachment_type = AttachmentType.PNG)
        By_xpath(paymentselector.pay_btn).click()
        time.sleep(9)
    except Exception as ex:
        raise ex

@allure.step("to create new account")
def signup(driver, firstname, lastname, email,phone,password):
    By_xpath= driver.find_element_by_xpath
    find_element_by_text(driver,"Create Account").click()
    time.sleep(3)
    By_xpath(loginselectors.signup_firstname).send_keys(firstname)
    By_xpath(loginselectors.signup_lastname).send_keys(lastname)
    By_xpath(loginselectors.signup_email).send_keys(email)
    By_xpath(loginselectors.signup_dob).send_keys("12122000")
    By_xpath(loginselectors.signup_phone).send_keys(phone)
    By_xpath(loginselectors.signup_password).send_keys(password)
    By_xpath(loginselectors.street).send_keys("67")
    By_xpath(loginselectors.town).send_keys("XYZ")
    By_xpath(loginselectors.city).send_keys("England")
    By_xpath(loginselectors.postcode).send_keys("123456")
    time.sleep(4)
    allure.attach(driver.get_screenshot_as_png(), name = 'signup_screen', attachment_type = AttachmentType.PNG)
    # find_element_by_text(driver, "Create my account").click()
    By_xpath(loginselectors.create_acc_btn).click()
    time.sleep(5)
    By_xpath(loginselectors.continue_btn).click()

@allure.description("To verify membership details")
def membership_verification(driver,name,mem_type):
    By_xpath= driver.find_element_by_xpath
    try:
        success= By_xpath(successpageselectors.success_heading).text 
        assert success =="Success"
        membership=By_xpath(successpageselectors.mem_type).text
        assert membership==mem_type
        member_name= By_xpath(successpageselectors. member_name).text
        assert member_name == name
        allure.attach(driver.get_screenshot_as_png(), name = 'success_screen', attachment_type = AttachmentType.PNG)
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(), name = 'failure_screen', attachment_type = AttachmentType.PNG)
        raise ex

@allure.step("To select member")
def select_member(driver,customer):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(customersearchselectors.search_field_xpath).send_keys(customer)
        By_xpath(customersearchselectors.search_field_xpath).send_keys(Keys.ENTER)
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name = 'memeber_detail_screen', attachment_type = AttachmentType.PNG)                        
        By_xpath(customersearchselectors.new_booking_btn).click()
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name = 'booking_screen', attachment_type = AttachmentType.PNG)                        
    except Exception as e:
        raise e
