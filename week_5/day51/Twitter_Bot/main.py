from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from dotenv import load_dotenv
import os
import time
import re

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("EMAIL")
TWITTER_PASSWORD = os.getenv("PASSWORD")
TWITTER_USERNAME = os.getenv("USERNAME")

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 30)
        self.up = None
        self.down = None

    def _is_numberish(self, s: str) -> bool:
        return bool(re.fullmatch(r"\d+(\.\d+)?", (s or "").strip()))

    def _read_text(self, css_selector: str) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, css_selector).text.strip()

    def _try_accept_cookies(self):
        for selector in [
            "#onetrust-accept-btn-handler",           # OneTrust
            "button#_evidon-banner-acceptbutton",     # Evidon
            "button[aria-label='Accept all']",
            "button[mode='primary']",                 # occasionally used
        ]:
            try:
                btn = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                btn.click()
                return
            except TimeoutException:
                pass

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self._try_accept_cookies()

        go_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))
        )
        go_button.click()

        end_time = time.time() + 120
        last_down, last_up = "", ""

        while time.time() < end_time:
            try:
                down = self._read_text("span.download-speed")
                up = self._read_text("span.upload-speed")
                last_down, last_up = down, up

                if self._is_numberish(down) and self._is_numberish(up):
                    time.sleep(1)
                    self.down, self.up = down, up
                    print(f"Measured: {self.down} down / {self.up} up")
                    return
            except StaleElementReferenceException:
                pass
            time.sleep(1)

        raise TimeoutException(
            f"Speedtest did not produce numeric results in time. down='{last_down}' up='{last_up}'"
        )

    def _already_logged_in_to_x(self) -> bool:
        self.driver.get("https://x.com/home")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[aria-label='Home']"))
            )
            return True
        except TimeoutException:
            return False

    def _login_to_x_if_needed(self):
        if self._already_logged_in_to_x():
            return

        self.driver.get("https://x.com/i/flow/login")

        ident = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
        ident.send_keys(TWITTER_EMAIL)
        ident.send_keys(Keys.ENTER)

        try:
            username_prompt = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            if TWITTER_USERNAME:
                username_prompt.send_keys(TWITTER_USERNAME)
                username_prompt.send_keys(Keys.ENTER)
        except TimeoutException:
            pass

        pwd = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        pwd.send_keys(TWITTER_PASSWORD)
        pwd.send_keys(Keys.ENTER)

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[aria-label='Home']")))

    def tweet_at_provider(self):
        self._login_to_x_if_needed()

        self.driver.get("https://x.com/compose/tweet")

        textbox = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
        )

        tweet = (
            f"Hey Internet Provider, why is my internet speed {self.down} down / {self.up} up "
            f"when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?"
        )
        textbox.send_keys(tweet)

        post_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='tweetButton']"))
        )
        post_button.click()

        print("Posted (or attempted). Current URL:", self.driver.current_url)

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    try:
        bot.get_internet_speed()
        bot.tweet_at_provider()
    finally:
        bot.quit()