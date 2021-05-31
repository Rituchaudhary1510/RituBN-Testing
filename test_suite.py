import unittest
from test_epos import TestEposBooking
from test_version3_staff import TestV3StaffBooking
# from test_version2_staff import TestV2StaffBooking
# from test_version3_kiosk import TestV3NewBooking
# from test_selfservice import TestSelfService
# from test_webstore import TestWebStoreBooking
# from test_membership import TestV3Membership
# from test_membership_bookings import TestV3MembershipBooking
# from test_v2_mem import TestV2Membership
# from test_v2_mem_booking import TestV2MembershipBooking
# from test_version2_customer import TestCustomerBooking
# from test_version3_checkin import TestV3CheckInBooking
from test_version2_checkin import TestV2CheckInBooking

# getting all the testcases together
epos_page_test = unittest.TestLoader().loadTestsFromTestCase(TestEposBooking)
staff_page_test = unittest.TestLoader().loadTestsFromTestCase(TestV3StaffBooking)
# v2_staff_page_test = unittest.TestLoader().loadTestsFromTestCase(TestV2StaffBooking)
# kiosk_page_test = unittest.TestLoader().loadTestsFromTestCase(TestV3NewBooking)
# selfservice_test= unittest.TestLoader().loadTestsFromTestCase(TestSelfService)
# webstore_test= unittest.TestLoader().loadTestsFromTestCase(TestWebStoreBooking)
# meshipmbership_test= unittest.TestLoader().loadTestsFromTestCase(TestV3Membership)
# member_test2= unittest.TestLoader().loadTestsFromTestCase(TestV3MembershipBooking)
# v2_membership_test= unittest.TestLoader().loadTestsFromTestCase(TestV2Membership)
# v2_membership_test2= unittest.TestLoader().loadTestsFromTestCase(TestV2MembershipBooking)
# v2_customer_test= unittest. TestLoader().loadTestsFromTestCase(TestCustomerBooking)
# checkin_page_test = unittest.TestLoader().loadTestsFromTestCase(TestV3CheckInBooking)
v2_checkin_page_test = unittest.TestLoader().loadTestsFromTestCase(TestV2CheckInBooking)


# create a test suite combining all test cases
# test_suite = unittest.TestSuite([])

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    # suite = suite()
    # runner.run(test_suite)