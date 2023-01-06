import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "TWITTER_EMAIL"
TWITTER_PASSWORD = "TWITTER_PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        # email
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        # phone_number
        phone_number = self.driver.find_element(By.CLASS_NAME,
                                                'r-30o5oe')
        if phone_number:
            phone_number.send_keys("949600685")
            phone_number.send_keys(Keys.ENTER)
            time.sleep(5)

        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/span')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # writing text -> test internet

        tweet = self.driver.find_element(By.XPATH,
                                         '<span data-offset-key="6jkk8-0-0">hola <span data-text="true">dfsdfgsdfg</span></span>')
        tweet.send_keys(
            f'Porque la velocidad de mi internet es {self.down} ⏬ de bajada y es {self.up} ⏫ de subida, cuando pago por {PROMISED_DOWN}⏬/{PROMISED_UP} >:T')
        send_tweet = self.driver.find_element(By.XPATH,
                                              '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send_tweet.click()


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot(Service(ChromeDriverManager().install()))
    bot.get_internet_speed()
    bot.tweet_at_provider()
