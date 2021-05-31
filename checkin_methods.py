from selector import commonpath,customersearchselectors
import time
import names
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from random import randint
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import allure
import pytest
from methods import find_element_by_text, find_element_by_text_input,find_element_by_text_div
from allure_commons.types import AttachmentType
from checkin_selector import loginselectors,checkinpageselectors,refundpageselectors

@allure.step("Selecvt site, change date and time:")
def site_selection(driver,site):
    By_xpath = driver.find_element_by_xpath
    Select(By_xpath(checkinpageselectors.site_newxpath)).select_by_visible_text(site)
    time.sleep(2)
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

@allure.step("To check in the customer")
def check_in(driver,waiver):
    By_xpath = driver.find_element_by_xpath
    By_xpath('//*[@id="preselectedBooking"]/td[1]/span[1]').click()
    # By_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id177"]/div').click()
    # By_xpath(checkinpageselectors.check_in_button_xpath).click()
    time.sleep(1)
    iframe= By_xpath(checkinpageselectors.iframe_xpath)
    driver.switch_to.frame(iframe)
    time.sleep(1)
    try:
        waiver=By_xpath(checkinpageselectors.participant_xpath)
        if waiver is not None:
            print("Already checked in")
            By_xpath(checkinpageselectors.checkin_close_button).click()
            driver.switch_to.default_content()
            time.sleep(1)
    except:
        By_xpath(checkinpageselectors.search_bar_xpath).clear()
        By_xpath(checkinpageselectors.search_bar_xpath).send_keys(waiver)
        By_xpath(checkinpageselectors.search_button_xpath).click()
        time.sleep(1)
        By_xpath(checkinpageselectors.waiver_xpath).click()
        time.sleep(1)
        try:
            By_xpath(checkinpageselectors.waiver_xpath).click()
            time.sleep(1)
            try:
                By_xpath(checkinpageselectors.waiver_xpath).click()
                time.sleep(1)
                try:
                    By_xpath(checkinpageselectors.waiver_xpath).click()
                    time.sleep(1)
                    try:
                        By_xpath(checkinpageselectors.waiver_xpath).click()
                        time.sleep(1)
                        try:
                            By_xpath(checkinpageselectors.waiver_xpath).click()
                            time.sleep(1)
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
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except Exception:
            print("no alert")
        driver.switch_to.default_content()
        time.sleep(1)

@allure.step("Add Notes to the booking")
def adding_notes(driver,notes):
    By_xpath = driver.find_element_by_xpath
    By_xpath('//*[@id="preselectedBooking"]/td[1]/a[1]/svg').click()
 
    time.sleep(3)
    try:
        By_xpath(checkinpageselectors.notes_text_xpath).clear()
        time.sleep(1)
        By_xpath(checkinpageselectors.notes_text_xpath).send_keys(notes)
        time.sleep(1)
    except:
        print("error in notes")
    allure.attach(driver.get_screenshot_as_png(), name = 'notes_image', attachment_type = AttachmentType.PNG)
    By_xpath(checkinpageselectors.save_changes_button_xpath).click()
    time.sleep(1)

@allure.step("checking details of booking")
def info(driver):  
            By_xpath = driver.find_element_by_xpath
            By_name = driver.find_element_by_name
            By_xpath('//*[@id="preselectedBooking"]/td[1]/a[2]').click()
            # driver.find_element_by_xpath('//*[@id="booking-data"]/tr/td[1]/a[2]').click()
            time.sleep(1)
            allure.attach(driver.get_screenshot_as_png(), name = 'info_screen_image', attachment_type = AttachmentType.PNG)
            try:
                By_name(checkinpageselectors.name_on_card_name).send_keys("John Watson")
                By_name(checkinpageselectors.card_number_name).send_keys("4976000000003436")
                By_name(checkinpageselectors.expiry_month_name).send_keys("12")
                By_name(checkinpageselectors.expiry_year_name).send_keys("21")
                By_name(checkinpageselectors.cv2_name).send_keys("452")
                By_name(checkinpageselectors.pay_button_name).click()
                By_xpath(checkinpageselectors.close_button_xpath).click()
                time.sleep(2)
            except:
                By_xpath(checkinpageselectors.close_button_xpath).click()
                time.sleep(1)

@allure.step("To change the date or time of selected product")
def change_datetime(driver,date,number):
    try:
            By_xpath = driver.find_element_by_xpath
            time.sleep(1)
            By_xpath('//*[@id="preselectedBooking"]/td[1]/span[3]').click()
            # By_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id187"]/a').click()
            time.sleep(2)
            By_xpath(checkinpageselectors.p1_xpath).click()
            time.sleep(1)
            By_xpath(checkinpageselectors.date_xpath).send_keys(date)
            time.sleep(5)
            print(date)
            allure.attach(driver.get_screenshot_as_png(), name = 'change_date/time_screen', attachment_type = AttachmentType.PNG)
            try:
                t1=By_xpath(checkinpageselectors.change_time).text
                By_xpath(checkinpageselectors.change_time).click()
            except:
                t2=By_xpath(checkinpageselectors.change_time2).text
                By_xpath(checkinpageselectors.change_time2).click()

            time.sleep(5)
            By_xpath(checkinpageselectors.date).send_keys(date)
            time.sleep(2)
            # By_xpath(checkinpageselectors.date).send_keys(date)
            # time.sleep(6)
            allure.attach(driver.get_screenshot_as_png(), name = 'new_date/time_checkin_screen', attachment_type = AttachmentType.PNG)
            time.sleep(1)
    except Exception as ex:
        raise ex
        
@allure.step("To go to refund section and then add product screen")
def got_to_add_products(driver):
    By_xpath = driver.find_element_by_xpath
    time.sleep(2)
    By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
    # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name = 'cancel_refund_screen', attachment_type = AttachmentType.PNG)
    By_xpath(refundpageselectors.add_product_btn).click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name = 'add_product_screen', attachment_type = AttachmentType.PNG)



@allure.step("Cancel the booking")
def cancel_refund(driver,checkin_date,):
    By_xpath = driver.find_element_by_xpath
    By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
    # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
    time.sleep(2)
    By_xpath(checkinpageselectors.cancel_refund_cancel_button_xpath).click()
    time.sleep(1)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except Exception:
        print("no alert")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name = 'cancel_refund_screen', attachment_type = AttachmentType.PNG)
    By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'after_cancel_booking_screen', attachment_type = AttachmentType.PNG)
    time.sleep(1)
   

@allure.step("UnCancel the booking")
def uncancel_a_booking(driver):
    By_xpath = driver.find_element_by_xpath
    By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
    # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
    By_xpath(checkinpageselectors.cancel_refund_cancel_button_xpath).click()
    time.sleep(2)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except Exception:
        print("no alert")
    time.sleep(4)
    allure.attach(driver.get_screenshot_as_png(), name = 'cancel_refund_screen', attachment_type = AttachmentType.PNG)
    By_xpath(checkinpageselectors.cancel_refund_cancel_button_xpath).click()
    time.sleep(1)
    By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name = 'after_uncancel_booking_screen', attachment_type = AttachmentType.PNG)
    time.sleep(1)

@allure.step(" To refund the amount ")
def refund_product_via_epos(driver):
    By_xpath= driver.find_element_by_xpath
    By_ID= driver.find_element_by_id
    try:
        By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
        # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
        time.sleep(1)
        By_xpath("//*[@title= 'Remove Products']").click()
        time.sleep(2)
        stage1= By_xpath(refundpageselectors.stage1).text
        assert stage1 == "Select Products - Current Stage"
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_screen', attachment_type = AttachmentType.PNG)
        By_xpath("//*[@title= 'Refund All']").click()
        time.sleep(1)
        stage2= By_xpath(refundpageselectors.stage2).text
        assert stage2== "Refund Method - Current Stage"
        By_xpath(refundpageselectors.buy_now_option).click()
        time.sleep(1)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        iframe = By_ID(refundpageselectors.iframe)
        driver.switch_to.frame(iframe)
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'epos_screen', attachment_type = AttachmentType.PNG)
        By_xpath(refundpageselectors.pay_btn).click()
        time.sleep(3)
        By_xpath(refundpageselectors.cash_btn_xpath).click()
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name = 'payment_time_screen', attachment_type = AttachmentType.PNG)
        By_xpath(refundpageselectors.no_receipt).click()
        time.sleep(3)
        driver.switch_to.default_content()
        time.sleep(2)
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
        time.sleep(2)
        By_xpath("//*[@title= 'Remove Products']").click()
        time.sleep(2)
        stage1= By_xpath(refundpageselectors.stage1).text
        assert stage1 == "Select Products - Current Stage"
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_screen', attachment_type = AttachmentType.PNG)
        By_xpath("//*[@title= 'Refund All']").click()
        time.sleep(2)
        stage2= By_xpath(refundpageselectors.stage2).text
        assert stage2== "Refund Method - Current Stage"
        By_xpath(refundpageselectors.online_option).click()
        time.sleep(1)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(1)
        # allure.attach(driver.get_screenshot_as_png(), name = 'creditcard_screen', attachment_type = AttachmentType.PNG)                         "
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
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except Exception:
            print("no alert")
        time.sleep(3)
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
        time.sleep(1)
    except Exception as ex:
        raise ex


@allure.step(" To refund the amount ")
def refund_product_via_giftcard(driver,giftcard):
    By_xpath= driver.find_element_by_xpath
    By_ID= driver.find_element_by_id
    try:
        By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
        # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
        time.sleep(2)
        By_xpath("//*[@title= 'Remove Products']").click()
        time.sleep(1)
        stage1= By_xpath(refundpageselectors.stage1).text
        # assert stage1 == "Select Products - Current Stage"
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_screen', attachment_type = AttachmentType.PNG)
        By_xpath("//*[@title= 'Refund All']").click()
        time.sleep(2)
        stage2= By_xpath(refundpageselectors.stage2).text
        # assert stage2== "Refund Method - Current Stage"
        By_xpath(refundpageselectors.gift_card_option).click()
        time.sleep(2)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(2)
        By_xpath(refundpageselectors.exsisting_card).click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        By_xpath(refundpageselectors.card_text).send_keys(giftcard)
        By_xpath(refundpageselectors.card_text).send_keys(Keys.ENTER)
        By_xpath(refundpageselectors.card_value).click()
        time.sleep(1)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(1)
        # allure.attach(driver.get_screenshot_as_png(), name = 'alert_screen', attachment_type = AttachmentType.PNG)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except Exception:
            print("no alert")
        time.sleep(5)
        voucher_table= By_xpath(refundpageselectors.voucher_table).text
        print(voucher_table)
        assert giftcard in voucher_table
        allure.attach(driver.get_screenshot_as_png(), name = 'voucher_screen', attachment_type = AttachmentType.PNG)
        By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
        time.sleep(3)
    except Exception as ex:
        raise ex
    

@allure.step(" To refund the amount ")
def refund_product_via_new_giftcard(driver,giftcard):
    By_xpath= driver.find_element_by_xpath
    By_ID= driver.find_element_by_id
    try:
        By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
        # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
        time.sleep(2)
        By_xpath("//*[@title= 'Remove Products']").click()
        time.sleep(1)
        # stage1= By_xpath(refundpageselectors.stage1).text
        # assert stage1 == "Select Products - Current Stage"
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_screen', attachment_type = AttachmentType.PNG)
        By_xpath("//*[@title= 'Refund All']").click()
        time.sleep(1)
        # stage2= By_xpath(refundpageselectors.stage2).text
        # assert stage2== "Refund Method - Current Stage"
        By_xpath(refundpageselectors.gift_card_option).click()
        time.sleep(1)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(1)
        By_xpath(refundpageselectors.new_card).click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        By_xpath(refundpageselectors.new_card_number).send_keys(giftcard)
        time.sleep(1)
        By_xpath(refundpageselectors.new_card_expiry).send_keys("6 Mar 2022")
        time.sleep(1)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(1)
        # allure.attach(driver.get_screenshot_as_png(), name = 'alert_screen', attachment_type = AttachmentType.PNG)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except Exception:
            print("no alert")
        time.sleep(2)
        voucher_table= By_xpath(refundpageselectors.voucher_table).text
        print(voucher_table)
        assert giftcard in voucher_table
        By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(), name = 'voucher_screen', attachment_type = AttachmentType.PNG)
    except Exception as ex:
        raise ex

allure.step(" To refund the amount ")
def refund_product_via_no_refund(driver):
    By_xpath= driver.find_element_by_xpath
    By_ID= driver.find_element_by_id
    try:
        By_xpath('//*[@id="preselectedBooking"]/td[1]/span[4]').click()
        # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:registration-table:j_id172:0:j_id192"]/a').click()
        time.sleep(2)
        By_xpath("//*[@title= 'Remove Products']").click()
        time.sleep(1)
        # stage1= By_xpath(refundpageselectors.stage1).text
        # assert stage1 == "Select Products - Current Stage"
        refund_amt=By_xpath(refundpageselectors.all_refund_value).text
        print(refund_amt)
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_screen', attachment_type = AttachmentType.PNG)
        By_xpath("//*[@title= 'Refund All']").click()
        time.sleep(2)
        # stage2= By_xpath(refundpageselectors.stage2).text
        # assert stage2== "Refund Method - Current Stage"
        By_xpath(refundpageselectors.no_refund_option).click()
        time.sleep(1)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(1)
        By_xpath(refundpageselectors.next_btn).click()
        time.sleep(1)
        # allure.attach(driver.get_screenshot_as_png(), name = 'alert_screen', attachment_type = AttachmentType.PNG)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except Exception:
            print("no alert")
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'refund_screen', attachment_type = AttachmentType.PNG)
        booking_value_amt= By_xpath(refundpageselectors.booking_value).text
        print(booking_value_amt)
        assert booking_value_amt == "GBP 0.00" or booking_value_amt == "0,00 EUR"
        By_xpath(checkinpageselectors.cancel_booking_close_btn).click()
        time.sleep(1)
    except Exception as ex:
        raise ex
    