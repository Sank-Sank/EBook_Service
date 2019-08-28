from django.db import models

class UserInfo(models.Model):
	user_account = models.CharField(max_length=100,unique=True)		#用户账号唯一
	user_password = models.CharField(max_length=100)	#用户密码
	user_name = models.CharField(max_length=100)		#用户名
	user_gender = models.CharField(max_length=10)		#用户性别
	user_mail = models.CharField(max_length=50)			#用户邮箱
	create_time = models.CharField(max_length=50)		#创建时间


class UserBook(models.Model):
	save_book_name = models.CharField(max_length=100)				# 存储的书名
	save_book_author = models.CharField(max_length=50)   			# 书的作者
	save_book_synopsis = models.TextField()              			# 书的简介
	save_book_image = models.CharField(max_length=255)  	 		# 书的封面在本地的url
	save_update_time = models.CharField(max_length=100)  			# 最后更新时间

	save_time = models.CharField(max_length=50)						#存储的时间
	this_user = models.ForeignKey("UserInfo", on_delete=models.CASCADE)		#外键
