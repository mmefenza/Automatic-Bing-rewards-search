# -*- coding: utf-8 -*-
##############################################
# Written by Michael Mefenza
#
################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from datetime import datetime, timedelta
import time
import requests

today_date = datetime.now().strftime("%d.%m.%Y")
file_object = open("lastchecked.txt", "r") 
lastchecked_date = file_object.readline()
file_object.close()


print today_date
print lastchecked_date 

if today_date ==  lastchecked_date:
    print "You have already used the script today"
else:
    file_object = open("lastchecked.txt", "w")
    file_object.write(today_date)
    file_object.close()

    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()


    ##PC search
    driver = webdriver.Firefox()
    ##logout
    driver.get("https://www.bing.com/rewards/signout")
    driver.implicitly_wait(3)
    time.sleep(3)


    ##login
    driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1441086351&rver=6.0.5286.0&wp=MBI&wreply=https:%2F%2Fwww.bing.com%2Fsecure%2FPassport.aspx%3Frequrl%3Dhttps%253a%252f%252fwww.bing.com%252frewards%252fdashboard%253fwlexpsignin%253d1&lc=1033&id=264960")
    elem = driver.find_element_by_name("loginfmt")
    elem.send_keys("username")
    elem = driver.find_element_by_name("passwd")
    elem.send_keys("password")
    login_button = driver.find_element_by_xpath('//div[contains(@class,"section")]//input[@name="SI"]')
    login_button.click()
    driver.implicitly_wait(3)
    time.sleep(3)


    ##reward page
    driver.get("https://www.bing.com/rewards/dashboard")
    driver.implicitly_wait(3)
    time.sleep(3)
    driver.refresh();
    
    driver.get("https://www.bing.com/search?q=top+stories&filters=segment:%22popularnow.carousel%22+scenario:%22carousel%22&FORM=ML11Z9&CREA=ML11Z9&rnoreward=1")
    driver.implicitly_wait(1)
    time.sleep(1)
    currentgain = driver.find_element_by_xpath('//span[@id="id_rc"]').text
    print currentgain
    newgain = driver.find_element_by_xpath('//span[@id="id_rc"]').text
    while int(newgain) - int(currentgain) < 15:
        elem = driver.find_element_by_name("q")
        driver.execute_script("document.getElementById('sb_form_q').setAttribute('value', '')");
        elem.send_keys(random.choice(WORDS))
        search_button = driver.find_element_by_xpath('//input[@name="go"]')
        search_button.click()
        driver.implicitly_wait(1)
        time.sleep(1)
        newgain = driver.find_element_by_xpath('//span[@id="id_rc"]').text

    print "PC search done"
    driver.close()


    ##mobile search
    ##use https://addons.mozilla.org/en-US/firefox/addon/user-agent-overrider/ to transform firefox into android
    ## set browser to android version
    #driver.get("about:config  general.useragent.override 'Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0'")

    profile = webdriver.FirefoxProfile();
    profile.add_extension(extension='user_agent_overrider.xpi')
    profile.set_preference("extensions.useragentoverrider.activated", True);
    profile.set_preference("extensions.useragentoverrider.currentLabel", "Android / Firefox 29");
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0");

    driver1=  webdriver.Firefox(firefox_profile=profile);
    driver1.implicitly_wait(3)
    time.sleep(3)

    #logout
    driver1.get("https://www.bing.com/rewards/signout")
    driver1.implicitly_wait(3)
    time.sleep(3)

    #login
    driver1.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1441086351&rver=6.0.5286.0&wp=MBI&wreply=https:%2F%2Fwww.bing.com%2Fsecure%2FPassport.aspx%3Frequrl%3Dhttps%253a%252f%252fwww.bing.com%252frewards%252fdashboard%253fwlexpsignin%253d1&lc=1033&id=264960")
    try:
        elem = driver1.find_element_by_name("loginfmt")
        elem.send_keys("username")
        elem = driver1.find_element_by_name("passwd")
        elem.send_keys("password")
        login_button = driver1.find_element_by_xpath('//div[contains(@class,"section")]//input[@class="default"]')
        login_button.click()
        driver1.implicitly_wait(3)
        time.sleep(3)
    except:
        pass
    
    driver1.refresh();
    driver1.get("https://www.bing.com/search?q=Popular%20now%20on%20Bing&filters=segment:%22popularnow.carousel%22&FORM=ML10NS&CREA=ML10NS")
    driver1.implicitly_wait(1)
    time.sleep(1)
    currentgain = driver1.find_element_by_xpath('//span[@id="id_rc"]').text
    print currentgain
    newgain = driver1.find_element_by_xpath('//span[@id="id_rc"]').text
    while int(newgain) - int(currentgain) < 10:
        elem = driver1.find_element_by_name("q")
        driver1.execute_script("document.getElementById('sb_form_q').setAttribute('value', '')");
        elem.send_keys(random.choice(WORDS))
        search_button = driver1.find_element_by_xpath('//input[@name="go"]')
        search_button.click()
        driver1.implicitly_wait(1)
        time.sleep(1)
        newgain = driver1.find_element_by_xpath('//span[@id="id_rc"]').text

    print "Mobile search done"

    # set browser to Desktop version
    #driver.get("about:config pref set general.useragent.override 'Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0'")
    profile.set_preference("extensions.useragentoverrider.activated", True);
    profile.set_preference("extensions.useragentoverrider.currentLabel", "Linux / Firefox 29");
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0");

    driver1.close()   

