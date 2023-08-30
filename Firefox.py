from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import concurrent.futures

def test_load():
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    driver.get('http://127.0.0.1:8000/')

    # Find the room name input field and enter the password
    password_field = driver.find_element(By.ID, 'room_name')
    password_field.send_keys('today')

    # Find the username input field and enter the username
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('anika')

    # Find the submit button with value "Enter Room"
    submit_button = driver.find_element(By.XPATH, '//*[@id="post-form"]/input[4]')

    # Click the submit button
    submit_button.click()

    # Wait for some time to simulate user activity
    time.sleep(5)

    # Close the browser
    driver.quit()

# Number of threads to create
num_threads = 50

# Create a thread pool executor
executor = concurrent.futures.ThreadPoolExecutor()

# Submit tasks to the executor
futures = [executor.submit(test_load) for _ in range(num_threads)]

# Wait for all tasks to complete
concurrent.futures.wait(futures)
