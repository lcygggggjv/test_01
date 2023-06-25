import asyncio
import random
import string

from selenium.common import InvalidArgumentException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from test_student_common.config import Config


class BasePage:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(Config.sit_url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "tenantCode").send_keys(Config.tenantCode)
        self.driver.find_element(By.NAME, "account").send_keys(Config.account)
        self.driver.find_element(By.NAME, "password").send_keys(Config.password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # await self.show_wait_el_clickable((By.XPATH, "(//button[@type='button'])[1]"))

        # await self.click(await self.get_element((By.XPATH, "(//button[@type='button'])[1]")))
        # await self.show_wait_el_clickable((By.XPATH, '//p[text()="设备资产管理"]'))
        # self.driver.find_element("xpath", "//p[text()='设备资产管理']")
        # await self.show_wait_el_clickable((By.XPATH, '//p[text()="基础配置"]'))
        # self.driver.find_element("XPATH", "//p[text()='基础配置']")
        # self.driver.find_element(By.XPATH, '//p[text()="区域管理"]').click()

    def logins(self):

        self.get_elements(("xpath", "(//button[@type='button'])[1]")).click()
        self.get_elements(("xpath", '//p[text()="设备资产管理"]')).click()
        self.get_elements(("xpath", '//p[text()="基础配置"]')).click()
        self.get_elements(("xpath", '//p[text()="区域管理"]')).click()

    def get_elements(self, locator):
        el = self.show_wait_el_clickable_2(locator)
        return el

    def clicks(self, locator):
        """click点击"""
        el = self.driver.find_element(locator)
        try:
            el.click()
        except InvalidArgumentException as e:  # try,click点击不了，捕获异常，满足InvalidArgumentException错误类型
            # 通过action方法点击
            ActionChains(self.driver).click(el).perform()  # 初始化action对象
        return self

    def show_wait_el_clickable_2(self, locator):
        wait = WebDriverWait(driver=self.driver, timeout=15)
        el = wait.until(expected_conditions.element_to_be_clickable(locator))
        return el

    async def show_wait_el_clickable(self, locator):
        wait = WebDriverWait(driver=self.driver, timeout=15)
        el = await wait.until(expected_conditions.element_to_be_clickable(locator))
        return el

    async def get_element(self, locator):
        el = await self.show_wait_el_clickable(locator)
        return el

    async def get_alert(self, locator):
        el = await self.show_wait_el_clickable(locator)
        return el.text

    async def click(self, locator):
        """click点击"""
        el = await self.get_element(locator)
        try:
            el.click()

        except InvalidArgumentException as e:  # try,click点击不了，捕获异常，满足InvalidArgumentException错误类型
            # 通过action方法点击
            ActionChains(self.driver).click(el).perform()  # 初始化action对象
        return self

    async def send_keys(self, locator, word):
        """输入"""
        el = await self.get_element(locator)
        try:
            el.send_keys(word)
        except:

            ActionChains(self.driver).send_keys_to_element(el, word).perform()
            # 先移动定位光标元素，再输入内容
        return self

    @staticmethod
    async def mock_data(default_data="tc"):
        all_str = string.ascii_letters + string.digits
        rand_str = ''.join(random.sample(all_str, 3))
        rse = rand_str + default_data
        return rse


















    async def open(self):
        self.driver.get("https://teamsit.teletraan.io")

    async def wait_for_element(self, locator, timeout=10):
        return await asyncio.get_event_loop().run_in_executor(None, WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        ))

    async def wait_for_element_clickable(self, locator, timeout=10):
        return await asyncio.get_event_loop().run_in_executor(None, WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        ))


