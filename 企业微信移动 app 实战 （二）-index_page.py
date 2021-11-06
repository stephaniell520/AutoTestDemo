from appium.webdriver.common.mobileby import MobileBy
from basepage import BasePage


class IndexPage(BasePage):
    # 跳转到通讯录页面
    def goto_ContactPage(self):
        # 导入通讯录页面对象的类包
        from page_object.contact_page import ContactPage
        # 首页查找通讯录元素
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 返回通讯录页面实例对象
        return ContactPage(self.driver)
