from appium import webdriver

desired_caps = {
    "platformName": "Windows",
    "app": r"C:\Program Files\WindowsApps\3312ADB7.MoodleDesktop_3.9.2.0_x64__t8q4t8fsbshw4\app\Moodle Desktop.exe",
}

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps)

# Perform further interactions with the Moodle app as needed

# Close the app
driver.quit()

