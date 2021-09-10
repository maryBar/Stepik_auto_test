from selenium import webdriver
import time
import os
browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    inp1 = browser.find_element_by_name("firstname")
    inp1.send_keys("Ivan")
    inp2 = browser.find_element_by_name("lastname")
    inp2.send_keys("Ivanov")
    inp3 = browser.find_element_by_name("email")
    inp3.send_keys("ff@mail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    inp3 = browser.find_element_by_id("file")
    inp3.send_keys(file_path)
    opt = browser.find_element_by_tag_name("button")
    opt.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()