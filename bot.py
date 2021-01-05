#!/usr/bin/env python3

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  

#importing selenuim libraries 

# store the variables
url = 'http://timesink.be/quizbot/index.php'
path = '/home/ouranos/ctf/brixel/quizbot/chromedriver'  # change this to the chrome driver path 
driver = webdriver.Chrome(path)
driver.get(url)

# getting the url
num = 0
while num < 1000 :   # a loop for submitting junk and extracting the answers
    num = num + 1    # increase the number value to keep the loop going 
    searchbar = driver.find_element_by_xpath('//*[@id="insert_answer"]')   # associating the answer bar with a variable using xpath
    searchbar.send_keys("junk")                                            # just sending junk
    searchbar.send_keys(Keys.RETURN)                                        # move to the other question
    answer = driver.find_element_by_xpath('//*[@id="answer"]')              # associating the correct answer with a variable using xpath
    fd = open('answers.txt',"a+")                                           # opening a file in append mode to write values
    fd.write(str(answer.text) + "\n" )                                      # writing the values to the file 
    fd.close()                                                              #closing the file
