from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time
import schedule 
import pywhatkit
import os
from threading import Timer
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import notification
PATH = "H:\Python\chromedriver.exe"

driver = webdriver.Chrome(PATH)
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

# All about driver code and all the stuff 
driver.get('https://classroom.google.com/u/3/h')





    # pywhatkit.sendwhatmsg(number,"class is joined",curr_hour,curren_min+1)
# number = input("Enter your number so that bot can send message to your whatsapp: ")
# joins the class 
'''working properly'''
def joining():
    time.sleep(10)
    to_switch = driver.window_handles[1] 
    driver.switch_to.window(to_switch)
    # driver.find_element_by_xpath('//*[@id="ow45"]/div/div').click()
    # time.sleep(2)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()
    time.sleep(10)
    



## join the english class
'''working'''
def english():
    driver.implicitly_wait(6)

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[4]/div[1]/div[3]/h2/a[1]/div[1]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div').click()
    driver.implicitly_wait(20)
    joining()
    notification.notify_me()

## join the hindi class
'''working'''
def hindi():
    driver.implicitly_wait(6)

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[6]/div[1]/div[3]/h2/a[1]/div[1]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div').click()
    driver.implicitly_wait(20)
    joining()
## joins maths class
'''working'''
def maths():
    driver.implicitly_wait(6)

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div').click()
    driver.implicitly_wait(20)
    joining()

## joins chem_bio class
'''working'''
def chem_bio():
    driver.implicitly_wait(6)

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div').click()
    driver.implicitly_wait(20)
    joining()

## joins physics class
'''working'''
def physics():
    driver.implicitly_wait(6)

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[2]/div[1]/div[3]/h2/a[1]/div[1]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div').click()
    driver.implicitly_wait(20)
    joining()

## joins sst class
'''working'''
def sst():
    driver.implicitly_wait(6)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[5]/div[1]/div[3]/h2/a[1]/div[1]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div').click()
    driver.implicitly_wait(20)
    joining()
## login too chrome with my account 
'''working'''
def login():
    driver.find_element_by_name('identifier').send_keys("")
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    driver.implicitly_wait(2)
    driver.find_element_by_name('password').send_keys("")
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

'''Declaring day'''
e= datetime.datetime.now()
day = (e.strftime("%a"))






  
'''main function!!!!!'''
if __name__ == "__main__":  
    # sign in to the chrome   
    if 'Sign' in driver.title: 
        login()
    # opens  the classes accoring to the timetable 
    # time table for monday 
    if day == "Mon":
        schedule.every().monday.at("09:52").do(maths)
        schedule.every().monday.at("10:59").do(english)
            
        
        schedule.every().monday.at("12:40").do(chem_bio)
    # time table for tuesday
    elif day == "Tue":
        schedule.every().tuesday.at("9:10").do(maths)
        schedule.every().tuesday.at("10:59").do(english)
        schedule.every().tuesday.at("12:40").do(chem_bio)           

    
    # time table for wednesday
    elif day == "Wed":
        schedule.every().wednesday.at("9:10").do(maths)
        schedule.every().wednesday.at("10:59").do(chem_bio)
        schedule.every().wednesday.at("12:40").do(maths)
    # time table for thursday
    elif day == "Thu":

        schedule.every().thursday.at("9:10").do(sst)
        schedule.every().thursday.at("10:59").do(chem_bio)
        schedule.every().thursday.at("12:40").do(sst)       
        
    # time table for friday
    elif day == "Fri":
        
        schedule.every().friday.at("9:10").do(hindi)
        schedule.every().friday.at("10:59").do(physics)
        schedule.every().friday.at("12:40").do(sst)
    # time table for saturday    
    else:

        schedule.every().saturday.at("09:10").do(sst)
        schedule.every().saturday.at("11:40").do(physics)
        schedule.every().saturday.at("12:40").do(hindi)
    while True:
        schedule.run_pending()
        time.sleep(1)
