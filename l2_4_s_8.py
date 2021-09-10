from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button.click()
x = browser.find_element_by_id("input_value").text
x = math.log(abs(12 * math.sin(int(x))))
opt1 = browser.find_element_by_id("answer")
opt1.send_keys(f"{x}")
button = browser.find_element_by_id("solve")
button.click()
allert = browser.switch_to.alert
allert_text = allert.text
print(allert_text)
allert.accept()

browser.quit()
