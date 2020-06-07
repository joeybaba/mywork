"""七夕小礼物"""
import time


class IsNotBirthdayError(Exception):
	pass


class NameNotFoundError(Exception):
	pass

class BirthdayNotFoundError(Exception):
	pass


class Lover():
	"""情侣基类"""

	def __init__(self, sex, age, name=None, birthday=None):
		self.sex = sex # 男/女
		self.age = age # 整数，如：23
		self.birthday = birthday # 生日应为(年, 月, 日)的元组形式
		self.name = name
		if self.birthday != None:
			self.formatted_birthday = str(self.birthday[0]) + "年" + \
				str(self.birthday[1]) + "月" + str(self.birthday[2]) + "日"

	def get_sex(self):
		"""获取性别"""
		return self.sex

	def get_age(self):
		"""获取年龄"""
		return self.age

	def is_current_age(self, age):
		"""是否为指定年龄"""
		return self.age == age

	def is_male(self):
		"""是否为男性"""
		return self.sex == "男"

	def is_female(self):
		"""是否为女性"""
		return self.sex == "女"

	def celebrate(self, err=False):
		"""庆祝生日"""
		current_day = time.gmtime() # 获取当前时间
		if self.birthday[1:] != (
		current_day.tm_mon, current_day.tm_mday): # 如果生日未到，则做出提示
			if err: # 如果指定引发异常，则在异常中提示
			 	raise IsNotBirthdayError(
			 		"你的{}友生日未到，{}的生日是{}！".format(
			 			self.sex,"他" if self.sex == "男" else "她",self.formatted_birthday)
			 		)
			else: # 如果指定不引发异常，则在直接打印提示信息
			 	print(
			 		"你的{}友生日未到，{}的生日是{}！".format(
			 			self.sex,"他" if self.sex == "男" else "她",self.formatted_birthday)
			 		)

		elif self.name == None: # 如果未指定姓名， 则做出提示
			if err: #  如果指定引发异常，则在异常中提示
					raise NameNotFoundError(
						"您未给{}友指定姓名！".format(self.sex))
			else: # 如果指定不引发异常，则在直接打印提示信息
				print("您未给{}友指定姓名！".format(self.sex))

		elif self.birthday == None:
			if err: # 如果未指定姓名， 则做出提示
				raise BirthdayNotFoundError("您未给{}友指定生日！".format(self.sex))
			else: # 如果指定不引发异常，则在直接打印提示信息
				print("您未给{}友指定生日！".format(self.sex))
		else:
			print("祝您的{}友{}岁生日快乐！".format(self.sex, self.age))


class BoyFriend(Lover):
	"""男友类，继承Lover情侣基类"""

	def __init__(self, age, name=None, birthday=None):
		super().__init__(sex="男", age=age, name=name, birthday=birthday)


class GirlFriend(Lover):
	"""女友类，继承Lover情侣基类"""

	def __init__(self, age, name=None, birthday=None):
		super().__init__(sex="女", age=age, name=name, birthday=birthday)

if __name__ == "__main__":
	bf = BoyFriend(25, "王俊恺", (1995, 6, 7))
	print(bf.is_female())
	gf = GirlFriend(24, "杨蜜", (1996, 6, 7))
	print(gf.is_male())
	bf.celebrate()