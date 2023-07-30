import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Placeholder values, replace these with your actual credentials
ACCOUNT_EMAIL = "your_email@example.com"
ACCOUNT_PASSWORD = "your_password"
PHONE_NUMBER = "+1234567890"
LINK = 'Please provide the direct link to the job section with the search filter set to "easy apply" mode.'

driver = webdriver.Chrome()
driver.get(LINK)

sign_in = driver.find_element(By.XPATH, "./html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)

sign_in_button = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container  button")
sign_in_button.click()

# time.sleep(30)

time.sleep(1)
easy_apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
easy_apply_button.click()

time.sleep(1)

field = driver.find_elements(By.CSS_SELECTOR, ".artdeco-text-input .artdeco-text-input--input, .artdeco-text-input .artdeco-text-input--search")
for input_field in field:
    if input_field.get_attribute("value") == "":
        input_field.send_keys(PHONE_NUMBER)

time.sleep(2)
next_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button, .artdeco-button--2, .peek-carousel-controls__button")
next_button.click()

time.sleep(2)
save_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
if save_button.get_attribute("data-control-name") == "save_application_btn":
    save_button.click()

    time.sleep(2)
    continue_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
    continue_button.click()

    time.sleep(2)
    next_button = driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
    next_button.click()

    time.sleep(1)
    next_button_2 = driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
    next_button_2.click()

    # Question_section
    Question_Label = driver.find_elements(By.CSS_SELECTOR,".artdeco-text-input .artdeco-text-input--label")
    labels = []
    for label in Question_Label:
        labels.append(label.text)

    answer = driver.find_elements(By.CSS_SELECTOR, ".artdeco-text-input .artdeco-text-input--input, .artdeco-text-input .artdeco-text-input--input:required:invalid, .artdeco-text-input .artdeco-text-input--input:required:valid, .artdeco-text-input .artdeco-text-input--search, .artdeco-text-input .artdeco-text-input--search:required:invalid, .artdeco-text-input .artdeco-text-input--search:required:valid")
    index = 0
    for ans in answer:
        ans.send_keys(input(labels[index]))
        index += 1

    time.sleep(2)
    review_button = driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
    review_button.click()

    time.sleep(1)
    submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
    submit_button.click()
    time.sleep(5)
else:
    print("Something went wrong text me at: your_email@example.com and add the screenshot of the error to fix it")

driver.quit()
