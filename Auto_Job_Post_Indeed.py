#RPA for Indeed

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pickle
import time



browser = webdriver.Chrome(
        executable_path = 'C:/chromedriver/chromedriver')
browser.maximize_window()
browser.get('https://www.indeed.com/hire')
cookies = pickle.load(open("K:/Ajackus/Auto_Job_Post/ats-rpa/cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
browser.get('https://www.indeed.com/hire')


time.sleep(3)

browser.find_element_by_xpath('//*[@id="hireHeroPostJobButton"]').click()

time.sleep(5)

job_title_xpath = '//*[@id="JobTitle"]'
job_title_click = browser.find_element_by_xpath(job_title_xpath)
job_title_click.send_keys("Python Developer");

time.sleep(2)

loc_xpath = '//*[@id="cityOrPostalCode"]'
loc_xpath_click = browser.find_element_by_xpath(loc_xpath)
loc_xpath_click.send_keys("Mumbai");

hires_xpath = '//*[@id="IntHiresNeeded_Stepper-1"]'
hires_click = browser.find_element_by_xpath(hires_xpath)
hires_click.send_keys("2");

next_xpath = '//*[@id="sheet-next-button"]/span/a'
browser.find_element_by_xpath(next_xpath).click()

time.sleep(5)

#name_xpath = '//*[@id="AdvertiserName"]'
#browser.find_element_by_xpath(name_xpath).send_keys("Demo")

#no_xpath ='//*[@id="AdvertiserPhoneNumber"]'
#browser.find_element_by_xpath(no_xpath).send_keys("919820197170")

#next_click = '//*[@id="sheet-next-button"]/span/a'
#browser.find_element_by_xpath(next_click).click()

#time.sleep(5)


sel_emp_type = Select(browser.find_element_by_xpath('//*[@id="ifl-SelectFormField-6"]'))
sel_emp_type.select_by_visible_text("Full-time")

schedule_xpath = '//*[@id="plugin_container_TaxonomyScheduleCustomClassAttributesContainer"]/div/div/div/div/div/div/div/fieldset/div[2]/label[7]/div[1]'
browser.find_element_by_xpath(schedule_xpath).click()



salary_min_xpath = '//*[@id="JobSalary1"]'
browser.find_element_by_xpath(salary_min_xpath).send_keys(Keys.CONTROL + "a")
browser.find_element_by_xpath(salary_min_xpath).send_keys(Keys.DELETE)
browser.find_element_by_xpath(salary_min_xpath).send_keys("500,000")

time.sleep(5)


salary_max_xpath = '//*[@id="JobSalary2"]'
browser.find_element_by_xpath(salary_max_xpath).send_keys(Keys.CONTROL + "a")
browser.find_element_by_xpath(salary_max_xpath).send_keys(Keys.DELETE)
browser.find_element_by_xpath(salary_max_xpath).send_keys("600,000")

time.sleep(5)

benefits_1 = '//*[@id="plugin_container_TaxonomyBenefitsCustomClassAttributesContainer"]/div/div/div/div/div/div/div/fieldset/div[2]/label[3]/div[2]'
browser.find_element_by_xpath(benefits_1).click()

benefits_2 = '//*[@id="plugin_container_TaxonomyBenefitsCustomClassAttributesContainer"]/div/div/div/div/div/div/div/fieldset/div[2]/label[10]/div[2]'
browser.find_element_by_xpath(benefits_2).click()

resume_submit = '//*[@id="ApplicationEmailResumeRequirement"]/fieldset/label[3]/div[2]'
browser.find_element_by_xpath(resume_submit).click()

job_desc_area = '//*[@id="AppendedJobDescription-editor-content"]'
browser.find_element_by_xpath(job_desc_area).send_keys('Proficient in Python Language,Minimum 2-3 years of Experience')

nxt = '//*[@id="sheet-next-button"]/span/a'
browser.find_element_by_xpath(nxt).click()

#time.sleep(2)


#agree = '//*[@id="plugin-smbcommunication-EmployerAssistLegalModal-modal_box_content"]/div/div/div/div/div/div[2]/div/button[1]'
#browser.find_element_by_xpath(agree).click()

time.sleep(5)

off_xpath = '//*[@id="QualificationsVisibility"]/div[1]/div[2]/div/label/div[2]'
browser.find_element_by_xpath(off_xpath).click()


off_2_xpath = '//*[@id="SkillsAssessmentVisibility"]/div[1]/div[2]/div/label/div[2]'
browser.find_element_by_xpath(off_2_xpath).click()

nxt_xpath = '//*[@id="sheet-next-button"]/span/a'
browser.find_element_by_xpath(nxt_xpath).click()

time.sleep(5)


final_cont = '//*[@id="sheet-next-button"]/span/a'
browser.find_element_by_xpath(final_cont).click()

time.sleep(5)

#dnt_optimize = '//*[@id="uniqueId1"]'
#browser.find_element_by_xpath(dnt_optimize).click()
