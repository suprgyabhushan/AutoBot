from selenium import webdriver
import time
import getpass
import sys
import argparse

def getURLList(fileName_):
    fileHandle = open(fileName_)
    fileText = fileHandle.read();
    urlList = fileText.split('\n');
    urlList = filter(None, urlList); #Delete empty elements
    #print urlList;
    return urlList;

def login(url_, userName_, password_):
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    driver.get(url_)

    followButton = driver.find_elements_by_class_name("btn")[1]
    followButton.click()

    time.sleep(2)

    userNameField = driver.find_element_by_id("login_field")
    userNameField.send_keys(userName_)

    passwordField = driver.find_element_by_id("password")
    passwordField.send_keys(password_)

    signinButton = driver.find_elements_by_class_name("btn")[2]
    signinButton.click()

    time.sleep(2)
    return driver

def clickFollowButtons(driver_, url_):
    driver_.get(url_)

    followButtons = driver_.find_elements_by_css_selector(
        "button.btn.btn-sm.js-toggler-target[aria-label='Follow this person']")
    
    for x in range (0, len(followButtons)):
        if followButtons[x].is_displayed():
            followButtons[x].click()

def clickUnFollowButtons(driver_, url_):
    driver_.get(url_)

    unFollowButtons = driver_.find_elements_by_css_selector(
        ".btn.btn-sm.js-toggler-target.js-unfollow-button")

    print len(unFollowButtons);
    for x in range (0, len(unFollowButtons)):
        if unFollowButtons[x].is_displayed():
            unFollowButtons[x].click()

def clickStarButtons(driver_, url_):
	driver_.get(url_)

	starButtons = driver_.find_elements_by_css_selector(
		"button.btn.btn-sm.btn-with-count.js-toggler-target")
	
	for x in range (0, len(starButtons)):
		if starButtons[x].is_displayed():
			starButtons[x].click()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--unfollow', 
                        action='store_true',
                        help='unfollow flag')

    parser.add_argument('--star',
				action='store_true',
				help='star sign')

    parser.add_argument('--user', 
                        required=True,
                        help='github username')

    parser.add_argument('--file', 
                        required=True,
                        help='github url list')    

    args = parser.parse_args()
    userName = args.user
    urlList = getURLList(args.file)
    
    password = getpass.getpass("Password: ")
    
    driver = login(urlList[0], userName, password)

    if args.star:
        for x in range (0, len(urlList)):
            clickStarButtons(driver, urlList[x])
    else:
        for x in range (0, len(urlList)):
            clickFollowButtons(driver, urlList[x])

if __name__ == "__main__": main()
