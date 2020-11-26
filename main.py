from selenium import webdriver
from time import sleep
from secrets import pw

class SnkrBot:
    def __init__(self,username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.nike.com/launch")
        sleep(2)
        # Login In Button based on Full xPath Address using Inspect
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/header/div[1]/section/ul/li[1]/button")\
            .click()
        sleep(2)
        # Add Email based on the name attribute
        self.driver.find_element_by_xpath("//input[@name=\"emailAddress\"]")\
            .send_keys(username)
        # Add Email based on the name attribute
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        sleep(1)
        # Press Submit Button based on type attribute
        self.driver.find_element_by_xpath("//input[@type=\"button\"]")\
            .click()
        sleep(4)
        # Press 'In Stock' based on Full xPath Address using Inspect
        # self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/div[1]/header/div/div/div/div/div[2]/div/nav/ul/li[3]/a/div")\
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/div[1]/header/div/div/div/div[1]/div[2]/div/nav/ul/li[2]/a/div")\
            .click()
        sleep(3)
        # Choose Shoe based on the name in Alt attribute
        self.driver.find_element_by_xpath("//img[@alt=\"Space Hippie 02 - Volt 'This is Trash' Release Date\"]")\
            .click()
        sleep(1)
        # Choose Shoe based on the name in class attribute and the text being the size I want
        self.driver.find_element_by_xpath("//button[@class='size-grid-dropdown size-grid-button' and contains(., 'M 9 / W 10.5')]")\
            .click()
        sleep(3)
        # Choose Shoe based on the name in class attribute and the text 'Add to Cart'
        self.driver.find_element_by_xpath("//button[@class='ncss-brand ncss-btn-black pb3-sm prl5-sm pt3-sm u-uppercase u-full-width' and contains(., 'BUY $150')]")\
            .click()   
        sleep(4)

SnkrBot('grxxpe@gmail.com',pw)