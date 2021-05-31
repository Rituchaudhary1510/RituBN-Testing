import time, names
import allure, pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from random import randint
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select
from v2_staff_selector import commonpath,customersearchselectors
from v2_staff_methods import find_element_by_text, find_element_by_text_input,find_element_by_text_div
from v2_checkin_selector import loginselectors,roomtableselectors, checkinpageselectors, refundpageselectors

@allure.step("Selecvt site, change date and time:")
def site_selection(driver,site):
    By_xpath = driver.find_element_by_xpath
    Select(By_xpath(checkinpageselectors.site_newxpath)).select_by_visible_text(site)
    time.sleep(2)
    # By_xpath(checkinpageselectors.date).send_keys(date)
    # time.sleep(2)
    # Select(By_name(checkinpageselectors.time_bar_name)).select_by_value(timeslot)
    # time.sleep(4)
    allure.attach(driver.get_screenshot_as_png(), name = 'checkin_screen', attachment_type = AttachmentType.PNG)

@allure.step("Select the booking number")
def select_booking(driver,customer, number):
    try:
        find_element_by_text(driver, "Booking").click()
        time.sleep(1)
        driver.find_element_by_xpath(customersearchselectors.search_field_xpath).send_keys(number)
        driver.find_element_by_xpath(customersearchselectors.search_field_xpath).send_keys(Keys.ENTER)
        time.sleep(5)
        customer_detail=driver.find_element_by_xpath(customersearchselectors.customer_detail_link).text
        print(customer_detail)
        assert customer in customer_detail
        driver.find_element_by_xpath(customersearchselectors.view_btn).click()
        time.sleep(2)
        find_element_by_text(driver, "Booking Products").click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'view_booking_screen', attachment_type = AttachmentType.PNG)
        try:
            find_element_by_text(driver, "Go").click()
        except:
            driver.find_element_by_xpath(customersearchselectors.first_go_btn).click()
        allure.attach(driver.get_screenshot_as_png(), name = 'booking_screen', attachment_type = AttachmentType.PNG)
    except Exception as e:
        raise e

@allure.step("Add Notes to the booking")
def adding_notes(driver,notes):
    time.sleep(3)
    By_xpath = driver.find_element_by_xpath
    By_xpath('//*[@id="preselectedBooking"]/td[1]/a[1]').click()
    # By_xpath('/html/body/div[2]/div/div[3]/form[2]/table/tbody/tr/td[1]/a[1]').click()
    time.sleep(5)
    try:
        By_xpath(checkinpageselectors.notes_text_xpath).clear()
        time.sleep(2)
        By_xpath(checkinpageselectors.notes_text_xpath).send_keys(notes)
        time.sleep(2)
    except:
        print("error in notes")
    allure.attach(driver.get_screenshot_as_png(), name = 'notes_image', attachment_type = AttachmentType.PNG)
    By_xpath(checkinpageselectors.save_changes_button_xpath).click()
    time.sleep(3)

@allure.step("To change the date or time of selected product")
def change_datetime(driver,date,number):
    try:
        By_xpath = driver.find_element_by_xpath
        time.sleep(3)
        booking_data_list=[]
        By_xpath('//*[@id="preselectedBooking"]/td[1]/span[3]').click()
        # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id187"]/a').click()
        time.sleep(2)
        By_xpath(checkinpageselectors.p1_xpath).click()
        time.sleep(4)
        # By_xpath(checkinpageselectors.date_xpath).clear()
        # time.sleep(2)
        By_xpath(checkinpageselectors.date_xpath).send_keys(date)
        time.sleep(10)
        print(date)
        allure.attach(driver.get_screenshot_as_png(), name = 'change_date/time_screen', attachment_type = AttachmentType.PNG)
        try:
            t1=By_xpath("/html/body/div[2]/div/span[2]/span/form/div[1]/div/div/div[2]/div/div[8]/div/center/small[1]").text
            By_xpath("/html/body/div[2]/div/span[2]/span/form/div[1]/div/div/div[2]/div/div[8]/div/center/small[1]").click()
            print(t1)
            time.sleep(2)
            
        except:
            t2=By_xpath(checkinpageselectors.change_time2).text
            By_xpath(checkinpageselectors.change_time2).click()
            print(t2)
            print("its t2")
            time.sleep(2)
            
        
        date_field= By_xpath(checkinpageselectors.date)
        date_field.send_keys(date)
        time.sleep(6)
        
        allure.attach(driver.get_screenshot_as_png(), name = 'change_date/time_checkin_screen', attachment_type = AttachmentType.PNG)
            
    except Exception as ex:
        raise ex
        # allure.attach(driver.get_screenshot_as_png(), name = 'change_date/time_checkin_screen', attachment_type = AttachmentType.PNG)
        # By_xpath(checkinpageselectors.close_date_xpath).click()
        # time.sleep(2)
        
@allure.step("checking details of booking")
def info(driver):  
            By_xpath = driver.find_element_by_xpath
            By_name = driver.find_element_by_name
            By_xpath('//*[@id="preselectedBooking"]/td[1]/a[2]').click()
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/form[2]/table/tbody/tr/td[1]/a[2]').click()
            time.sleep(5)
            allure.attach(driver.get_screenshot_as_png(), name = 'info_screen_image', attachment_type = AttachmentType.PNG)
            try:
                By_name(checkinpageselectors.name_on_card_name).send_keys("John Watson")
                time.sleep(2)
                By_name(checkinpageselectors.card_number_name).send_keys("4976000000003436")
                time.sleep(2)
                By_name(checkinpageselectors.expiry_month_name).send_keys("12")
                time.sleep(2)
                By_name(checkinpageselectors.expiry_year_name).send_keys("21")
                time.sleep(2)
                By_name(checkinpageselectors.cv2_name).send_keys("452")
                time.sleep(2)
                By_name(checkinpageselectors.pay_button_name).click()
                time.sleep(2)
                By_xpath(checkinpageselectors.close_button_xpath).click()
                time.sleep(2)
            except:
                By_xpath(checkinpageselectors.close_button_xpath).click()
                time.sleep(2)

@allure.step("To check in the customer")
def check_in(driver,waiver):
    By_xpath = driver.find_element_by_xpath
    By_xpath('//*[@id="preselectedBooking"]/td[1]/span[1]').click()
    # driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/form[2]/table/tbody/tr/td[1]/span[1]/span/span/div").click()
    # By_xpath(checkinpageselectors.check_in_button_xpath).click()
    time.sleep(2)
    iframe= By_xpath(checkinpageselectors.iframe_xpath)
    driver.switch_to.frame(iframe)
    time.sleep(3)
    try:
        waiver=By_xpath(checkinpageselectors.participant_xpath)
        if waiver is not None:
            print("Already checked in")
            By_xpath(checkinpageselectors.checkin_close_button).click()
            driver.switch_to.default_content()
            time.sleep(3)
    except:
        By_xpath(checkinpageselectors.search_bar_xpath).clear()
        By_xpath(checkinpageselectors.search_bar_xpath).send_keys(waiver)
        time.sleep(2)
        By_xpath(checkinpageselectors.search_button_xpath).click()
        time.sleep(2)
        By_xpath(checkinpageselectors.waiver_xpath).click()
        time.sleep(2)
        try:
            By_xpath(checkinpageselectors.waiver_xpath).click()
            time.sleep(2)
            try:
                By_xpath(checkinpageselectors.waiver_xpath).click()
                time.sleep(2)
                try:
                    By_xpath(checkinpageselectors.waiver_xpath).click()
                    time.sleep(2)
                    try:
                        By_xpath(checkinpageselectors.waiver_xpath).click()
                        time.sleep(2)
                        try:
                            By_xpath(checkinpageselectors.waiver_xpath).click()
                            time.sleep(2)
                        except:
                            print("no waiver found")
                    except:
                        print("no waiver found")
                except:
                    print("no waiver found")
            except:
                print("no waiver found")
        except:
            print("no waiver found")
        allure.attach(driver.get_screenshot_as_png(), name = 'checkin_screen_image', attachment_type = AttachmentType.PNG)
        By_xpath(checkinpageselectors.final_checkin_button_xpath).click()
        time.sleep(2)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except Exception:
            print("no alert")
        driver.switch_to.default_content()
        time.sleep(3)

@allure.step("Cancel the booking")
def cancel_refund(driver,checkin_date,):
    By_xpath = driver.find_element_by_xpath
    # By_xpath(checkinpageselectors.date).send_keys(checkin_date)
    time.sleep(5)
    By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
    # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
    # cancel=driver.find_element_by_class_name('glyphicon-remove-circle')
    # cancel.click()
    time.sleep(9)
    By_xpath(checkinpageselectors.cancel_booking_btn).click()
    time.sleep(2)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except Exception:
        print("no alert")
    time.sleep(4)
    allure.attach(driver.get_screenshot_as_png(), name = 'cancel_refund_screen', attachment_type = AttachmentType.PNG)
    By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name = 'after_cancel_booking_screen', attachment_type = AttachmentType.PNG)
    time.sleep(2)
   

@allure.step("Cancel the booking")
def uncancel_a_booking(driver):
    By_xpath = driver.find_element_by_xpath
    By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
    # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
    # cancel=driver.find_element_by_class_name('glyphicon-remove-circle')
    # cancel.click()
    time.sleep(9)
    By_xpath(checkinpageselectors.cancel_booking_btn).click()
    time.sleep(2)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except Exception:
        print("no alert")
    time.sleep(4)
    allure.attach(driver.get_screenshot_as_png(), name = 'cancel_refund_screen', attachment_type = AttachmentType.PNG)
    By_xpath(checkinpageselectors.cancel_booking_btn).click()
    time.sleep(2)
    By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name = 'after_uncancel_booking_screen', attachment_type = AttachmentType.PNG)
    time.sleep(2)


allure.step(" To refund the amount ")
def refund_product_via_epos(driver):
    By_xpath= driver.find_element_by_xpath
    By_ID= driver.find_element_by_id
    try:
        By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
        # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
        time.sleep(8)
        By_xpath("//*[@title= 'Remove Products']").click()
        time.sleep(2)
        stage1= By_xpath(refundpageselectors.stage1).text
        assert stage1 == "Select Products - Aktuelle Phase"
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_screen', attachment_type = AttachmentType.PNG)
        By_xpath("//*[@title= 'Refund All']").click()
        time.sleep(2)
        stage2= By_xpath(refundpageselectors.stage2).text
        assert stage2== "Refund Method - Aktuelle Phase"
        By_xpath(refundpageselectors.buy_now_option).click()
        time.sleep(2)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        iframe = By_ID(refundpageselectors.iframe)
        driver.switch_to.frame(iframe)
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name = 'epos_screen', attachment_type = AttachmentType.PNG)
        By_xpath(refundpageselectors.pay_btn).click()
        time.sleep(8)
        print("click done")
        try:
            By_xpath(refundpageselectors.cash_btn_xpath).click()
        except:
            print("cash not done")
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name = 'payment_time_screen', attachment_type = AttachmentType.PNG)
        By_xpath(refundpageselectors.no_receipt).click()
        time.sleep(3)
        driver.switch_to.default_content()
        time.sleep(5)
        payment_table= By_xpath(refundpageselectors.payments_table).text
        print(payment_table)
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_home_screen', attachment_type = AttachmentType.PNG)
        cash_refund_title=By_xpath(refundpageselectors.cash_refund_title).text
        print(cash_refund_title)
        assert cash_refund_title in payment_table
        refund_amt= By_xpath(refundpageselectors.cash_refund_amount).text
        print(refund_amt)
        assert refund_amt in payment_table
        By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
        time.sleep(2)
    except Exception as ex:
        raise ex


@allure.step(" To refund the amount ")
def refund_product_via_credit_card(driver):
    By_xpath= driver.find_element_by_xpath
    By_ID= driver.find_element_by_id
    try:
        By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
        # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
        time.sleep(8)
        By_xpath("//*[@title= 'Remove Products']").click()
        time.sleep(2)
        stage1= By_xpath(refundpageselectors.stage1).text
        assert stage1 == "Select Products - Aktuelle Phase"
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_screen', attachment_type = AttachmentType.PNG)
        By_xpath("//*[@title= 'Refund All']").click()
        time.sleep(2)
        stage2= By_xpath(refundpageselectors.stage2).text
        assert stage2== "Refund Method - Aktuelle Phase"
        By_xpath(refundpageselectors.online_option).click()
        time.sleep(2)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(2)
        try:
            alert = driver.switch_to.alert
            alert.accept()  
        except Exception:
            print("no alert")
        allure.attach(driver.get_screenshot_as_png(), name = 'creditcard_screen', attachment_type = AttachmentType.PNG)
        By_xpath(refundpageselectors.payment_xpath).click()
        time.sleep(2)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(2)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except Exception:
            print("no alert")
        time.sleep(4)
        payment_table= By_xpath(refundpageselectors.payments_table).text
        print(payment_table)
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_home_screen', attachment_type = AttachmentType.PNG)
        cash_refund_title=By_xpath(refundpageselectors.cash_refund_title).text
        print(cash_refund_title)
        assert cash_refund_title in payment_table
        refund_amt= By_xpath(refundpageselectors.cash_refund_amount).text
        print(refund_amt)
        assert refund_amt in payment_table
        By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
        time.sleep(2)
    except Exception as ex:
        raise ex


@allure.step("to check the room availability")
def room_verification(driver):
    By_xpath= driver.find_element_by_xpath
    By_ID= driver.find_element_by_id
    try:
        timeslot= By_xpath('//*[@id="preselectedBooking"]/td[3]/span/span').text
        print(timeslot)
        split_time= list(timeslot)
        print(split_time)
        time1= int(split_time[1]+split_time[2])
        time2= time1+1
        print(time2)
        new_time= str(time2)+":"+"00"
        print(new_time)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        # allure.attach(driver.get_screenshot_as_png(), name = 'booking_screen', attachment_type = AttachmentType.PNG)
        room_table= By_xpath(roomtableselectors.room_table).text
        # print(room_table)
        time.sleep(2)
        unavailable_room=By_xpath("//*[contains(text(),'{0}')]//ancestor::th//ancestor::tr//td".format(new_time))
        print(unavailable_room.text)
        unavailable_room_background_colour = Color.from_string(unavailable_room.value_of_css_property('background-color'))
        print(unavailable_room_background_colour)
        assert unavailable_room_background_colour.hex == '#f5c6cb'

    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(), name = 'exception_screen', attachment_type = AttachmentType.PNG)
        raise ex