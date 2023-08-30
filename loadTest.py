from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time
import threading

# Set up desired capabilities
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',  # Replace with your emulator device name
    'appPackage': 'com.moodle.moodlemobile',  # Replace with your app package name
    'appActivity': '.MainActivity',  # Replace with your app's main activity
    'autoGrantPermissions': True  # Grant all permissions automatically
}

# Number of login attempts to simulate
num_login_attempts = 10

# Function to simulate login attempt
def simulate_login_attempt():
    # Connect to the Appium server
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # Delay for app to load completely
    time.sleep(30)  # Adjust the delay as needed

    # Handle popup notification
    try:
        allow_button = driver.find_element(MobileBy.XPATH, "//android.widget.Button[@text='Allow']")
        allow_button.click()
        print("Clicked on Allow button")
    except NoSuchElementException:
        print("Popup notification not found or already handled")

    # Rest of your login code goes here...
   

    time.sleep(5)
    # Click on "Skip" button
    try:
        skip_button = driver.find_element(MobileBy.XPATH, "//android.widget.Button[@text='Skip']")
        skip_button.click()
        print("Clicked on Skip button")
    except NoSuchElementException:
        print("Skip button not found")

    time.sleep(5)
    # Find the text field and enter the value
    try:
        text_field = driver.find_element(MobileBy.CLASS_NAME, "android.widget.EditText")
        text_field.clear()
        text_field.send_keys("moodle.org")
        print("Filled the text field with 'moodle.org'")
    except NoSuchElementException:
        print("Text field not found")

    time.sleep(5)

    # Find the button by text and click it
    try:
        button = driver.find_element(MobileBy.XPATH,
                                     "//android.widget.Button[contains(@text, 'Connect to your site moodle.org')]")
        button.click()
        print("Clicked the button")
    except NoSuchElementException:
        print("Button not found")

    time.sleep(15)
    # Find the text field and fill it with the value "ahmnanzil"
    try:
        text_field = driver.find_element(MobileBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText")
        text_field.clear()  # Clear any existing text
        text_field.send_keys("ahmnanzil")
        print("Filled the text field with 'ahmnanzil'")
    except NoSuchElementException:
        print("Text field not found")

    # Click the pass button
    try:
        text_field = driver.find_element(MobileBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText")
        text_field.clear()  # Clear any existing text
        text_field.send_keys("ahmnanzil@")
        print("Filled the text field with pass")
    except NoSuchElementException:
        print("Text field not found")

    # Click on "LOG IN" button
    try:
        login_button = driver.find_element(MobileBy.XPATH, "//android.widget.Button[@text='LOG IN']")
        login_button.click()
        print("Clicked on LOG IN button")
    except NoSuchElementException:
        print("LOG IN button not found")
    time.sleep(25)
    # Click on "GOT IT" button
    try:
        got_it_button = driver.find_element(MobileBy.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button")
        got_it_button.click()
        print("Clicked on GOT IT button")
    except NoSuchElementException:
        print("GOT IT button not found")
    # Close the driver session
    driver.quit()

# Create a list to store the threads
threads = []

# Start the login attempt threads
for _ in range(num_login_attempts):
    t = threading.Thread(target=simulate_login_attempt)
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()
