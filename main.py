from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"

# Chrome driver setup
browser_driver = Service('/usr/bin/chromedriver')

# Start the browser
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/login/index.php")
    time.sleep(2)

    page_to_scrape.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/a").click()
    time.sleep(2)

    mail = page_to_scrape.find_element(By.XPATH, '//*[@id="i0116"]')
    mail.send_keys(os.environ['MAIL'])  
    page_to_scrape.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(2)   

    password = page_to_scrape.find_element(By.XPATH, '//*[@id="i0118"]')
    password.send_keys(os.environ['PASSWORD'])  
    page_to_scrape.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(2)

    page_to_scrape.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
    time.sleep(2)

    # bp

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=4&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2025&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(3)
    
    responseBP = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')
    novosti_markdown = responseBP.text

    with open("bp.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

    heightBP = responseBP.size['height']
    widthBP = responseBP.size['width']
    desired_widthBP = max(widthBP, 1200)  
    desired_heightBP = min(heightBP, 1000)
    page_to_scrape.set_window_size(desired_widthBP, desired_heightBP)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", responseBP)
    responseBP.screenshot('bp.png')

    # oop

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=45&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=9&fromyear=2024&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(3)
    
    responseOOP = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')
    novosti_markdown = responseOOP.text

    with open("oop.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

    heightOOP = responseOOP.size['height']
    widthOOP = responseOOP.size['width']
    desired_widthOOP = max(widthOOP, 1200)  
    desired_heightOOP = min(heightOOP, 1000)
    page_to_scrape.set_window_size(desired_widthOOP, desired_heightOOP)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", responseOOP)
    responseOOP.screenshot('oop.png')







finally:
    # Close the browser
    page_to_scrape.quit()
