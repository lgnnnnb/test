from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as re


class test1:

    def __init__(self):

        self.wb = webdriver.Chrome()
        self.wb.get("http://dms-admin-test.ifyou.net/#/login")
        sleep(2)
        self.wb.find_element(By.XPATH, '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[1]/div/div/span/span/input').send_keys(18830059396)
        sleep(2)
        url = 'http://dms-test.ifyou.net/authCode'
        # paramas = {"account": "18611660290", "accountType": 1, "cerificationType": 2}
        paramas1 = {
            "account": "18830059396",
            "accountType": 1,
            "cerificationType": 2
        }
        headers = {"Content-type": "application/json;charset=UTF-8"}
        yzm = json.loads(re.post(url=url, json=paramas1, headers=headers).text)
        sleep(2)
        self.wb.find_element(By.XPATH,
                             '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[2]/div[1]/div/div/span/input').send_keys(
            yzm['data']['smsCode'])
        self.wb.find_element(By.XPATH,
                             '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/div/button').click()
        sleep(2)
        # self.wb.refresh()
        self.wb.get('http://dms-admin-test.ifyou.net/#/order3/YdCLZM?bid=YdCLZM')
        self.wb.maximize_window()
        sleep(3)
        # wb.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']/span[text()='新建']").click()
        self.wb.find_element(By.XPATH, "//div[@class='add-new']//button").click()
        sleep(5)

    def buttonclick(self, element, text):
        self.wb.find_element(By.XPATH, f"//input[@placeholder='{element}']").send_keys(text)
        sleep(2)
        self.wb.find_element(By.XPATH, '//*[@id="popContainer"]/div/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        sleep(2)
    def end_save(self):
        sleep(2)
        self.wb.find_element(By.XPATH,'//*[@id="popContainer"]/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
    def upload(self):
        self.wb.find_element(By.XPATH,'//*[@id="popContainer"]/div[2]/div/div[2]/div/div[2]/div[2]/div/form/div[6]/div[2]/div/div/div/div/div[2]/div/span/span/div[1]/span/button').send_keys("E:\1.txt")
    def buttenorselect1(self, element, text):
        if "2022" not in text:
            try:
                self.wb.find_element(By.XPATH, f"//input[@placeholder='{element}']").send_keys(text)
            except:
                if text == '是' or text == '否':
                    sleep(2)
                    WebDriverWait(self.wb, 5, 1).until(
                        EC.presence_of_element_located((By.XPATH, f"//div[text()='{element}']"))).click()
                    sleep(5)
                    # WebDriverWait(self.wb, 5, 1).until(
                    #     EC.presence_of_element_located((By.XPATH, f"//li[contains(text(),'{text}')]"))).click()
                    try:
                        self.wb.find_element(By.XPATH, f"//li[contains(text(),'{text}')]").click()
                        sleep(2)
                    except:
                        self.wb.find_elements(By.XPATH, '//li[@role="option"]')[2].click()
                else:
                    self.wb.find_element(By.XPATH, f"//textarea[@placeholder='{element}']").send_keys(text)


        elif "2022" in text and ":" in text:
            self.wb.find_element(By.XPATH, f"//input[@placeholder='{element}']").click()
            sleep(2)
            self.wb.find_element(By.CLASS_NAME, "ant-calendar-input ").send_keys(text)
            sleep(2)
            self.wb.find_element(By.LINK_TEXT, '确 定').click()
        elif ":" not in text:
            self.wb.find_element(By.XPATH, f"//input[@placeholder='{element}']").click()
            sleep(2)
            self.wb.find_element(By.CLASS_NAME, "ant-calendar-input ").send_keys(text)
            sleep(2)
            self.wb.find_element(By.LINK_TEXT, '今天').click()
