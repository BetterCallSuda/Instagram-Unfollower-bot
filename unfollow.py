import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Chromedriver

option = Chromedriver()
driver = option.driver

def open_account(driver):
    driver.get("https://www.instagram.com/ghiliboiz")
    sleep(5)

    wait = WebDriverWait(driver, 20)

    # Checking our targets follower list
    followers_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/following/')]")
        )
    )

    followers_button.click()
    print(driver.page_source[:2000])

    sleep(5.2)

def unfollow_users(driver, max_unfollows=15):
    wait = WebDriverWait(driver, 10)
    unfollowed = 0

    print("🚀 Starting unfollow process...")

    while unfollowed < max_unfollows:

        # Get all "Following" buttons
        buttons = driver.find_elements(
            By.XPATH, "//button[.//div[text()='Following']]"
        )

        if not buttons:
            print("⚠️ No Following buttons found.")
            break

        for button in buttons:
            if unfollowed >= max_unfollows:
                break

            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    button
                )
                sleep(random.uniform(1.5, 3))

                button.click()

                # Confirm Unfollow popup
                confirm = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[text()='Unfollow']")
                    )
                )
                confirm.click()

                unfollowed += 1
                print(f"✓ Unfollowed ({unfollowed}/{max_unfollows})")

                sleep(random.uniform(10, 20))

            except (StaleElementReferenceException, ElementClickInterceptedException):
                continue

        # Scroll down followers modal
        try:
            modal = driver.find_element(By.XPATH, "//div[@role='dialog']")
            driver.execute_script("arguments[0].scrollTop += 500", modal)
            sleep(random.uniform(4, 6))
        except:
            break

    print(f"✅ Done. Unfollowed {unfollowed} users safely.")

open_account(driver)
unfollow_users(driver)