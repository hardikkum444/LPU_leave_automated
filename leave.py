# Dont run this, run leave_applier.py
# Run this only if you want to run without firefoxe's GUI
# This is strictly terminal based
# PLEASE LOOK AT LINE 129 FOR MORE REFERENCE!!!
# No threads have been put to sleep (pretty quick as well)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import getpass

GREEN = "\033[92m"
RESET = "\033[0m"

def get_creds():

    username      = input("Username-> ")
    password      = getpass.getpass("Password-> ")
    print()
    print("which type?")
    print("'1' for night leave")
    print("'2' for day leave")
    print("'3' for day leave (extended)")
    print("'4' for night leave (extended)")
    num = input("Enter digit only-> ")
    print()
    stay_adress   = input("Stay Address-> ")
    mobile_number = input("Guardian mobile number-> ")
    leave_reason  = input("Leave reason-> ")
    date1         = input("Date of leaving-> ")
    time1         = input("Time of leaving (format ex: 7:45 PM)-> ")
    date2         = input("Date of returning-> ")
    time2         = input("Time of returning (format ex: 7:45 PM)-> ")
    
    return username,password,stay_adress,mobile_number,leave_reason, date1, date2, time1, time2, num


def login_to_website(username, password, stay_adress, mobile_number, leave_reason, date1, date2, time1, time2, num):
   
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()
    
    driver.get("https://ums.lpu.in/lpuums/")

    driver.find_element("name","txtU").send_keys(username)
    driver.find_element("id","TxtpwdAutoId_8767").send_keys(password)
    
    time.sleep(1)

    driver.find_element("id","TxtpwdAutoId_8767").send_keys(password)
    driver.find_element("id","iBtnLogins150203125").click()
    
  #  time.sleep(1)

    driver.get("https://ums.lpu.in/lpuums/frmStudentHostelLeaveApplicationTermWise.aspx")

  #  time.sleep(1)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$ddlLeaveTerm"))
    dropdown.select_by_index(1)
    
  #  time.sleep(1)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$drpLeaveType"))
    dropdown.select_by_index(num)
    
    #time.sleep(1)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$ddlVisitDay"))

    dropdown.select_by_visible_text("Other")

  #  time.sleep(1)
    
    driver.find_element("id","ctl00_cphHeading_txtPlaceToVisit").send_keys(stay_adress)

    time.sleep(1)

    driver.find_element("id","ctl00_cphHeading_txtVisitingMobile").send_keys(mobile_number)
    
  #  time.sleep(1)
    
    driver.find_element("id","ctl00_cphHeading_txtLeaveReason").send_keys(leave_reason)

    driver.find_element("id","ctl00_cphHeading_startdateRadDateTimePicker1_popupButton").click()

    xpath_expression1 = f"//a[contains(text(), '{date1}')]"
    xpath_expression2 = f"//a[contains(text(), '{date2}')]"
    xpath_expression3 = f"//a[contains(text(), '{time1}')]"
    xpath_expression4 = f"//a[contains(text(), '{time2}')]"

    driver.find_element(By.XPATH, xpath_expression1).click()

    #driver.find_element(By.XPATH, "//a[text()='22']").click()

  #  time.sleep(1)

    driver.find_element("id","ctl00_cphHeading_startdateRadDateTimePicker1_timePopupLink").click()

    driver.find_element(By.XPATH, xpath_expression3).click()

    #driver.find_element(By.XPATH, "//a[text()='7:45 PM']").click()

  #  time.sleep(1)

    driver.find_element("id","ctl00_cphHeading_enddateRadDateTimePicker2_popupButton").click()

    driver.find_element(By.XPATH, xpath_expression2).click()

    # driver.find_element(By.XPATH, "//a[text()='23']").click()

    #time.sleep(1)

    driver.find_element("id","ctl00_cphHeading_enddateRadDateTimePicker2_timePopupLink").click()

    driver.find_element(By.XPATH, xpath_expression4).click()

#    driver.find_element(By.XPATH, "//a[text()='7:45 PM']").click()
    
    print(f"{GREEN}Leave applied successfully{RESET}")


    # UNCOMMENT THIS ONLY IF YOU ARE SURE ABOUT SUBMITTING
    # THIS WILL SUBMIT, SO MAKE SURE THAT INFO ENTERED IS CORRECT
    #driver.find_element("name","ctl00$cphHeading$btnSubmit").click()

    driver.quit()

def main():
    
    username, password, stay_adress, mobile_number, leave_reason, date1, date2, time1, time2, num = get_creds()
    login_to_website(username, password, stay_adress, mobile_number, leave_reason, date1, date2, time1, time2, num)



if __name__ == "__main__":
    main()

