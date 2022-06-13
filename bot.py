#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By

url = 'http://timesink.be/quizbot/index.php'
path = '/home/ouranos/ctf/brixel/quizbot/chromedriver'  # change this to the chrome driver path
driver = webdriver.Chrome(path)
driver.get(url)

# getting the url
num = 0
while num < 1000 :   # a loop for submitting junk and extracting the answers
    num = num + 1
    searchbar = driver.find_element(By.XPATH, '//*[@id="insert_answer"]')
    searchbar.send_keys("junk")
    searchbar.send_keys(Keys.RETURN)
    answer = driver.find_element(By.XPATH ,'//*[@id="answer"]').text
    with open('answers.txt',"a+") as f:
        f.write(str(answer) + "\n")
