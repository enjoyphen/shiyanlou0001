import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.get('https://www.shiyanlou.com/courses/427')
actions = ActionChains(driver)
elme = driver.find_element_by_css_selector('li.next-page')
items = []
page = 1
while elme:
    for i in range(1,11):
        item = {}
        nameSelector = 'div[class~=text-center]:nth-child({}) a.username'.format(i)
        commentSelector = 'div[class~=text-center]:nth-child({}) div[class~=markdown-box]'.format(i)
        err = True
        while err:
            try:
                item['username'] = driver.find_element_by_css_selector(nameSelector).text
                item['content'] =  driver.find_element_by_css_selector(commentSelector).text
                err = False
            except TypeError:
                pass
                print('error extract item') 
        items.append(item)

        print(item['content'])
    try:
        elme = driver.find_element_by_css_selector('li[class="disabled next-page"]')
        print(elme.text)
        if page != 4:
            raise NoSuchElementException
        elme = None
        print('sss')
    except NoSuchElementException:
        elme = driver.find_element_by_css_selector('li.next-page')
        actions.move_to_element(elme)
        actions.click(elme)
        actions.perform()
        wait = WebDriverWait(driver, 10)
        page += 1
        wait.until(EC.text_to_be_present_in_element((By.XPATH,'//ul[@class="pagination"]/li[@class="active"]'),str(page) )) 
print('follow close')
driver.close()
with open('/home/shiyanlou/comments.json','w') as f:
    f.write(json.dumps(items))
