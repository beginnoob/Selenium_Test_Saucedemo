from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")

# element = driver.find_element(By.ID, "user-name")
# element.send_keys("standard_user")

# element = driver.find_element(By.ID, "password")
# element.send_keys("secret_sauce")

# element = driver.find_element(By.ID, "login-button")
# element.click()


def setup_driver():
    options = webdriver.ChromeOptions()
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False  # ⬅️ penting!
    }
    
    options.add_experimental_option("prefs", prefs)

    # disable infobars & automation flags
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    
    return driver

def open_website(driver, url):
    driver.get(url)
    time.sleep(2)

def login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
def verify_login(driver):
    try:
        title = driver.find_element(By.CLASS_NAME, "title").text
        if title == "Products":
            print("Login Success ✅")
        else:
            print("Login Failed ❌")
    except:
        print("Element not found ❌")

def open_sidebar(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click()

def logout(driver):
    wait = WebDriverWait(driver, 10)
    
    # tunggu tombol logout muncul
    logout_btn = wait.until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
    )
    
    logout_btn.click()

def verify_logout(driver):
    wait = WebDriverWait(driver, 10)
    
    login_btn = wait.until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    
    assert login_btn.is_displayed(), "Logout Failed ❌"
    print("Logout Success ✅")
def close_browser(driver):
    time.sleep(2)
    driver.quit()

def main():
    driver = setup_driver()
    open_website(driver, "https://www.saucedemo.com/")
    login(driver, "standard_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)
    time.sleep(1)
    
    # login(driver, "locked_out_user", "secret_sauce")
    # verify_login(driver)
    # open_sidebar(driver)
    # logout(driver)
    # verify_logout(driver)
    # time.sleep(1)

    login(driver, "problem_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)
    time.sleep(1)

    login(driver, "performance_glitch_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)
    time.sleep(1)

    login(driver, "error_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)
    time.sleep(1)

    login(driver, "visual_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)

    close_browser(driver)








if __name__ == "__main__":
    main()