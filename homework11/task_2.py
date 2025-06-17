# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

#Скрываю панель включения уведомлений
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)
sbis_site = 'https://fix-online.sbis.ru/'
action = ActionChains(driver)

try:
    #авторизация
    driver.get(sbis_site)
    sleep(2)
    driver.maximize_window()
    login = driver.find_element(By.CSS_SELECTOR, '.controls-Field')
    login.send_keys('Леший', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    password.send_keys('Леший123', Keys.ENTER)
    sleep(3)

    #Контакты-контакты
    contact_1 = driver.find_elements(By.CSS_SELECTOR,'[data-qa=NavigationPanels-Accordion__title]')
    contact_1[0].click()
    sleep(1)
    contact_2 = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contact_2.click()
    sleep(2)


    #Выбор получателя
    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    add_btn.click()
    sleep(3)
    search_field = driver.find_element(By.CSS_SELECTOR, '.controls-Field ')
    search_field.send_keys('Леший Лесной', Keys.ENTER)
    sleep(1)
    add_emp = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-selector__addressee')
    add_emp.click()
    sleep(1)

    #Отправка сообщения и проверка его наличия
    textbox = driver.find_element(By.CSS_SELECTOR, '.textEditor_slate_Field')
    textbox.send_keys('Message 4 myself', Keys.ENTER)
    sleep(1)
    send_notif = driver.find_element(By.CSS_SELECTOR, '.controls-Notification__simpleTemplate')
    assert send_notif.is_displayed()

    #Удаление сообщения
    msg_dialogs = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item')
    action = ActionChains(driver)
    action.move_to_element(msg_dialogs[0])
    action.context_click(msg_dialogs[0]).perform()
    context_menu = driver.find_elements(By.CSS_SELECTOR, '.controls-Menu__content-wrapper_width')
    assert context_menu[-1].text == 'Удалить'
    action.click(context_menu[-1]).perform()
    archive_notice = driver.find_element(By.CSS_SELECTOR, '[class="controls-Notification__content tw-flex-grow controls-Notification__content-spacing controls-Notification__content-padding"]')
    assert archive_notice.is_displayed()
    sleep(1)


finally:
    driver.quit()
