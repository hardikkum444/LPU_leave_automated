from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time



def get_creds():

    username = input("Username-> ")
    password = input("Password-> ")
    stay_adress = input("Stay Address-> ")
    mobile_number = input("Guardian mobile number-> ")
    leave_reason = input("Leave reason-> ")

    return username,password,stay_adress,mobile_number,leave_reason


def login_to_website(username, password, stay_adress, mobile_number, leave_reason):
   
    driver = webdriver.Firefox()

    driver.get("https://ums.lpu.in/lpuums/")

    driver.find_element("name","txtU").send_keys(username)
    driver.find_element("id","TxtpwdAutoId_8767").send_keys(password)
    
    time.sleep(2)

    driver.find_element("id","TxtpwdAutoId_8767").send_keys(password)
    driver.find_element("id","iBtnLogins150203125").click()
    
    time.sleep(2)

    driver.get("https://ums.lpu.in/lpuums/frmStudentHostelLeaveApplicationTermWise.aspx")

    time.sleep(2)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$ddlLeaveTerm"))
    dropdown.select_by_index(1)
    
    time.sleep(2)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$drpLeaveType"))
    dropdown.select_by_index(3)
    
    time.sleep(2)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$ddlVisitDay"))

    dropdown.select_by_visible_text("Other")

    time.sleep(2)
    
    driver.find_element("id","ctl00_cphHeading_txtPlaceToVisit").send_keys(stay_adress)

    time.sleep(2)

    driver.find_element("id","ctl00_cphHeading_txtVisitingMobile").send_keys(mobile_number)
    
    time.sleep(2)
    
    driver.find_element("id","ctl00_cphHeading_txtLeaveReason").send_keys(leave_reason)

    driver.find_element("id","ctl00_cphHeading_startdateRadDateTimePicker1_popupButton").click()

    driver.find_element(By.XPATH, "//a[text()='22']").click()

    time.sleep(2)

    driver.find_element("id","ctl00_cphHeading_startdateRadDateTimePicker1_timePopupLink").click()

    driver.find_element(By.XPATH, "//a[text()='7:45 PM']").click()

    # driver.quit()


def main():

    username, password, stay_adress, mobile_number, leave_reason = get_creds()
    login_to_website(username, password, stay_adress, mobile_number, leave_reason)



if __name__ == "__main__":
    main()

# ctl00_cphHeading_ddlLeaveTerm
# Term-II
