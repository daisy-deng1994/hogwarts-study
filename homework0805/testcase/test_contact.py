# editor:Daisy
# date:28/07/21 12:32 上午
import logging
import allure
from faker import Faker
from homework0718.api.contact_api import ContactApi


@allure.feature("企业微信通讯录增删改查")
class TestContact:
    def setup_class(self):
        self.contact = ContactApi()
        self.fake = Faker('zh_CN')
        logging.info("生成虚假的姓名和电话")
        self.name = self.fake.name()
        self.userid = self.fake.bban()


    @allure.title("添加成员")
    def test_create_member(self):
        logging.info("---执行添加成员用例---")
        r = self.contact.create_member(user_id=self.userid, name=self.name, mobile=self.fake.phone_number())
        # print(r.json())
        assert r.json().get("errcode") == 0

    @allure.title("获取成员")
    def test_get_member(self):
        logging.info("---执行获取成员用例---")
        r = self.contact.get_member(user_id=self.userid)
        # print(r.json())
        assert r.json().get("errcode") == 0

    @allure.title("更新成员")
    def test_update_member(self):
        logging.info("---执行更新成员用例---")
        r = self.contact.update_member(user_id=self.userid)
        # print(r.json())
        assert r.json().get("errcode") == 0

    @allure.title("删除成员")
    def test_delete_member(self):
        logging.info("---执行删除成员用例---")
        r = self.contact.delete_member(user_id=self.userid)
        # print(r.json())
        assert r.json().get("errcode") == 0
