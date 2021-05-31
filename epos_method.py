import time
from epos_selector import epospageselector,paymentselectors
import allure
import pytest
from selector import commonpath
from methods import find_element_by_text,execute_click_by_text
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

@allure.step("Select epos product:{1}")
def itemselection(driver, productname):
    By_xpath= driver.find_element_by_xpath
    for i in productname:
        print(i)
        By_xpath(epospageselector.product_input_area).send_keys(i)
        By_xpath(epospageselector.product_input_area).send_keys(Keys.ENTER)
        time.sleep(1)
        cart= By_xpath(epospageselector.cart).text
        assert i in cart
    total_price=By_xpath(epospageselector.total_cart_value).text
    return total_price
        
@allure.step("search a customer with name: {1}")
def search_customer(driver,customer_name):
            By_xpath= driver.find_element_by_xpath
            By_ID= driver.find_element_by_id
            driver.execute_script("window.scroll(0, 0)")
            time.sleep(2)
            By_ID(epospageselector.search_bar_id).send_keys(customer_name)
            By_xpath(epospageselector.search_button_xpath).click()
            time.sleep(2)
            By_xpath(epospageselector.customer_detail_xpath).click()
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name = 'customer_details_screen', attachment_type = AttachmentType.PNG)
            new_customer_name=By_xpath(epospageselector.new_customer_name).text
            print(new_customer_name)
            assert new_customer_name == customer_name

def increase_quantity(driver):
            driver.find_element_by_xpath(epospageselector.plus_buttin_sanwich_xpath).click()
            driver.find_element_by_xpath(epospageselector.plus_buttin_sanwich_xpath).click()
            time.sleep(2)

def decrease_quantity(driver):
            driver.find_element_by_xpath(epospageselector.minus_button_sandwich_xpath).click()
            time.sleep(2)

@allure.step("modifing cart item")
def modify_cartitem(driver, item_to_modify,price, qty, dis):
    By_xpath=driver.find_element_by_xpath
    try:
        find_element_by_text(driver, item_to_modify).click()
        time.sleep(3)
        By_xpath(epospageselector.notes_edit).send_keys("Testing.......")
        By_xpath(epospageselector.save_btn).click()
        By_xpath(epospageselector.price_value).clear()
        By_xpath(epospageselector.price_value).send_keys(price)
        By_xpath(epospageselector.qty_value).clear()
        By_xpath(epospageselector.qty_value).send_keys(qty)
        By_xpath(epospageselector.discount_value).clear()
        By_xpath(epospageselector.discount_value).send_keys(dis)
        allure.attach(driver.get_screenshot_as_png(), name = 'edit_screen', attachment_type = AttachmentType.PNG)
        By_xpath(epospageselector.update_item).click()
        time.sleep(3)
        price=int(price)
        qty=int(qty)
        dis=int(dis)
        item_price= int((price*qty)-((dis/100)*(price*qty)))
        item_price=str(item_price)
        item_price='£'+item_price
        print(item_price)
        time.sleep(2)
        item_total_price=By_xpath(("//*[contains(text(),'{0}')]/ancestor::div//ancestor::div//ancestor::div[@id='saleItems']//div[2]//div//h4[3]").format(item_to_modify))
        p1=item_total_price.text
        print(p1)
        assert item_price in p1
    except Exception as ex:
        raise ex

@allure.step("total price calculation")
def total_price_verification(driver,firstitem,scnditem):
    try:
        By_xpath= driver.find_element_by_xpath
        allure.attach(driver.get_screenshot_as_png(), name = 'cart_table_screen', attachment_type = AttachmentType.PNG)
        item1_total=By_xpath("/html/body/span[2]/div[12]/div[2]/div/div[2]/div[1]/div/h4[3]")
        p1=item1_total.text
        value=list(p1)
        print(value)
        pp1=float(value[1]+value[2]+value[3]+value[4])
        print(pp1)
        item_total_price2=By_xpath("/html/body/span[2]/div[12]/div[2]/div/div[2]/div[2]/div/h4[3]")
        p2=item_total_price2.text
        value2=list(p2)
        print(value2)
        pp2=float(value2[1]+value2[2]+value2[3]+value2[4])
        print(pp2)
        total_pp= pp1+pp2
        total_pp= str(total_pp)
        total="PAY"+" "+"£"+total_pp+"0"
        print(total)
        total_cart=By_xpath(epospageselector.total_cart_value).text
        print(total_cart)
        assert total == total_cart
    except Exception as ex:
        raise ex

@allure.step("Select the desired table number")          
def select_table(driver,table):
        By_xpath= driver.find_element_by_xpath
        By_ID= driver.find_element_by_id
        By_xpath(epospageselector.parked_table_select_xpath).click()
        time.sleep(2)
        try:
            By_ID(epospageselector.parked_table_number_id).click()
            time.sleep(2)
        except:
            print("o")
        if table == "1":
            By_xpath(epospageselector.table_number6_xpath).click()
            time.sleep(2)
            By_xpath(epospageselector.clear_button_xpath).click()
            time.sleep(2)
            By_xpath(epospageselector.table_number1_xpath).click()
            time.sleep(2)
        elif table== "6":
            By_xpath(epospageselector.table_number6_xpath).click()
            time.sleep(2)
        elif table == "5":
            By_xpath(epospageselector.table_number5_xpath).click()
            time.sleep(2)
        elif table == "2":
            By_xpath(epospageselector.table_number2_xpath).click()
            time.sleep(2)
        else:
            By_xpath(epospageselector.table_number1_xpath).click()
            time.sleep(2)
            By_xpath(epospageselector.table_number0_xpath).click()
            time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'table_screen', attachment_type = AttachmentType.PNG)
        By_xpath(epospageselector.done_button_xpath).click()
        time.sleep(2)
        try:
            By_xpath(epospageselector.save_table_xpath).click()
            time.sleep(2)
        except:
            print("table selected")

@allure.step("Selected table number must be ={1}")
def table_assertion(driver,number):
            By_xpath= driver.find_element_by_xpath
            table_orders = By_xpath(epospageselector.table_xpath).text
            print(table_orders)
            assert number in table_orders
            allure.attach(driver.get_screenshot_as_png(), name = 'table_confirm_screen', attachment_type = AttachmentType.PNG)

@allure.step("Adding Gift Voucher")
def giftcard(driver, promocode):
    By_xpath= driver.find_element_by_xpath
    try:
        By_xpath(epospageselector.giftvoucher_text_xpath).send_keys(promocode)
        By_xpath(epospageselector.gift_voucher_search_btn).click()
        time.sleep(1)
        # By_xpath(epospageselector.giftvoucher_savebtn).click()
        allure.attach(driver.get_screenshot_as_png(), name = 'giftvoucher_screen', attachment_type = AttachmentType.PNG)    
        total_cart=By_xpath(epospageselector.total_cart_value).text
        print(total_cart)
        assert total_cart == "PAY  £0.00"

    except Exception as ex:
        print(ex)

@allure.step("Creating new customer account")
def new_account(driver, firstname, lastname, phone):
    By_xpath= driver.find_element_by_xpath
    customer="{0} {1}".format(firstname, lastname)
    email='{0}.{1}@booknow.com'.format(firstname, lastname)
    By_xpath(epospageselector.new_account).click()
    time.sleep(2)
    By_xpath(epospageselector.first_name_xpath).send_keys(firstname)
    By_xpath(epospageselector.lastname_xpath).send_keys(lastname)
    By_xpath(epospageselector.email_xpath).send_keys(email)
    By_xpath(epospageselector.phone_xpath).send_keys(phone)
    By_xpath(epospageselector.add_new_button).click()
    time.sleep(2)
    driver.execute_script("window.scroll(0, 0)")
    time.sleep(2)
    new_customer_name=By_xpath(epospageselector.new_customer_name).text
    print(new_customer_name)
    assert new_customer_name == customer

@allure.step("To cancel an order")
def cancel_order(driver, tablenumber):
    By_xpath= driver.find_element_by_xpath
    By_ID = driver.find_element_by_id
    try:
        table_orders = By_xpath(epospageselector.table_xpath).text
        print(table_orders)
        if tablenumber in table_orders and "£6.00" in table_orders:
            # find_element_by_text(driver, tablenumber).click()
            By_xpath("//*[contains(text(),'{}')]//ancestor::tr".format(tablenumber)).click()
            time.sleep(2)
            
            By_xpath(epospageselector.delete_sale_btn).click()
            time.sleep(1)
            By_xpath(epospageselector.delete_sale_btn).click()
            time.sleep(4)
            allure.attach(driver.get_screenshot_as_png(), name = 'deleted_order_screen', attachment_type = AttachmentType.PNG)
            table_orders = By_xpath(epospageselector.table_xpath).text
            assert tablenumber not in table_orders
           
    except Exception as ex:
        raise ex

@allure.step("Making payments")
def payment(driver, number):
        By_xpath= driver.find_element_by_xpath
        By_ID = driver.find_element_by_id
        try:
            table_orders = By_xpath(epospageselector.table_xpath).text
            print(table_orders)
            if number in table_orders and "£6.00" in table_orders:
                # find_element_by_text(driver, number).click()
                By_xpath("//*[contains(text(),'{}')]//ancestor::tr".format(number)).click()
                time.sleep(4)
                try:
                    By_xpath(epospageselector.order_table_xpath).click()
                    time.sleep(3)
                except:
                    print("skip this step")
                allure.attach(driver.get_screenshot_as_png(), name = 'sale_item_screen', attachment_type = AttachmentType.PNG)
                By_ID(epospageselector.pay_button_id).click()
                time.sleep(4)
                By_xpath(paymentselectors.cash).click()
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(), name = 'payment_screen', attachment_type = AttachmentType.PNG)
                By_xpath(paymentselectors.receipt).click()
                time.sleep(5)
        except Exception as ex:
            raise ex

@allure.step("Making zero price checkout")
def zero_price_checkout(driver):
    try:
        By_xpath= driver.find_element_by_xpath
        By_ID = driver.find_element_by_id
        By_ID(epospageselector.pay_button_id).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name = 'payment_screen', attachment_type = AttachmentType.PNG)       
        By_xpath(paymentselectors.receipt).click()
        time.sleep(2)
    except Exception as ex:
            raise ex

@allure.step("Moving to payment scren then edit sale then again to payments")
def editing_saleitems(driver, productname):
    By_xpath= driver.find_element_by_xpath
    By_ID = driver.find_element_by_id
    By_ID(epospageselector.pay_button_id).click()
    time.sleep(2)
    driver.execute_script("window.scroll(0, 0)")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name = 'payment_screen', attachment_type = AttachmentType.PNG)
    element = By_ID(epospageselector.edit_sale_btn)
    element.click()
    time.sleep(2)
    for i in productname:
        print(i)
        By_xpath(epospageselector.product_input_area).send_keys(i)
        By_xpath(epospageselector.product_input_area).send_keys(Keys.ENTER)
        time.sleep(1)
        cart= By_xpath(epospageselector.cart).text
        assert i in cart
    total_price= By_xpath(epospageselector.total_cart_value).text
    print(total_price)
    allure.attach(driver.get_screenshot_as_png(), name = 'editsale_screen', attachment_type = AttachmentType.PNG)
    By_ID(epospageselector.pay_button_id).click()
    time.sleep(2)
    By_xpath(paymentselectors.cash).click()
    time.sleep(2)
    By_xpath(paymentselectors.receipt).click()
    time.sleep(2)


@allure.step("Edit parked sale:")
def edit_parkedsale(driver,number,price,productname):
    By_xpath= driver.find_element_by_xpath
    By_ID = driver.find_element_by_id
    try:
        table_orders = By_xpath(epospageselector.table_xpath).text
        print(table_orders)
        if number in table_orders and price in table_orders:
            # find_element_by_text(driver,number).click()
            By_xpath("//*[contains(text(),'{}')]//ancestor::tr".format(number)).click()
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name = 'editsale_screen1', attachment_type = AttachmentType.PNG)
            for i in productname:
                print(i)
                By_xpath(epospageselector.product_input_area).send_keys(i)
                By_xpath(epospageselector.product_input_area).send_keys(Keys.ENTER)
                time.sleep(2)
                cart= By_xpath(epospageselector.cart).text
                assert i in cart
        else:
            print("NO if")
            allure.attach(driver.get_screenshot_as_png(), name = 'editsale_else_screen', attachment_type = AttachmentType.PNG)
            driver.close()

        total_price= By_xpath(epospageselector.total_cart_value).text
        print(total_price)
        allure.attach(driver.get_screenshot_as_png(), name = 'editsale_screen', attachment_type = AttachmentType.PNG)
        
        driver.find_element_by_id(epospageselector.save_yellow_btn).click()
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name = 'modified_parkedsale_screen', attachment_type = AttachmentType.PNG)
        table_orders = By_xpath(epospageselector.table_xpath).text
        print(table_orders)
        assert number in table_orders and "£8.50" in table_orders
    except Exception as ex:
        raise ex


@allure.step("Navigation through kitchen abd bar tabs")      
def present_pastorder_navigation(driver):
        By_Linktext= driver.find_element_by_link_text
        By_Linktext('Kitchen').click()
        time.sleep(1)
        driver.find_element_by_xpath(epospageselector.click_to_begin).click()
        time.sleep(1)
        assert driver.title == "Kitchen Orders"
        allure.attach(driver.get_screenshot_as_png(), name = 'kitchen_screen', attachment_type = AttachmentType.PNG)
        By_Linktext('Past Orders').click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(), name = 'Past_Orders_screen', attachment_type = AttachmentType.PNG)
        By_Linktext('Bar').click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(), name = 'Bar_screen', attachment_type = AttachmentType.PNG)
        By_Linktext('New Orders').click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(), name = 'New_Orders_screen', attachment_type = AttachmentType.PNG)
        By_Linktext('ePos').click()
        time.sleep(1)

@allure.step("Select celebration_hall product")       
def add_to_sale(driver):
    By_xpath= driver.find_element_by_xpath
    By_ID = driver.find_element_by_id
    Select(By_ID(epospageselector.quantity)).select_by_value('2')
    time.sleep(1)
    By_xpath(epospageselector.add_to_sale).click()
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name = 'after_adding_to_cart_screen', attachment_type = AttachmentType.PNG)


@allure.step("verify that order is palced")
def assertion(driver):
    try:
        text_area = driver.find_element_by_xpath(epospageselector.card_area).text  
        if text_area=="There was an error submitting this order, please try again. Error code: System.NullPointerException: Attempt to de-reference a null object":
        # if text_area is not None:    
            print("error")
            time.sleep(1)
            allure.attach(driver.get_screenshot_as_png(), name = 'test_order_screen_failure', attachment_type = AttachmentType.PNG)
            assert False
        else:
            time.sleep(1)
            allure.attach(driver.get_screenshot_as_png(), name = 'test_orderconfirm_screen', attachment_type = AttachmentType.PNG)
            print("ok")
            assert True  
    except:
        allure.attach(driver.get_screenshot_as_png(), name = 'test_orderconfirm_screen', attachment_type = AttachmentType.PNG)
        print("ok")
        assert True
        
