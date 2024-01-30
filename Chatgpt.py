from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from sympy import derive_by_array
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib

ScriptDir=pathlib.Path().absolute()
url = "https://flowgpt.com/chat"
chrome_option=Options()
user_agent="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_option.add_argument(f"user_agent={user_agent}")
chrome_option.add_argument('--profile-directory=Default')
chrome_option.add_argument(f'user-data-dir={ScriptDir}')
service=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option)
driver.maximize_window()
driver.get(url=url)
Chatnumber = 3
def Websiteopener():
    while True:
        try:
            xPATH = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea'
            driver.find_element(by=By.XPATH,value=xPATH)
            break
        except:
            pass
def SendMessage(Query):
    xPATH='/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea'
    driver.find_element(by=By.XPATH,value=xPATH).send_keys(Query)
    sleep(0.5)
    xPath2='/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button'
    driver.find_element(by=By.XPATH,value=xPath2).click()
def Resultscrapper():
    global Chatnumber
    Chatnumber=str(Chatnumber)
    xPath=f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{Chatnumber}]/div/div/div/div"
    Text = driver.find_element(by=By.XPATH,value=xPath).text
    ChatNumberNew=int(Chatnumber)+2
    Chatnumber=ChatNumberNew
#def Popupremover():
#    XPath='/html/body/div[3]/div[3]/div/section/button'
#    driver.find_element(by=By.XPATH,value=XPath).click()
#Popupremover()
Websiteopener()
while True:
    Query=input("Enter Query: ")
    SendMessage(Query=Query)
    sleep(3)
    Resultscrapper()