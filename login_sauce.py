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
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
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
def verify_login_failed(driver,expected_message):
    try:
        wait = WebDriverWait(driver,5)
        error_element= wait.until(EC.visibility_of_element_located((By.XPATH,"//h3[@data-test='error']")))
        error_text = error_element.text.lower()
        assert "inventory" not in driver.current_url, "Harusnya tidak berpindah halaman!"
        assert expected_message.lower() in error_text, \
            f"Expected '{expected_message}' tapi error message: '{error_element.text}'"
        print(f"Login Correctly Failed ✅ | Error: '{error_element.text}'")
        
    except AssertionError as e:
        print(f"Assertion Error ❌: {e}")
    except Exception as e:
        print(f"Error element not found ❌: {e}")

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

    print("\n = Positive Test Cases =")
    print("\n Standard user")
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

    print("\n Problem user")
    login(driver, "problem_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)
    time.sleep(1)

    print("\n Performance glitch user")
    login(driver, "performance_glitch_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)
    time.sleep(1)

    print("\n Error user")
    login(driver, "error_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)
    time.sleep(1)

    print("\n Visual user")
    login(driver, "visual_user", "secret_sauce")
    verify_login(driver)
    open_sidebar(driver)
    logout(driver)
    verify_logout(driver)

    print("\n = Negative Test Cases = ")
    print("\n Locked out user")
    login(driver, "locked_out_user", "secret_sauce")
    verify_login_failed(driver, expected_message="locked out")

    print("\n Wrong password")
    open_website(driver, "https://www.saucedemo.com/")  # reset halaman
    login(driver, "standard_user", "wrong_password")
    verify_login_failed(driver, expected_message="do not match")

    print("\n Unregistered username")
    open_website(driver, "https://www.saucedemo.com/")
    login(driver, "unknown_user", "secret_sauce")
    verify_login_failed(driver, expected_message="do not match")

    print("\n Empty username")
    open_website(driver, "https://www.saucedemo.com/")
    login(driver, "", "secret_sauce")
    verify_login_failed(driver, expected_message="username is required")

    print("\n Empty password")
    open_website(driver, "https://www.saucedemo.com/")
    login(driver, "standard_user", "")
    verify_login_failed(driver, expected_message="password is required")

    print("\n Both fields empty")
    open_website(driver, "https://www.saucedemo.com/")
    login(driver, "", "")
    verify_login_failed(driver, expected_message="username is required")
    
    close_browser(driver)




if __name__ == "__main__":
    main()