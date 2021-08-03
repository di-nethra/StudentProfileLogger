
from selenium import webdriver


from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\\Users\Dinethrex\\Downloads\\DriversSelenium\\chromedriver.exe")
# #C:\Users\Dinethrex\Downloads\DriversSelenium\chromedriver.exe
#
# url=input("enter browser URL:")
# driver.get(url)
# # https://www.csestack.org/
# print(driver.title)
#
# driver.close()



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
driver.get("http://student.sliit.lk/profile/");
regnum=input("enter Student ID:")
nic=input("Enter NIC:")
driver.find_element_by_id("regno").send_keys(regnum)
driver.find_element_by_id("nic").send_keys(nic)
driver.find_element_by_name("submit").click()
