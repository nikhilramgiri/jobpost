from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import json
import pickle

header= {"Authorization": "Bearer " + "keynRNfKupAXaHbAO"}
response = requests.get("https://api.airtable.com/v0/appOJoA8DZDOHUgmd/Positions/", headers=header)
api_records=response.json()
data=api_records.values()
data=list(data)
data=data[0]
copy_data=data.copy()
for i in range(len(copy_data)):
    j=copy_data[i]
    j=j['fields']
    if '[Confirmation] Auto-posted' in j:
        data.remove(data[i])


for i in range(len(data)):
    browser = webdriver.Chrome(
            executable_path = 'C:/chromedriver/chromedriver')
    browser.maximize_window()
    browser.get('https://www.indeed.com/hire')
    cookies = pickle.load(open("K:/Ajackus/Auto_Job_Post/ats-rpa/cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get('https://www.indeed.com/hire')
    action = ActionChains(browser)


    time.sleep(3)

    browser.find_element_by_xpath('//*[@id="hireHeroPostJobButton"]').click()

    time.sleep(5)

    indeed_job_title_xpath = '//*[@id="JobTitle"]'
    indeed_job_title_click = browser.find_element_by_xpath(indeed_job_title_xpath)
    indeed_job_title_click.send_keys(data[i]['fields']['Position Name']);

    time.sleep(2)

    indeed_loc_xpath = '//*[@id="cityOrPostalCode"]'
    indeed_loc_xpath_click = browser.find_element_by_xpath(indeed_loc_xpath)
    indeed_loc_xpath_click.send_keys("Mumbai");

    indeed_hires_xpath = '//*[@id="IntHiresNeeded_Stepper-1"]'
    indeed_hires_click = browser.find_element_by_xpath(indeed_hires_xpath)
    indeed_hires_click.send_keys(data[i]['fields']['Positions Open']);

    indeed_next_xpath = '//*[@id="sheet-next-button"]/span/a'
    browser.find_element_by_xpath(indeed_next_xpath).click()

    time.sleep(5)

    indeed_sel_emp_type = Select(browser.find_element_by_xpath('//*[@id="ifl-SelectFormField-7"]'))
    indeed_sel_emp_type.select_by_visible_text("Full-time")

    indeed_schedule_xpath = '//*[@id="plugin_container_TaxonomyScheduleCustomClassAttributesContainer"]/div/div/div/div/div/div/fieldset/div[2]/label[7]/div[1]'
    browser.find_element_by_xpath(indeed_schedule_xpath).click()


    time.sleep(2)
    indeed_salary_min_xpath = '//*[@id="JobSalary1"]'
    browser.find_element_by_xpath(indeed_salary_min_xpath).send_keys(Keys.CONTROL + "a")

    time.sleep(2)

    browser.find_element_by_xpath(indeed_salary_min_xpath).send_keys(Keys.DELETE)
    time.sleep(2)

    browser.find_element_by_xpath(indeed_salary_min_xpath).send_keys(data[i]['fields']['Minimum Annual Budget'])

    time.sleep(2)

    indeed_salary_max_xpath = '//*[@id="JobSalary2"]'
    browser.find_element_by_xpath(indeed_salary_max_xpath).send_keys(Keys.CONTROL + "a")
    browser.find_element_by_xpath(indeed_salary_max_xpath).send_keys(Keys.DELETE)
    browser.find_element_by_xpath(indeed_salary_max_xpath).send_keys(data[i]['fields']['Maximum Annual Budget'])

    time.sleep(2)

    indeed_resume_submit = '//*[@id="ApplicationEmailResumeRequirement"]/fieldset/label[3]/div[2]'
    browser.find_element_by_xpath(indeed_resume_submit).click()


    browser.execute_script("window.open('https://docs.google.com/document/d/1XoCLRKiO7lJNLF8a4z2PmCvbjYtJF4RNlkMpw5pFZe0/edit','new window')")

    handles = browser.window_handles

    browser.switch_to.window(handles[1])


    action = ActionChains(browser)
    action.key_down(Keys.CONTROL).send_keys("a").perform()
    action.key_down(Keys.CONTROL).send_keys("c").perform()

    time.sleep(2)

    browser.close()

    browser.switch_to.window(handles[0])

    time.sleep(2)

    action = ActionChains(browser)
    indeed_job_desc = browser.find_element_by_xpath('//*[@id="AppendedJobDescription-editor-content"]')
    action.click_and_hold(indeed_job_desc).perform()
    action.key_down(Keys.CONTROL).send_keys("v").perform()

    indeed_nxt = '//*[@id="sheet-next-button"]/span/a'
    browser.find_element_by_xpath(indeed_nxt).click()

    time.sleep(10)

    
    W(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="QualificationsVisibility"]/div[1]/div[2]/div/label/div[2]/div/div[2]'))).click()


    
    W(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SkillsAssessmentVisibility"]/div[1]/div[2]/div/label/div[2]'))).click()

    time.sleep(2)

    indeed_nxt_xpath = '//*[@id="sheet-next-button"]/span/a'
    browser.find_element_by_xpath(indeed_nxt_xpath).click()

    time.sleep(5)

    indeed_final_cont = '//*[@id="sheet-next-button"]/span/a'
    browser.find_element_by_xpath(indeed_final_cont).click()

    time.sleep(5)



    W(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniqueId1"]'))).click()

    time.sleep(5)

    browser.close()

print("Indeed Auto-Post Done Successfully")