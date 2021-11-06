from appium.webdriver.common.mobileby import MobileBy
from basepage import BasePage


class AddTypePage(BasePage):
    # 跳转到添加方式页面
    def goto_AddMembersPage(self):
        from page_object.addmembers_page import AddMembersPage
        # 通讯录页面查找添加成员元素
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # 返回通讯录页面实例对象
        return AddMembersPage(self.driver)
