from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import random
import time

proxies = {
    "http": "http://brd-customer-hl_ba670e89-zone-web_unlocker1:40vkf5q6os1m@brd.superproxy.io:22225",
    "https": "https://brd-customer-hl_ba670e89-zone-web_unlocker1:40vkf5q6os1m@brd.superproxy.io:22225"
}
ua = UserAgent()
userAgent = ua.random
options = Options()
# options.add_argument("--headless")  # Enable headless mode
options.add_argument("--disable-gpu")  # Disabling GPU acceleration (sometimes necessary)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(f'user-agent={userAgent}')
srv=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=srv, seleniumwire_options={'proxy': proxies}, options=options)

try:
    # Open Amazon login page
    login_url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dmy%2Baccount%2Bwith%2Bamazon%2Bsign%2Bin%26hvadid%3D397159913882%26hvdev%3Dc%26hvlocphy%3D1013962%26hvnetw%3Dg%26hvqmt%3De%26hvrand%3D626471453090633138%26hvtargid%3Dkwd-843559735172%26hydadcr%3D7442_9611317%26tag%3Dgooghydr-20%26ref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    driver.get(login_url)

    # Wait for the page to load
    time.sleep(random.uniform(2, 5))

    # Find the email input field and enter your email
    email_field = driver.find_element(By.ID, "ap_email")
    email_field.send_keys("+1 212 555 1212")

    # Wait for a random time
    time.sleep(random.uniform(2, 5))

    # Find and click the "Continue" button
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # Wait for the next page to load
    time.sleep(random.uniform(2, 5))

finally:
    # Close the WebDriver
    driver.quit()


