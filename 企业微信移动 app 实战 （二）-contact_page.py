from appium.webdriver.common.mobileby import MobileBy
from basepage import BasePage


class ContactPage(BasePage):
    # 跳转到添加方式选择页面
    def goto_AddTypePage(self):
        from page_object.addtype_page import AddTypePage
        # 通讯录页面查找添加成员元素
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        # 返回通讯录页面实例对象
        return AddTypePage(self.driver)
