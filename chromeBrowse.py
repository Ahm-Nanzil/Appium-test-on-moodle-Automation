from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--disable-features=VizDisplayCompositor")

# Set user-agent to appear more like a regular browser
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Create a new instance of the Chrome driver with the configured options
driver = webdriver.Chrome(options=chrome_options)

# Open a website
driver.get('https://web.facebook.com/?')

# Keep the browser open for interaction
input("Press Enter to quit...")

# Close the browser
driver.quit()
