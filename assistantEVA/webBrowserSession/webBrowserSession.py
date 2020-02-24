# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
import os

# Dictionary to convert str to int for switching tabs
nth = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4,
    'fifth': 5,
    'sixth': 6,
    'seventh': 7,
    'eighth': 8,
    'nineth': 9,
    'tenth': 10
}

class webBrowserSession():
    
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/7590/.wdm/drivers/chromedriver/79.0.3945.36/win32/chromedriver.exe')
        self.driver.get("http://www.google.com")
        self.driver.maximize_window()
        self.tabCount = 1
        
    def googleSearch(self, query):
        driver = self.driver
        driver.get("http://www.google.com")
        input_element = driver.find_element_by_name("q")
        input_element.send_keys(query)
        input_element.submit()
        
    def googleMapsNav(self, origin, destination):
        driver = self.driver
        google_map_url = 'https://www.google.com/maps/dir/' + origin + '/' + destination
        driver.get(google_map_url)
        
    def youtubeSearch(self, query):
        driver = self.driver
        driver.get("http://www.youtube.com")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search_query")))
        input_element = driver.find_element_by_name("search_query")
        input_element.send_keys(query)
        input_element.submit()
        
    # Function to click on links with specified targetText
    def clickOn(self, targetText):
        driver = self.driver
        xpath = "//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{0}')]".format(targetText)
        try:
            elem = driver.find_element_by_xpath(xpath)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            pass
    
    def makeNewTab(self):
        driver = self.driver
        driver.execute_script("window.open('');")
        self.tabCount += 1 # increase tabCount counter
        driver.switch_to.window(driver.window_handles[self.tabCount - 1])

        
    def closeCurrentTab(self):
        driver = self.driver
        driver.close()
        self.tabCount -= 1 # decrease tabCount counter
        driver.switch_to.window(driver.window_handles[self.tabCount - 1])
                
    def switchTab(self, tabNum):
        driver = self.driver
        try:
            tabNum = nth[tabNum]
        except KeyError:
            return 0
        
        if tabNum <= self.tabCount:
            driver.switch_to.window(driver.window_handles[tabNum - 1])
        else:
            pass
        
    def makeBookmark(self, path):
        driver = self.driver
        bookmark_url = driver.current_url
        f = open(os.path.join(path, 'bookmark.txt'), "w")
        f.write(bookmark_url)
        f.close()
        
    def openBookmark(self, path):
        driver = self.driver
        f = open(os.path.join(path, 'bookmark.txt'), "r")
        url = f.readline()
        f.close()  
        driver.get(url)
     
    def goForward(self):
        driver = self.driver
        # driver.forward()
        driver.execute_script("window.history.go(1)")
        
    def goBack(self):
        driver = self.driver
        # driver.back()
        driver.execute_script("window.history.go(-1)")
        
    def refreshPage(self):
        driver = self.driver
        driver.refresh()

    # --------------------------------------------------
    # For toggling between chapters at Mangakakalots.com
    # --------------------------------------------------
    def nextChapter(self):
        driver = self.driver
        elem = driver.find_element_by_css_selector('a.navi-change-chapter-btn-next')
        if elem:
            elem.click()
        else:
            pass
    
    def prevChapter(self):
        driver = self.driver
        elem = driver.find_element_by_css_selector('a.navi-change-chapter-btn-prev')
        if elem:
            elem.click()
        else:
            pass
          
    def quitSession(self):
        self.driver.quit()

# # FOR TESTING     
# if __name__ == "__main__":
#     browser = webBrowserSession()
#     browser.driver.get("http://www.youtube.com")
#     sleep(3)
#     browser.driver.get("http://www.reddit.com")
#     sleep(3)
#     browser.goBack()
#     sleep(3)
#     browser.goForward()
#     sleep(2)
#     browser.quitSession()
    