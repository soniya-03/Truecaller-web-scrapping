from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import time
from dotenv import load_dotenv
load_dotenv() 

FAIL_NEXT =(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div[2]/div[2]/div/div[2]/div/div/div/div/button/span')
EMAILFIELD = (By.XPATH,'//*[@id="identifierId"]')
PASSWORD = (By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
NEXTBUTTON = (By.XPATH,'//*[@id="identifierNext"]/div/button/span')
SEARCHBUTTON = (By.XPATH,"/html/body/div/div/main/div[2]/header/div/form/input")
BUTTON = (By.XPATH,"/html/body/div/div/main/div[2]/header/div/form/button")
BUTTON_AFTER_FIRST_SEARCH = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[1]/form/button")
NAME = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[2]/div/div/div[2]/header/div[1]/div[4]")
NAME2 = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[2]/div/div/div[2]/header/div[1]/div[3]")
AFTER_FIRST_SEARCH = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[1]/form/input")
ADDRESS = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[2]/div/div/div[2]/div[2]/a[2]/div/div[2]")

options = webdriver.ChromeOptions()
options.add_argument('--profile-directory=Person 1')
options.add_argument("--user-data-dir=C:/Users/lenovo/AppData/Local/Google/Chrome/User Data/Default") 
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get('https://www.truecaller.com/')
time.sleep(30)
# load_cookie(driver, 'path/to/cookie')
# driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
# driver.get("https://www.truecaller.com/")
# time.sleep(20)
# driver.get("""https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&respone_mode=query&redirect_uri=https%3A%2F%2Fwww.truecaller.com%2Fauth%2Fmicrosoft%2Fcallback&state=asia-south1%7Cin%7Cfalse%7Cweb%7Chttps%3A%2F%2Fwww.truecaller.com&client_id=000000004818BA61&scope=openid+profile+email+User.Read&sso_reload=true""")
# driver.get("""https://accounts.google.com/v3/signin/identifier?opparams=%253Frespone_mode%253Dquery&dsh=S-1207160665%3A1690988961897281&client_id=22378802832-klpcj5dosalhnu0vshg3hjm9qgidmp8j.apps.googleusercontent.com&o2v=2&redirect_uri=https%3A%2F%2Fasia-south1-truecaller-web.cloudfunctions.net%2Fapi%2Fnoneu%2Fauth%2Fgoogle%2Fv1&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcontacts.readonly&service=lso&state=asia-south1%7Cin%7Ctrue%7Cweb%7Chttps%3A%2F%2Fwww.truecaller.com&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAPATU4UcR9mejh2D4mleziUYOICOYw0w9E4lN_GCrPy01F4cyBHqOqc5cSxY_uFQNMrXro9TK11IiugtLasuB4WVQcATUzmRTPNn6fLnvL5PYwaOiXfAuaYoHVCEY19hV8CJlALMoXyejHsGTPuitNz0lMk00GnH1vQcutZv1ZQ9trFneo2h6V-UcaUJ7q0lziWmI__4I8N6QAwqC6s860TD0Mmcd17JhVJvuBG0m8OOovn27KWr2Q2tdQ9VqNvjUuk6jv6R7_mqdrcfD6hFs0U-db8gcoQQTaOTsEaY6WWnTVuPR2EosRD3oweKsiXKnBqO0MQ-25tmamlqtnJqXmpNR-IfZNeYdx0C0NKWuaaZseiYwckaVzt_QJFtyNVKRV0nFhYdnqJqDnk1Bre4SwSvsctZOw-ANKm8lanJ3plFQOleStINsP2H8s05TpCHbO4ER5DGYTV2GW8CnoelGsuKLHtN8asHS7ng3jYnYmEtgy2SlLy8ZV0QDw640VdspM5_olduvy56c2oswdnjSJNulVuqQ%26as%3DS-1207160665%253A1690988961897281%26client_id%3D22378802832-klpcj5dosalhnu0vshg3hjm9qgidmp8j.apps.googleusercontent.com%23&app_domain=https%3A%2F%2Fasia-south1-truecaller-web.cloudfunctions.net&rart=ANgoxcdBayUtlVsI8g3yiJAej6MkbfsD89YoQw4K33woD90_Ytx5Lt28JiukPKlEgda9ibQfgdvcIbNTzaQgBd_icgL9ofqYbpG2fLKCIXagWF_hK-XUg80""")
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(SIGNINBUTTON)).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(MICROSOFTBUTTON)).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(os.getenv("GMAIL_EMAIL", default=".env"))
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(FAIL_NEXT)).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(os.getenv("GMAIL_EMAIL", default=".env"))
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(PASSWORD)).send_keys(os.getenv("GMAIL_PASSWORD", default=".env"))
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
list=[8268291167,9867913757,8779278482]
for i in list:
    if(i==8268291167):
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(SEARCHBUTTON)).send_keys(i)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(BUTTON)).click()
        print(WebDriverWait(driver,20).until(EC.visibility_of_element_located(NAME)).text)
        try:
            print(WebDriverWait(driver,10).until(EC.visibility_of_element_located(ADDRESS)).text)
        except:
            pass
    if(i==9867913757):
        inp = WebDriverWait(driver,10).until(EC.element_to_be_clickable(AFTER_FIRST_SEARCH))
        inp.click()
        inp.send_keys(Keys.CONTROL + "a")
        inp.send_keys(Keys.DELETE)
        inp.send_keys(i)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(BUTTON_AFTER_FIRST_SEARCH)).click()
        # print(WebDriverWait(driver,20).until(EC.visibility_of_element_located(NAME)).text) 
        print(WebDriverWait(driver,10).until(EC.visibility_of_element_located(NAME2)).text)
        try:
            print(WebDriverWait(driver,10).until(EC.visibility_of_element_located(ADDRESS)).text)
        except:
            pass
    else:
        inp = WebDriverWait(driver,10).until(EC.element_to_be_clickable(AFTER_FIRST_SEARCH))
        inp.click()
        inp.send_keys(Keys.CONTROL + "a")
        inp.send_keys(Keys.DELETE)
        inp.send_keys(i)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(BUTTON_AFTER_FIRST_SEARCH)).click()
        # print(WebDriverWait(driver,20).until(EC.visibility_of_element_located(NAME)).text) 
        print(WebDriverWait(driver,10).until(EC.visibility_of_element_located(NAME2)).text)
        try:
            print(WebDriverWait(driver,10).until(EC.visibility_of_element_located(ADDRESS)).text)
        except:
            pass