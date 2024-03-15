from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import getpass
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("730x860")

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def get_creds():

    username      = entry1.get()
    password      = entry2.get()
    # print()
    # print("which type?")
    # print("'1' for night leave")
    # print("'2' for day leave")
    # print("'3' for day leave (extended)")
    # print("'4' for night leave (extended)")
    # label2.configure(text="'1' for night leave\n'2' for day leave\n'3' for daye leave (extended)\n'4' for night leave (extended)")
    num = entry3.get()
    print()
    stay_adress   = entry4.get()
    mobile_number = entry5.get()
    leave_reason  = entry6.get()
    date1         = entry7.get()
    time1         = entry8.get()
    date2         = entry9.get()
    time2         = entry0.get()
    label1.configure(text="Please check your leave status on terminal")
    
    return username,password,stay_adress,mobile_number,leave_reason, date1, date2, time1, time2, num


def login_to_website(username, password, stay_adress, mobile_number, leave_reason, date1, date2, time1, time2, num):
   
    options = webdriver.FirefoxOptions()
    # options.add_argument("-headless")
    driver = webdriver.Firefox()

    print(f"{GREEN}Fetching ums{RESET}")
    driver.get("https://ums.lpu.in/lpuums/")

    time.sleep(1)

    driver.find_element("name","txtU").send_keys(username)
    driver.find_element("id","TxtpwdAutoId_8767").send_keys(password)
    
    time.sleep(1)

    driver.find_element("id","TxtpwdAutoId_8767").send_keys(password)
    driver.find_element("id","iBtnLogins150203125").click()
    
    time.sleep(2)

    try:
              error = driver.find_element("class name","confirm")
              error.click()
              print(f"{RED}error message closed, continuing with script{RESET}")
    except:
               print()
               print(f"{GREEN}no obstacles found, continuing with the script{RESET}")
    try:
              checkbox = driver.find_element("id","chkReadMessage")
              confirm = driver.find_element("id","btnClose")

              checkbox.click()
              confirm.click()
              print(f"{RED}UMS pop-up message closed{RESET}")

    except:
        print()
        print(f"{GREEN}no pop-up message found, continuing with the script{RESET}\n")

    driver.get("https://ums.lpu.in/lpuums/frmStudentHostelLeaveApplicationTermWise.aspx")

    time.sleep(1)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$ddlLeaveTerm"))
    dropdown.select_by_index(1)
    
    time.sleep(1)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$drpLeaveType"))
    dropdown.select_by_index(num)
    
    time.sleep(1)

    dropdown = Select(driver.find_element("name","ctl00$cphHeading$ddlVisitDay"))

    dropdown.select_by_visible_text("Other")

    time.sleep(1)
    
    driver.find_element("id","ctl00_cphHeading_txtPlaceToVisit").send_keys(stay_adress)

    time.sleep(1)

    driver.find_element("id","ctl00_cphHeading_txtVisitingMobile").send_keys(mobile_number)
    
    time.sleep(1)
    
    driver.find_element("id","ctl00_cphHeading_txtLeaveReason").send_keys(leave_reason)

    driver.find_element("id","ctl00_cphHeading_startdateRadDateTimePicker1_popupButton").click()

    xpath_expression1 = f"//a[contains(text(), '{date1}')]"
    xpath_expression2 = f"//a[contains(text(), '{date2}')]"
    xpath_expression3 = f"//a[contains(text(), '{time1}')]"
    xpath_expression4 = f"//a[contains(text(), '{time2}')]"

    driver.find_element(By.XPATH, xpath_expression1).click()

    #driver.find_element(By.XPATH, "//a[text()='22']").click()

    time.sleep(1)

    driver.find_element("id","ctl00_cphHeading_startdateRadDateTimePicker1_timePopupLink").click()

    driver.find_element(By.XPATH, xpath_expression3).click()

    #driver.find_element(By.XPATH, "//a[text()='7:45 PM']").click()

    time.sleep(1)

    driver.find_element("id","ctl00_cphHeading_enddateRadDateTimePicker2_popupButton").click()

    driver.find_element(By.XPATH, xpath_expression2).click()

    #driver.find_element(By.XPATH, "//a[text()='23']").click()

    time.sleep(1)

    driver.find_element("id","ctl00_cphHeading_enddateRadDateTimePicker2_timePopupLink").click()

    driver.find_element(By.XPATH, xpath_expression4).click()

    #driver.find_element(By.XPATH, "//a[text()='7:45 PM']").click()
    
    print(f"{GREEN}Leave applied successfully{RESET}")

    # this will quit without applying leave beacuse script doesn't automatically click SUBMIT (for safety reasons)
    #driver.quit()

def main():

    username, password, stay_adress, mobile_number, leave_reason, date1, date2, time1, time2, num = get_creds()
    login_to_website(username, password, stay_adress, mobile_number, leave_reason, date1, date2, time1, time2, num)

# custom_font = tkFont.Font('Ubuntu Regular', 18)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Leave applying system", font=('Arial', 22, 'bold'))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", width=200, font=('Arial', 16))
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*", width=200, font=('Arial', 16))
entry2.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="")
label2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Leave type", width=200, font=('Arial', 16))
entry3.pack(pady=12, padx=10)

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Stay address", width=200, font=('Arial', 16))
entry4.pack(pady=12, padx=10)

entry5 = customtkinter.CTkEntry(master=frame, placeholder_text="Phone number", width=200, font=('Arial', 16))
entry5.pack(pady=12, padx=10)

entry6 = customtkinter.CTkEntry(master=frame, placeholder_text="Reason", width=200, font=('Arial', 16))
entry6.pack(pady=12, padx=10)

label3 = customtkinter.CTkLabel(master=frame, text="")
label3.pack(pady=12, padx=10)

entry7 = customtkinter.CTkEntry(master=frame, placeholder_text="Date1", width=200, font=('Arial', 16))
entry7.pack(pady=12, padx=10)

entry8 = customtkinter.CTkEntry(master=frame, placeholder_text="Time1", width=200, font=('Arial', 16))
entry8.pack(pady=12, padx=10)

entry9 = customtkinter.CTkEntry(master=frame, placeholder_text="Date2", width=200, font=('Arial', 16))
entry9.pack(pady=12, padx=10)

entry0 = customtkinter.CTkEntry(master=frame, placeholder_text="Time2", width=200, font=('Arial', 16))
entry0.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=main)
button.pack(pady=12, padx=10)

label1 = customtkinter.CTkLabel(master=frame, text="")
label1.pack(pady=12, padx=10)

label2.configure(text="'1' for night leave\n'2' for day leave\n'3' for daye leave (extended)\n'4' for night leave (extended)",font=('Arial', 14))

label3.configure(text="Date format (24, just number, no space\nTime format (7:45 PM), ensure proper formatting)", font=('Arial',14))


root.mainloop()


# if __name__ == "__main__":
    # main()


