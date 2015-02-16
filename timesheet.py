# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://cas.ucdavis.edu/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_2(self):
        password = raw_input("password: ")
        start_date = raw_input("start date (first sunday): ")


        driver = self.driver
        driver.get(self.base_url + "/cas/login?service=https%3a%2f%2ftrs.ucdavis.edu%2ftrs%2femployee%2faccessCurrentTimesheet.htm")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("daniel93")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("a[title=\"View Timesheet\"] > img").click()

        time.sleep(3)

        for handle in driver.window_handles[1:]:
            driver.switch_to_window(handle)
            if(self.is_element_present(By.ID, "selection_18")):
                break

        driver.find_element_by_id("selection_" + str(start_date)).click()
        driver.find_element_by_id("dropdown-clock_" + str(start_date)).click()
        driver.find_element_by_id("weekList0.dayList0.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList0.dayList0.clockInOutList0.userClockIn").send_keys("4")
        driver.find_element_by_css_selector("span.hoverselect").click()
        driver.find_element_by_id("weekList0.dayList0.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList0.dayList0.clockInOutList0.userClockOut").send_keys("7")
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("selection_" + str(start_date + 1)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("dropdown-clock_" + str(start_date + 1)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList0.dayList1.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList0.dayList1.clockInOutList0.userClockIn").send_keys("8")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList0.dayList1.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList0.dayList1.clockInOutList0.userClockOut").send_keys("12")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("selection_" + str(start_date + 3)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("dropdown-clock_" + str(start_date + 1)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList0.dayList3.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList0.dayList3.clockInOutList0.userClockIn").send_keys("8")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList0.dayList3.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList0.dayList3.clockInOutList0.userClockOut").send_keys("10")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_css_selector("span.hoverselect").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("selection_" + str(start_date + 4)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("dropdown-clock_" + str(start_date + 4)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList0.dayList4.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList0.dayList4.clockInOutList0.userClockIn").send_keys("4")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_css_selector("span.hoverselect").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList0.dayList4.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList0.dayList4.clockInOutList0.userClockOut").send_keys("6")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("selection_" + str(start_date + 5)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("dropdown-clock_" + str(start_date + 5)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList0.dayList5.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList0.dayList5.clockInOutList0.userClockIn").send_keys("3")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_css_selector("span.hoverselect").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList0.dayList5.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList0.dayList5.clockInOutList0.userClockOut").send_keys("4")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("selection_" + str(start_date + 8)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("dropdown-clock_" +  + str(start_date + 8)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList1.dayList1.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList1.dayList1.clockInOutList0.userClockIn").send_keys("8")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList1.dayList1.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList1.dayList1.clockInOutList0.userClockOut").send_keys("12")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("selection_" + str(start_date + 10)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("dropdown-clock_" + str(start_date + 10)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList1.dayList3.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList1.dayList3.clockInOutList0.userClockIn").send_keys("8")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList1.dayList3.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList1.dayList3.clockInOutList0.userClockOut").send_keys("10")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_css_selector("span.hoverselect").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("selection_" + str(start_date + 11)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("dropdown-clock_" + str(start_date + 11)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList1.dayList4.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList1.dayList4.clockInOutList0.userClockIn").send_keys("7")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_css_selector("span.hoverselect").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList1.dayList4.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList1.dayList4.clockInOutList0.userClockOut").send_keys("11")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("selection_" + str(start_date + 12)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("dropdown-clock_" + str(start_date + 12)).click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList1.dayList5.clockInOutList0.userClockIn").clear()
        driver.find_element_by_id("weekList1.dayList5.clockInOutList0.userClockIn").send_keys("3")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_css_selector("span.hoverselect").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_id("weekList1.dayList5.clockInOutList0.userClockOut").clear()
        driver.find_element_by_id("weekList1.dayList5.clockInOutList0.userClockOut").send_keys("5")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]
        driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=c0-param3 | ]]   

        driver.find_element_by_name("save").click()


    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
