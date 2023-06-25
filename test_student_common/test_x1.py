
from test_student_common.selenium_async import BasePage
from test_student_common.test_demo22 import AreaPage
import pytest


class TestArea:

    test_area = None

    def setup_method(self):

        self.test_area = AreaPage()
        self.test_area.logins()

    @pytest.mark.asyncio
    async def test_create(self):

        assert_info = await self.test_area.create_area()

        assert assert_info == "新增成功"

    @pytest.mark.asyncio
    async def test_required_verification(self):

        assert_info = await self.test_area.create_required_verification()

        assert assert_info == "请输入该必填项"

