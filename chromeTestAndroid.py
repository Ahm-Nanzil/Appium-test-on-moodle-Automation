from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',  # Replace with your emulator device name
    'appPackage': 'com.android.chrome',  # Replace with your app package name
    # 'appActivity': 'com.google.android.apps.chrome.Main',  # Replace with your app's main activity
    'appActivity': 'com.google.android.apps.chrome.IntentDispatcher',  # Replace with your app's main activity
    'autoGrantPermissions': True  # Grant all permissions automatically
}

# Connect to the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# time.sleep(50)
# ngrok_url = "https://0842-103-120-38-29.ngrok-free.app"  # Your ngrok URL
# driver.get(ngrok_url)


