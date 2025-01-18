#chromedriver inializaion
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

user_data = "C:\\Users\\Bobby\\AppData\\Local\\Google\\Chrome\\User Data\\Guest Profile"
options = webdriver.ChromeOptions()

# options.add_argument("--headless")
# options.add_argument("--disable-gpu")

options.add_argument(f"user-data-dir={user_data}")

driver = webdriver.Chrome(options=options)
time.sleep(4)

driver.execute_script("window.open(' ');")
driver.switch_to.window(driver.window_handles[1])

driver.get("https://yopmail.com")
time.sleep(10)

# #opening a file we do:
# #if we want to write instead of reading a file we replace the 'r' w 'w' then add ', newline="" so it can go to a new line every time it writes'
# with open ("file location", "r") as file:
#     #if we want to add to a file we add this line
#     # writer = csv.writer(file)
#     for line in file:
#         driver.get("page")
#         # add this as well if we want to write a line
#         #writer.writerow([iteration])
    
# #if we want to find elements in a page we do:
# pageInput = driver.find_element(By.XPATH, PATH)
# pageInput.click()
# #or if we want to send a key we do
# pageInput = driver.find_element(By.XPATH, PATH).send_keys("test", Keys.ENTER)
        
        
driver.quit()