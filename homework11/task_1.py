# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://saby.ru/'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    assert driver.current_url == 'https://saby.ru/'
    contact_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu')
    contact_btn.click()
    sleep(1)
    contact_menu = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__items')
    assert contact_menu.is_displayed()
    other_btn = driver.find_element(By.CSS_SELECTOR, "[href='/contacts']")
    other_btn.click()
    contact_url = 'https://saby.ru/contacts/'
    sleep(1)
    assert contact_url in driver.current_url
    logo_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    logo_btn.click()


    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://tensor.ru/'
    pwr = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    pwr.location_once_scrolled_into_view
    assert pwr.is_displayed()
    about_btn = driver.find_elements(By.CSS_SELECTOR, '[href="/about"]')
    about_btn[1].click()
    assert driver.current_url == 'https://tensor.ru/about'
    sleep(3)
finally:
    driver.quit()
