from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import os
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
import json

''' Setting up ENV Variables'''
load_dotenv()

load_dotenv(verbose=True)

from pathlib import Path  # Python 3.6+ only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



''' Call API From Airtable '''

header= {"Authorization": "Bearer " + "keynRNfKupAXaHbAO"}

response = requests.get("https://api.airtable.com/v0/appOJoA8DZDOHUgmd/Positions/", headers=header)
api_records=response.json()


'''Manageing the Data'''

data=api_records.values()
data=list(data)
data=data[0]
copy_data=data.copy()
for i in range(len(copy_data)):
    j=copy_data[i]
    j=j['fields']
    if '[Confirmation] Auto-posted' in j:
        data.remove(data[i])


'''Selenium automation For Cutshot Website'''

for i in range(len(data)):    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    browser.maximize_window()
    browser.get('https://cutshort.io/profile/employer-dashboard')


    action = ActionChains(browser)
    login_xpath = '//*[@class="t bold"]'
    login_click = browser.find_element_by_xpath(login_xpath)
    login_click.click()

    email_xpath = '//*[@ng-model="user_email"]'
    email_click = browser.find_element_by_xpath(email_xpath)
    email_click.send_keys('vhkvy73274@ulisaig.com')


    continue_click = '//*[@ng-click="checkLoginStatusOfEmail()"]'
    continue_button = browser.find_element_by_xpath(continue_click)
    continue_button.click()
    
    time.sleep(3)

    password_xpath = '//*[@type="password"]'
    password_click = browser.find_element_by_xpath(password_xpath)
    password_click.send_keys('Test@1234')

    login_xpath = '//*[@id="login_flow_container"]/div/div/div[3]/div/div/div[2]/div/div/div[4]/div/div[4]/div[2]/div[1]/div[1]'
    login_click = browser.find_element_by_xpath(login_xpath)
    login_click.click()
    time.sleep(5)

    job_post = '//*[@id="view_content"]/div/div/div[2]/div/div[4]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/a'
    if browser.find_element_by_xpath(job_post):
            post_a_job = browser.find_element_by_xpath(job_post)
            post_a_job.click()
    
    #driver.find_elements_by_link_text("Tutorials")
    time.sleep(5)
    login_xpath = '//*[@class="cat p5"]'
    login_click = browser.find_element_by_xpath(login_xpath)
    login_click.click()

    sel_category = '//*[@ng-model="input_value"]'
    sel_title=browser.find_element_by_xpath(sel_category)
    sel_title.send_keys(data[i]['fields']['Position Name'])
    sel_title.send_keys(Keys.ENTER)
    
    client_details=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[4]/div/div[2]/div[1]/globalradiobutton/div/div[1]/div/div')
    client_details.click()
    
    fintech=browser.find_element_by_xpath('//*[@id="addtnl"]')
    action.move_to_element(fintech).click().send_keys('fintech').perform()
    
    for j in data[i]['fields']['Desired Skills']:
        sel_skills = '//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[6]/div/div[1]/div[1]/inputwithtags/div/input'
        skills=browser.find_element_by_xpath(sel_skills)
        skills.send_keys(j)
        skills.send_keys(Keys.ENTER)

    location_type=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[7]/div/div[1]/div[1]/globalradiobutton/div/div[1]/div/div')
    location_type.click()



    w_location=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[8]/div/div[1]/inputwithtags/div/input')
    w_location.send_keys("Mumbai")
    w_location.send_keys(Keys.ENTER)

    w2_location=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[8]/div/div[1]/inputwithtags/div/input')
    w2_location.send_keys("Bangalore")
    w2_location.send_keys(Keys.ENTER)

    min_exp=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[11]/div/div/div[1]/input')
    min_exp.send_keys(data[i]['fields']['Desired Experience Minimum'])
    min_exp.send_keys(Keys.ENTER)

    max_exp=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[11]/div/div/div[3]/input')
    max_exp.send_keys(data[i]['fields']['Desired Experience Maximum'])
    max_exp.send_keys(Keys.ENTER)

    min_sal=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[15]/div/div[1]/div[2]/div/input')
    min_sal.send_keys(int(str(data[0]['fields']['Minimum Annual Budget']).strip("0")))
    min_sal.send_keys(Keys.ENTER)

    max_sal=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[15]/div/div[1]/div[4]/div/input')
    max_sal.send_keys(int(str(data[i]['fields']['Maximum Annual Budget']).strip("0")))
    max_sal.send_keys(Keys.ENTER)

    equity=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[21]/div/div[1]/div[1]/globalradiobutton/div/div[1]/div/div')
    equity.click()


    browser.execute_script("window.open('https://docs.google.com/document/d/1XoCLRKiO7lJNLF8a4z2PmCvbjYtJF4RNlkMpw5pFZe0/edit','new window')")
    handles = browser.window_handles
    time.sleep(2)
    browser.switch_to.window(handles[1])
    action = ActionChains(browser)
    action.key_down(Keys.CONTROL).send_keys("a").perform()
    action.key_down(Keys.CONTROL).send_keys("c").perform()
    time.sleep(2)

    browser.switch_to.window(handles[0])
    action = ActionChains(browser)
    job_desc = browser.find_element_by_xpath('//*[@id="mceu_12"]')
    action.click_and_hold(job_desc).perform()
    action.key_down(Keys.CONTROL).send_keys("v").perform()
    
    
    remove_tick=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[23]/div/div/globalcheckbox/div/div[1]/div')
    remove_tick.click()

    Addprefer=browser.find_element_by_xpath('//*[@id="create_signal_wrapper"]/div/div[2]/div[2]/div[25]/div/div[1]/div/span[2]')
    action.double_click(Addprefer).perform()
    
    time.sleep(3)

#     submit=browser.find_element_by_xpath('//*[@id="matches_workflow_wrapper"]/div[2]/div/div/div[8]/div/div[2]/div/div[2]/div[1]')
#     submit.click()
#     #W(browser,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="matches_workflow_wrapper"]/div[2]/div/div/div[8]/div/div[2]/div/div[2]/div[1]/span[2]'))).click()
    
#     W(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="setup_job_incoming_automation_container"]/div/div/div[3]/div/div/div[1]'))).click()

    browser.quit()
    
