
class loginselectors:
    username = 'j_id0:j_id4:inputUser'
    password = "j_id0:j_id4:inputPassword"
    login = "j_id0:j_id4:j_id17"

class checkinpageselectors:
    date="/html/body/div[2]/div/div[3]/form[1]/div[1]/div[2]/div/input"
    iframe_xpath = '/html/body/div[2]/div/div[8]/div/div/div/div/iframe'
    site_newxpath="/html/body/div[2]/div/div[3]/form[1]/div[1]/div[1]/div/select"
    site_xpath = '/html/body/div[2]/div/div[3]/form[2]/div[1]/table/tbody/tr[1]/td[1]/select'
    time_bar_name = 'j_id0:j_id1:date-filters:j_id125'
    booking_data="/html/body/div[2]/div/div[3]/form[2]/table"
    notes_button_xpath = '/html/body/div[2]/div/div[3]/form[3]/table/tbody/tr/td[1]/a[1]'
    notes_text_xpath = "/html/body/div[2]/div/div[3]/form[2]/div[3]/div/div/div[2]/textarea"
    save_changes_button_xpath = "/html/body/div[2]/div/div[3]/form[2]/div[3]/div/div/div[3]/button[2]"

    cancel_booking_btn= '/html/body/div[2]/div/div[6]/div/div/div[1]/div/div/div/article/div[2]/div/div[1]/div[1]/article/div[1]/header/div[3]/button'
    cancel_booking_close_btn="/html/body/div[2]/div/div[6]/div/div/div[2]/button"                                              
    info_button_xpath = '/html/body/div[2]/div/div[3]/form[3]/table/tbody/tr/td[1]/a[2]'
    name_on_card_name = 'j_id0:j_id1:j_id813:j_id826'
    card_number_name = 'j_id0:j_id1:j_id813:j_id828'
    expiry_month_name = 'j_id0:j_id1:j_id813:j_id830'
    expiry_year_name = 'j_id0:j_id1:j_id813:j_id833'
    cv2_name = 'j_id0:j_id1:j_id813:j_id844'
    pay_button_name = 'j_id0:j_id1:j_id813:j_id854'
    close_button_xpath = '/html/body/div[2]/div/span[5]/span/div/div/div/div[2]/button[3]'
    
    change_datetime_button_xpath = '/html/body/div[2]/div/div[3]/form[3]/table/tbody/tr/td[1]/span[3]/a'
    close_date_xpath ="/html/body/div[2]/div/span[2]/span/form/div[1]/div/div/div[3]/button"
    p1_xpath="/html/body/div[2]/div/span[2]/span/form/div[1]/div/div/div[2]/div/div/div"
    date_xpath="/html/body/div[2]/div/span[2]/span/form/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/input"
    change_time="/html/body/div[2]/div/span[3]/span/form/div[1]/div/div/div[2]/div/div[2]/div/center/small[1]"
    change_time2="/html/body/div[2]/div/span[2]/span/form/div[1]/div/div/div[2]/div/div[2]/div/center/small[1]"
    capacity_xpath="/html/body/div[2]/div/div[4]/div[1]/span/div/div/select"
            
    cancel_refunds_xpath= '/html/body/div[2]/div/div[3]/form[3]/table/tbody/tr[1]/td[1]/span[4]/a/span'
    cancel_refund_cancel_button_xpath="/html/body/div[2]/div/span[3]/span/form/div[1]/div/div/div[2]/div[2]/span/a"
    cancel_norefund_xpath= '/html/body/div[2]/div/span[3]/span/form/div[1]/div/div/div[2]/div[2]/span/a'
                            
    check_in_button_xpath = '/html/body/div[2]/div/div[3]/form[3]/table/tbody/tr/td[1]/span[1]/span/span/div'
    search_bar_xpath= '/html/body/span[2]/nav/form/div[1]/ul/li[1]/div/input'
    search_button_xpath = '/html/body/span[2]/nav/form/div[1]/ul/li[1]/div/div/button'
    waiver1_id = 'nowaiverhover'
    waiver_xpath="/html/body/span[2]/div/div/div[1]/form/div[1]/div/div/div"
    final_checkin_button_xpath = '/html/body/span[2]/nav/form/div[1]/div/button'

    save_button_xpath = '/html/body/div[2]/div/span[3]/span/form/div[1]/div/div/span/div[2]/a'
    participant_xpath="/html/body/span[2]/div/div/div[2]/form/div[1]/div/div/div[1]"
    checkin_close_button="/html/body/span[2]/nav/form/div[1]/div/a"

    checkin_table="/html/body/div[2]/div/div[3]/form[3]/table"

class refundpageselectors:
    stage1="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[1]/div/div/div/div/div/ul/lightning-progress-step[1]/a/span[1]/span"
    stage2= "/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[1]/div/div/div/div/div/ul/lightning-progress-step[2]/a/span[1]/span"
    buy_now_option="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div/div[1]/div/center"
    online_option="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div/div[2]/div/center"
    gift_card_option="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div/div[3]/div/center"
    no_refund_option="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div/div[4]/div/center"
    online_card_msg="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div[1]"
    payment_xpath="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div[2]/div/div"
    next_btn="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/footer/button[3]"
    pay_btn="/html/body/span[2]/div[12]/div[2]/div/div[3]/button"
    cash_btn_xpath="/html/body/span[2]/div[13]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/button"
    no_receipt="/html/body/span[2]/div[13]/main/div/div[2]/div[5]/span/div/div/div[3]/button"
    payments_table="/html/body/div[2]/div/div[6]/div/div/div[1]/div/div/div/article/div[2]/div/div[2]/div[2]/article"
    cash_refund_title="/html/body/div[2]/div/div[6]/div/div/div[1]/div/div/div/article/div[2]/div/div[2]/div[2]/article/div[2]/ul/li[2]/div/div[2]/h3/a"
    cash_refund_amount="/html/body/div[2]/div/div[6]/div/div/div[1]/div/div/div/article/div[2]/div/div[2]/div[2]/article/div[2]/ul/li[2]/div/div[2]/div/ul/li[1]/lightning-formatted-number"
    iframe = "eposFrame"
    iframe2= "staffbookingframe"
    add_product_btn="/html/body/div[2]/div/div[6]/div/div/div[1]/div/div/div/article/div[1]/header/div[2]/div/button[1]"
    exsisting_card="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div/div[2]/div/center"
    new_card="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div/div[1]/div/center"
    card_text="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div[2]/div[1]/lightning-input/div/input"
    card_value="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div[2]/div[2]/div/div/center"
    voucher_table="/html/body/div[2]/div/div[6]/div/div/div[1]/div/div/div/article/div[2]/div/div[1]/div[2]"
    new_card_number="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div[2]/article/div[2]/lightning-input[1]/div/input"
    new_card_expiry="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div[2]/article/div[2]/lightning-input[2]/lightning-datepicker/div/div/input"
    all_refund_value="/html/body/div[2]/div/div[6]/div/div/div[1]/div/section/div/div/div[2]/div/div[1]/div/center/lightning-formatted-number"
    booking_value="/html/body/div[2]/div/div[6]/div/div/div[1]/div/div/div/article/div[2]/div/div[1]/div[1]/article/div[2]/div/div[1]/center/lightning-formatted-number"


class roomtableselectors:
    booking_time= "j_id0:j_id1:registration-table:j_id172:4:j_id200"
    room_table="/html/body/div[2]/div/div[4]/div[5]/span/div/div"
