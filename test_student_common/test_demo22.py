from test_student_common.selenium_async import BasePage


class AreaPage(BasePage):

    def __init__(self):

        super().__init__()

    async def create_area(self):
        """新增区域"""
        self.get_elements(("xpath", "//p[text()='cr7777']")).click()
        await self.click(self.get_elements(("xpath", '//span[@aria-label="新增下属区域"]//*[name()="svg"]')))
        await self.send_keys(self.get_elements(("xpath", '//input[@name="name"]')), await self.mock_data())
        await self.send_keys(self.get_elements(("xpath", '//input[@name="code"]')), await self.mock_data())
        await self.click(self.get_elements(("xpath", '//button[text()="确定"]')))
        assert_info = await self.get_alert(("xpath", '//div[text()="新增成功"]'))
        return assert_info

    async def create_required_verification(self):
        """新增区域必填校验"""

        await self.click(await self.get_element(("xpath", '//span[@aria-label="新增下属区域"]//*[name()="svg"]')))
        await self.click(await self.get_element(("xpath", '//button[text()="确定"]')))
        assert_info = await self.get_alert(("xpath", '//p[text()="请输入该必填项"]'))
        await self.click(await self.get_element(("xpath", "//button[text()='取消']")))
        return assert_info
