# coding:UTF-8
"""用户登录管理"""
from datetime import datetime
from random import randint
import os
import traceback
import sys
import time
import hmac


class HmacEncrypt(object):
    def __init__(self, password):
        self.__key = 'statickey'
        self.password = password
        # self.__password = self.__hmac_encrypt()

    def __hmac_encrypt(self):
        self.__password = hmac.new(self.__key.encode('utf-8'), self.password.encode('utf-8'),
                                   digestmod='MD5').hexdigest()
        return self.__password

# class User(object,macEncrypt):
class User(object):  # 输入用户名、密码、时间，写入用户信息
    def __init__(self, username, password, logintime=0.0):
        # super(User, self).__init__(password)
        self.username = username
        self.password = password
        self.logintime = float(logintime)

    # def __hmac_encrypt(self):
    #     return super(User, self)._HmacEncrypt__hmac_encrypt()

    def update_writefile(self, filepath):
        with open(filepath + self.username + '.txt', 'w') as f:
            f.write('%s:%s:%s' % (self.username, self.password, self.logintime))

    def writefile(self, filepath):
        hmacpassword = HmacEncrypt(self.password)
        with open(filepath + self.username + '.txt', 'w') as f:
            f.write('%s:%s:%s' % (self.username, hmacpassword._HmacEncrypt__hmac_encrypt(), self.logintime))
        # with open(filepath + self.username + '.txt', 'w') as f:
        #     f.write('%s:%s:%s' % (self.username, self.__hmac_encrypt(), self.logintime))


class UserDataBase(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.alluser = []
        try:
            with open(self.filepath + 'alluser.txt', 'r') as f:
                for i in f.readlines():
                    self.alluser.append(i.strip())
        except IOError:
            print('error')
            self.alluser = []

    def isexist(self, username):
        return username in self.alluser

    def newuser(self, username, password, logintime=0.0):
        if self.isexist(username):
            return None
        new_user = User(username, password, logintime)
        self.alluser.append(username)
        self.quit()
        new_user.writefile(self.filepath)
        return new_user

    def _get_user_with_name(self, username):
        if not self.isexist(username):
            return None
        with open(self.filepath + username + '.txt', 'r') as f:
            name, pwd, lgtm = f.readline().split(':')
            user = User(name, pwd, lgtm)
            return user

    def _get_password_with_name(self, username):
        if not self.isexist(username):
            return None
        with open(self.filepath + username +'.txt', 'r') as f:
            name, pwd, lgtm = f.readline().split(':')
            return pwd

    def login(self, username, password, logintime):
        if not self.isexist(username):
            return 0, 0
        hmacobj = HmacEncrypt(password)
        user = self._get_user_with_name(username)
        pwd = self._get_password_with_name(username)
        if hmacobj._HmacEncrypt__hmac_encrypt() != pwd:
            return -1, 0
        if user.logintime == 0:
            user.logintime = logintime
            user.update_writefile(self.filepath)
            return -2, 0
        else:
            time_intervel = user.logintime - logintime
            last_time = user.logintime
            user.logintime = logintime
            user.update_writefile(self.filepath)
            return time_intervel, last_time

    def update_info(self, username, ch, new_info):
        if not self.isexist(username):
            return None
        with open(self.filepath + username + '.txt', 'r') as f:
            info = f.readline().split(':')
            info[ch] = new_info
            new_info_user = User(*info)
            if ch == 0:  # 0为对应的用户名，new_info为用户名
                os.remove(self.filepath + username + '.txt')
                self.alluser.remove(username)
                self.alluser.append(new_info)
                self.quit()
                new_info_user.update_writefile(self.filepath)
            elif ch == 1:
                new_info_user.writefile(self.filepath)
            elif ch == 2:
                new_info_user.update_writefile(self.filepath)
            return new_info_user

    def quit(self):
        with open(self.filepath + 'alluser.txt', 'w') as f:
            f.write('\n'.join(self.alluser))


class Manager(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.manager = UserDataBase(self.filepath)

    def create_new_user(self):
        username = input('input new user name:')
        password = input('input new password:')
        user = self.manager.newuser(username, password, 0.0)
        if user is None:
            print('username exists')
        else:
            print('success')

    def login(self):
        username = input('input user name:')
        password = input('input password:')
        (retval, last_time) = self.manager.login(username, password, datetime.now().timestamp())
        if retval == 0:
            print('user invalid')
        elif retval == -1:
            print('password incorrect')
        else:
            print('login success')
            if retval == -2 or abs(retval) > 4 * 60 * 60:
                print('welcome', username)
            else:
                print('welcome back', username, '.you already logged in at:',
                      datetime.fromtimestamp(round(float(last_time), 0)))
                # showtime = time.gmtime(last_time)
                # print('welcome back', username, '.you already logged in at: %d-%d-%d %d:%d:%d' % \
                #       (showtime.tm_year, showtime.tm_mon, showtime.tm_mday, showtime.tm_hour,
                #        showtime.tm_min, showtime.tm_sec))


def run():
    manager = Manager(r'/Users/joey/PycharmProjects/mywork/')
    judge = True
    prompt = """
    -------------------------
    select you num:
    (1): create new user
    (2): login
    (3): update data
    (4): check username
    (5): quit(last operate)
    :"""
    while judge:
        c = 5  # try的值要处理好，c在try模块中不通用
        try:
            c = int(input(prompt))
        except KeyboardInterrupt as e:
            traceback.print_exc(file=sys.stdout)
            c = 5
        finally:
            if c == 1:
                manager.create_new_user()
                time.sleep(2)
            elif c == 2:
                manager.login()
                time.sleep(2)
            elif c == 3:
                username = input('input newusername:')
                ch = int(input('input list ch:'))
                new_info = input('input change content:')
                manager.manager.update_info(username, ch, new_info)
                time.sleep(2)
            elif c == 4:
                username = input('input newusername:')
                if manager.manager.isexist(username):
                    print('user exists')
                else:
                    print('user inexistence')
                time.sleep(2)
            elif c == 5:
                # manager.manager.quit()
                time.sleep(2)
                judge = False


if __name__ == '__main__':
    run()
