# coding:UTF-8

"""usermanager test case"""

from unittest import TestCase
import usermanager


# 测试案例
class UserManagerTest(TestCase):
    def setUp(self) -> None:  # 每个测试前调用，用来调用链接数据库，或者预先某动作
        print('setUp')

    def tearDown(self) -> None:  # 每个测试后调用
        print('tearDown')

    def test_init(self):
        hmac = usermanager.HmacEncrypt('password')
        self.assertTrue(isinstance(hmac, usermanager.HmacEncrypt))
        self.assertTrue(hmac.password == 'password')
        self.assertEqual(hmac.password, 'password')
        self.assertEqual(hmac._HmacEncrypt__key, 'statickey')

    def test_attrerror(self):
        hmac = usermanager.HmacEncrypt('password')
        with self.assertRaises(AttributeError):
            value = hmac._HmacEncrypt__password

    def test_writerfile(self):
        user = usermanager.User('joeyss', 'joeyss')
        self.assertTrue(not user.update_writefile(''))

    def test_UserBataBase(self):
        with self.assertRaises(TypeError):
            userdb = usermanager.UserDataBase()


if __name__ == '__main__':
    UserManagerTest()

# 终端运行
# cd /Users/joey/PycharmProjects/mywork/
# $ python -m unittest usermanagertest
