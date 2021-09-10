from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    opt = browser.find_element_by_tag_name("button")
    opt.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_el = browser.find_element_by_id("input_value")
    x = x_el.text
    n = math.log(abs(12 * math.sin(int(x))))
    inp1 = browser.find_element_by_id("answer")
    inp1.send_keys(f"{n}")

    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert
    alert_tex = alert.text
    print(alert_tex)
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()