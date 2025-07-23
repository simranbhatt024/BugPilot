from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome browser
driver = webdriver.Chrome()
driver.get("file:///C:/Users/Simra/OneDrive/Desktop/qa-bug-dashboard/frontend/index.html")  # Your file path

print("🔍 Opening BugPilot form...")

# Fill the bug form
driver.find_element(By.ID, "title").send_keys("Selenium Bug Test")
driver.find_element(By.ID, "severity").send_keys("High")
driver.find_element(By.ID, "description").send_keys("Form testing via Selenium automation")
driver.find_element(By.ID, "screenshot").send_keys("https://testimage.com")
driver.find_element(By.ID, "status").send_keys("New")  # Optional: Bug status dropdown

print("Form fields filled.")

# Submit the form
driver.find_element(By.CSS_SELECTOR, "form button[type='submit']").click()
print("Form submitted. Waiting for response...")

time.sleep(2)  # Let the UI update

# Verify success message
success_message = driver.find_element(By.ID, "successMsg")
if success_message.is_displayed():
    print("🎉 Test Passed: Success message displayed after submission.")
else:
    print("Test Failed: Success message not found.")

driver.quit()
