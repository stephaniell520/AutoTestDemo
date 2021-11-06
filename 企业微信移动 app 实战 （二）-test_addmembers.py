import pytest
import yaml
from page_object.index_page import IndexPage
import logging


class TestAddMembers:
    # 启动设备，准备资源
    def setup(self):
        pass
    
    # 添加成员方法
    data = [('name1','15900000001'),('name2','15900000002')]
    @pytest.mark.parametrize('name,phone',data)
    def test_add_members(self,name,phone):
        # 将测试数据保存在yaml文件
        with open("../page_Object/test.yaml", "w") as f:
            yaml.safe_dump('data', f)
        # 首页页面对象实例化
        self.index = IndexPage()
        # 添加成员
        self.MembersList = self.index.goto_ContactPage().goto_AddTypePage().goto_AddMembersPage().AddMembers()

    def test_logfile_mymap(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('Started')
        logging.debug('This message should go to the log file')
        logging.warning('And this, too')
        logging.info('Finished')

    # 关闭资源
    def teardown(self):
        self.driver.quit()
