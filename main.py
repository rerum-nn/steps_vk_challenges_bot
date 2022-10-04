from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from config import vk_login, vk_password, victim, names_for_challenges, path

options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(executable_path=path, options=options)

try:
    driver.get("https://id.vk.com/auth?v=1.32.0&app_id=7913379&uuid=3ff886be73&redirect_uri=https%3A%2F%2Fvk.com%2Ffeed&app_settings=W10%3D&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInRva2VuIjoiIiwicGFyYW1zIjp7InR5cGUiOiJzaWduX2luIn19&scheme=bright_light")

    sleep(5)
except:
    print("У вас отсутствует подключение к интернету")
    driver.close()
    driver.quit()
    exit(-1)

try:
    login_input = driver.find_element(By.CLASS_NAME, "vkc__TextField__input")
    login_input.clear()
    login_input.send_keys(vk_login)
    login_input.send_keys(Keys.ENTER)
    sleep(3)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(vk_password)
    password_input.send_keys(Keys.ENTER)
except Exception as ex:
    print("Невозможно авторизоваться, что то поменялось")
    print(ex)
    driver.close()
    driver.quit()
    exit(-1)

sleep(20)

try:
    driver.get("https://vk.com/steps")
    steps = driver.find_element(By.XPATH, '//iframe[@webkitallowfullscreen="true"]')
    sleep(10)

    driver.switch_to.frame(steps)

    for name in names_for_challenges:
        challenges = driver.find_element(By.CLASS_NAME, 'vkuiGallery__viewport')
        make_a_challenge_button = driver.find_element(By.CLASS_NAME, "ChallengesMinified__friendsAction")

        driver.execute_script("arguments[0].scrollIntoView(true);", challenges)

        while not make_a_challenge_button.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView(true);", challenges)
            ActionChains(driver) \
                .drag_and_drop_by_offset(challenges, -100, 0)\
                .perform()
            sleep(1)
        sleep(2)

        make_a_challenge_button.click()
        sleep(5)

        name_input = driver.find_element(By.XPATH, '//*[@id="panel_challenge_editor"]/div/form/div/div[1]/div/input')
        name_input.clear()
        name_input.send_keys(name)

        amount_of_steps_enter = driver.find_element(By.XPATH, '//*[@id="panel_challenge_editor"]/div/form/div/div[3]/div[1]/div/input')
        amount_of_steps_enter.clear()
        amount_of_steps_enter.send_keys("500")

        # invite_friends_checkbox = driver.find_element(By.XPATH, '//*[@id="panel_challenge_editor"]/div/form/div/div[6]/div[1]/div[1]/div[2]')
        # invite_friends_checkbox.click()
        #
        # events_push_checkbox = driver.find_element(By.XPATH, '//*[@id="panel_challenge_editor"]/div/form/div/div[6]/div[1]/div[2]/div[2]')
        # events_push_checkbox.click()

        add_members_button = driver.find_element(By.CLASS_NAME, 'ChallengeEditor__add')
        driver.execute_script("arguments[0].scrollIntoView(true);", add_members_button)
        add_members_button.click()
        sleep(5)

        search_members_input = driver.find_element(By.XPATH, '//*[@id="modal_base_select_friends"]/div/div/div[2]/div/div/div[1]/div/label/input')
        search_members_input.clear()
        search_members_input.send_keys(victim)
        sleep(3)

        member_checkbox = driver.find_element(By.XPATH, '//*[@id="modal_base_select_friends"]/div/div/div[2]/div/div/div[2]/div/div[3]')
        driver.execute_script("arguments[0].scrollIntoView(true);", member_checkbox)
        member_checkbox.click()
        sleep(1)

        ready_button = driver.find_element(By.XPATH, '//*[@id="modal_base_select_friends"]/div/div/div[2]/div/div/div[4]/div/div/button')
        driver.execute_script("arguments[0].scrollIntoView(true);", ready_button)
        ready_button.click()
        sleep(1)

        send_challenge = driver.find_element(By.XPATH, '//*[@id="panel_challenge_editor"]/div/div[4]/div/div/button')
        driver.execute_script("arguments[0].scrollIntoView(true);", send_challenge)
        send_challenge.click()
        sleep(2)

        back_button = driver.find_element(By.XPATH, '//*[@id="panel_challenge"]/div/div[2]/div/div/div/div[1]/button[2]')
        driver.execute_script("arguments[0].scrollIntoView(true);", back_button)
        back_button.click()

        sleep(2)


except Exception as ex:
    print("Ошибка в приложении шаги")
    print(ex)
finally:
    driver.close()
    driver.quit()
    exit(-1)

print("Все успешно отработало")

