from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    opt = browser.find_element_by_tag_name("button")
    opt.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    x = math.log(abs(12 * math.sin(int(x))))
    opt1 = browser.find_element_by_id("answer")
    opt1.send_keys(f"{x}")
    button = browser.find_element_by_tag_name("button")
    button.click()
    allert = browser.switch_to.alert
    allert_text = allert.text
    print(allert_text)
    allert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()