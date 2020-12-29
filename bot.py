#!/usr/bin/env python3

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# stock the variables
url = 'http://timesink.be/quizbot/index.php'
path = '/home/ouranos/ctf/brixel/quizbot/chromedriver'
driver = webdriver.Chrome(path)

# getting the url
num = 0
while num < 1000 :
    num = num + 1
    driver.get(url)
    searchbar = driver.find_element_by_xpath('//*[@id="insert_answer"]')
    searchbar.send_keys("junk")
    searchbar.send_keys(Keys.RETURN)
    answer = driver.find_element_by_xpath('//*[@id="answer"]')
    fd = open('answers.txt',"a+")
    fd.write(str(answer.text) + "\n" )
    fd.close()
