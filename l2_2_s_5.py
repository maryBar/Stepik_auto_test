from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_el = browser.find_element_by_id("input_value")
    x1 = x_el.text
    x = math.log(abs(12 * math.sin(int(x1))))
    button = browser.find_element_by_tag_name("button")

    inp1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp1)
    inp1.send_keys(f"{x}")
    opt1 = browser.find_element_by_id("robotCheckbox")
    opt1.click()
    opt2 = browser.find_element_by_css_selector("[value='robots']")

    opt2.click()
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
