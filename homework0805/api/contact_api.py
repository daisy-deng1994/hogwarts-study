# editor:Daisy
# date:28/07/21 12:25 上午
from homework0718.api.base_api import BaseApi


class ContactApi(BaseApi):
    def create_member(self, user_id, name, department=[1], **kwargs):
        """
        创建成员
        :param user_id:成员UserID
        :param name:成员名称
        :param department:成员所属部门id列表
        :param kwargs:其它参数
        :return:
        """
        data = {
            "userid": user_id,
            "name": name,
            "department": department
        }
        data.update(kwargs)
        res = self.send("POST", f"user/create?access_token={self.token}", json=data)
        return res

    def get_member(self, user_id):
        """
        读取成员
        :param user_id:成员UserID
        :return:
        """
        res = self.send("GET", f"user/get?access_token={self.token}&userid={user_id}")
        return res

    def update_member(self,user_id,**kwargs):
        """
        更新成员
        :param user_id:成员UserID
        :return:
        """
        data = {
            "userid": user_id
        }
        data.update(kwargs)
        res = self.send("POST", f"user/update?access_token={self.token}", json=data)
        return res

    def delete_member(self,user_id):
        """
        删除成员
        :param user_id:成员UserID
        :return:
        """
        res = self.send("GET", f"user/delete?access_token={self.token}&userid={user_id}")
        return res
