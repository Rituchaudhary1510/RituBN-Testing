class commonpath:
    path ="/home/bnuser/Documents/TestScripts-main/chromedriver"
    
class loginselectors:
    username = 'j_id0:j_id4:inputUser'
    password = "j_id0:j_id4:inputPassword"
    register= "custom-select"
    login = "j_id0:j_id4:j_id19"

class bookingpageselectors:
    site = '/html/body/div[2]/div/div[7]/div/div/div/div/ul/li[2]'
    date_xpath="/html/body/div[2]/div/div[5]/div/div/form/div[1]/center[2]/input"
    date_time_alert_xpath ='/html/body/div[2]/div/div[5]/div/div/form/div[2]/div[1]/div/div'
    date_time_close_button_xpath='/html/body/div[2]/div/div[5]/div/div/form/div[3]/button'
    skate_xpath = '/html/body/div[2]/div/div[7]/div/div/span[2]/div[4]/div/div/div[5]/div'
    other_productgroup="/html/body/div[2]/div/div[7]/div/div/div[2]/div/ul[1]/li[1]"
    new_price="/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li/div/div[1]/div/div[3]/b"
    price="/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li[1]/div/div[1]/div/div[3]/b"
    quantity = 'selectedTicketQuantity' 
    product_option_id="productOptions"
    productname_in_cart="/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li[1]/div/div[1]/div/div[1]/span"
    add_to_sale = '/html/body/div[2]/div/div[5]/div/div/form/div[2]/div[3]/div[2]/div/div/div[2]/a'
    full_day_add_to_sale="/html/body/div[2]/div/div[5]/div/div/form/div[2]/div[1]/div[2]/div/div/div[2]/a"
    additional_quatity = 'selectedAdditionalQuantity'
    add_to_sale2 = '/html/body/div[2]/div/div[6]/div/div/form/div[2]/div/div/div[2]/a'
    birthday_name="/html/body/div[2]/div/div[5]/div/div/form/div[2]/div[3]/div[4]/div/div/input"
    birthday_age="/html/body/div[2]/div/div[5]/div/div/form/div[2]/div[3]/div[5]/div/div/input"
                  
    birthday_product = "/html/body/div[2]/div/div[7]/div/div/div[2]/div/ul/li[2]"
    
    option_id="productOptions"

    promocode_success="successToast"
    promocode_error="errorToast"
    failure_error="errorToast"
    cart_table="/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul"
    remove_from_cart_button_xpath = '/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li[1]/div/div[2]/div/div[1]/span[2]'
    product_in_cart_xpath = '/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li[1]'
    cart_product_name_xpath = '/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li[2]/div/div[2]/div/div[1]/span[1]'
    
    new_xpath = '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/div/div[1]/div/div/div/button[1]'
    first_name_xpath= '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/form/div[1]/input'
    last_name_xpath= '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/form/div[2]/input'
    email_xpath = '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/form/div[3]/input'
    account_phone_xpath = '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/form/div[4]/input'
    dob_xpath = '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/form/div[5]/span/input'
    save_xpath = '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/form/div[6]/input'
    
    search_bar = 'customerSearchTerms'
    search_button = '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/div/div[2]/div/button'
    customer1_detail = '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/ul/li[2]'
    customer2_detail = '/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/ul/li[1]'
    customer_name="/html/body/div[2]/div/span[1]/span/span[1]/span/div[1]/div/div[3]/input"
                
    discount_xpath="/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li[1]/div/div[2]/div/div[2]/div/input"
    discount_save_button_xpath="/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li/div/div[2]/div/div[2]/div/div[2]/button"
    giftvoucher_text_xpath="/html/body/div[2]/div/span[1]/span/span[2]/span/div/div/div[2]/div/input"
    giftvoucher_add_btn="/html/body/div[2]/div/span[1]/span/span[2]/span/div/div/div[2]/div/span/button"
    
    actual_amount_xpath = "/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li[1]/div/div[1]/div/div[3]"
    checkout_button = '/html/body/div[2]/div/span[1]/span/span[2]/span/div/div/div[1]/span/div/button[1]'

class paymentselectors:
    online= '/html/body/div[2]/div/span[2]/div[1]/div/ul/li[1]'
    select_method_name = '/html/body/div[2]/div/span[2]/div[2]/span[1]/div/div/div/div[1]/div/div[2]/form/div[1]/div/select'
    amount_to_pay="/html/body/div[2]/div/span[2]/div[2]/span[1]/div/div/div/div[1]/div/div[2]/form/div[2]/div/p"
    card_number = 'card-number'
    name_on_card = 'card-holders-name'
    month_year = '/html/body/div[2]/div/span[2]/div[2]/span[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/input[1]'
    security_code = 'cvc'
    pay = '/html/body/div[2]/div/span[2]/div[2]/span[1]/div/div/div/div[2]/div/div[3]/button'
    pay_button="/html/body/div[2]/div/span[2]/div[2]/span[1]/div/div/div/div[2]/button"

    epos = '/html/body/div[2]/div/span[2]/div[1]/div/ul/li[2]'
    epos_register_crx_btn="/html/body/span[2]/div[3]/div/div/span/div/button"
    iframe = 'eposMethod'
    iframe2 = "payRemainingFrame"
    pay_now = 'payBtn'
    cash ="/html/body/span[2]/div[13]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/button"
    receipt = 'receiptConfirm'
    no_receipt_xpath = '/html/body/span[2]/div[13]/main/div/div[2]/div[5]/span/div/div/div[3]/button'
    no_receipt="/html/body/span[2]/div[13]/main/div/div[2]/div[5]/span/div/div[3]/button"
    receipt_xpath="/html/body/span[2]/div[13]/main/div/div[2]/div[3]/span/div/div/div[1]/button"

    skip_payment= '/html/body/div[2]/div/span[2]/div[1]/div/ul/li[3]'
    submit = '/html/body/div[2]/div/span[2]/div[2]/span[5]/div/div/div/div[2]/button'
    
    send_payment_link_xpath = '/html/body/div[2]/div/span[2]/div[1]/div/ul/li[8]'
    confirm_button_xpath = '/html/body/div[2]/div/span[2]/div[2]/span[4]/div/div/div/div[2]/button'
    
    element_xpath ='/html/body/div[2]/div/div[8]/div[1]/div/div/label[1]'

class confirmationpageselectors:
    confirmation_table= "/html/body/div[2]/div/div[8]"
    
    upper_table="/html/body/div[2]/div/div[8]/div[1]"
    cart_item="/html/body/div[2]/div/span[1]/span/span[2]/span/div/ul/li[1]/div/div[1]/div/div[3]"
    grand_total="/html/body/span[2]/div[13]/main/div/div[2]/div[1]/table[1]/tfoot/tr[3]/th[2]/b"

class customersearchselectors:
    booking_number_xpath="/html/body/div[2]/div/div[8]/div[1]/div/div/label[2]/span"
    customer_name_xpath="/html/body/div[2]/div/div[8]/div[1]/ul/li[2]/span[2]"
    customer_serach_button_xpath="/html/body/div[2]/div/div[2]/div[2]/a[3]/center"
    search_field_xpath="/html/body/div[2]/div/div[3]/div/div[3]/div[1]/div/lightning-input/div/input"
    customer_detail_link="/html/body/div[2]/div/div[3]/div/div[3]/div[3]/ul/li/section/div[1]/h3/button/span"

    view_btn="/html/body/div[2]/div/div[3]/div/div[3]/div[3]/ul/li/section/div[2]/div/div[1]/div[2]/lightning-datatable/div[2]/div/div/table/tbody/tr/td[4]/lightning-primitive-cell-factory/span/div/lightning-primitive-cell-button/lightning-button/button"
    first_go_btn="/html/body/div[2]/div/div[3]/div/section[2]/div/div/div/div[2]/lightning-datatable/div[2]/div/div/table/tbody/tr[1]/td[7]/lightning-primitive-cell-factory/span/div/lightning-primitive-cell-button/lightning-button/button"
    customer_table_list="/html/body/div[2]/div/div[3]/form/div[2]"
    booking_table_list="/html/body/div[2]/div/div[3]/form/div[2]/div/div[3]/div/div[1]"
    go_to_booking="/html/body/div[2]/div/div[3]/form/div[2]/div/div[3]/div/div[1]/div/div[1]/div/input"
    success_alert="/html/body/div[2]/div/div[3]/div[2]/div[2]/div"
    checkin_btn="/html/body/div[2]/div/div[2]/span/ul/a[2]"
    search_box="/html/body/div[2]/div/div[3]/input"
    find_customer="/html/body/div[2]/div/div[2]/span/ul/a[4]"
    eye_btn="/html/body/div[2]/div/div[3]/form[2]/table/tbody/tr[3]/td[1]/a[2]/svg"
    blue_pay_btn="/html/body/div[2]/div/span[5]/span/div/div/div/span/div/span[2]/form/span/div[2]/div[2]/input"
    balance_amt="/html/body/div[2]/div/span[5]/span/div/div/div/span/div/span[1]/div[4]/div[2]/div[2]/div[4]/span"
    rem_name_on_card="j_id0:j_id1:j_id802:j_id815"
    rem_card_number="j_id0:j_id1:j_id802:j_id817"
    rem_expiry_date="j_id0:j_id1:j_id802:j_id819"
    rem_expiry_year="j_id0:j_id1:j_id802:j_id822"
    rem_cv2="j_id0:j_id1:j_id802:j_id833"
    rem_pay_btn="j_id0:j_id1:j_id802:j_id843"