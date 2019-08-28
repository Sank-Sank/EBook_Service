from django.http import JsonResponse
from .models import *
import json


def createUser(request):
	'''
	创建用户,参数:账户 密码 姓名 性别
	'''
	data = request.GET
	account = data['account']
	password = data['password']
	name = data['name']
	gender = data['gender']
	mail = data['mail']
	import time
	createTime = time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime(time.time()))
	# 向数据库中添加用户信息
	dic = {
		'user_account' : account,
		'user_password' : password,
		'user_name' : name,
		'user_gender' : gender,
		'create_time' : createTime,
		'user_mail' : mail
	}
	try:
		UserInfo.objects.create(**dic)
	except BaseException as e:
		print(str(e))
		return JsonResponse({"status":1,"message":"The account already exists"})
	return JsonResponse({"status":0,"message":"Create success"})


def login(request):
	'''
	用户登录，参数：账号 密码
	'''
	data = request.GET
	account = data['account']
	password = data['password']
	try:
		u = UserInfo.objects.get(user_account=account)
	except UserInfo.DoesNotExist:
		return JsonResponse({"status":1,"message":"The user was not found"})
	if str(u.user_password) == str(password):
		context = {
			"status":0,
			"message": "login Success",
			"account": u.user_account,
			"name": u.user_name,
			"gender": u.user_gender,
		}
		return JsonResponse(context)
	else:
		context = {
			"status":2,
			"message":"This password is wrong"
		}
		return JsonResponse(context)


def retrievePassword(request):
	'''
	找回密码，参数：账号 邮箱
	'''
	data = request.GET
	account = data['account']
	mail = data['mail']
	try:
		u = UserInfo.objects.get(user_account=account)
	except UserInfo.DoesNotExist:
		return JsonResponse({"status":1,"message":"The user was not found"})
	if str(u.user_mail) == str(mail):
		context = {
			"status":0,
			"password":u.user_password
		}
		return JsonResponse(context)
	else:
		return JsonResponse({"status":2,"message":"This mail is incorrect"})


def userBook(request):
	'''
	用户书架中的书籍
	'''
	data = request.GET
	account = data['account']
	try:
		u = UserInfo.objects.get(user_account=account)
	except UserInfo.DoesNotExist:
		return JsonResponse({"status":1,"message":"The user was not found"})
	books = u.userbook_set.all()
	l = []
	for b in books:
		dic = {}
		dic["name"] = b.save_book_name
		dic["author"] = b.save_book_author
		dic["synopsis"] = b.save_book_synopsis
		dic["image"] = b.save_book_image
		dic["update_time"] = b.save_update_time
		l.append(dic)
	context = {
		"status": 0,
		"books": l
	}
	return JsonResponse(context)



def addBook(request):
	'''
	添加书籍到书架中
	'''
	data = request.GET
	account = data['account']
	name = data["name"]
	author = data["author"]
	synopsis = data["synopsis"]
	image = data["image"]
	update_time = data["updatetime"]
	import time
	save_time = time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime(time.time()))
	try:
		u = UserInfo.objects.get(user_account=account)
	except UserInfo.DoesNotExist:
		return JsonResponse({"status":1,"message":"The user was not found"})
	dic = {
		'save_book_name' : name,
		'save_book_author' : author,
		'save_book_synopsis' : synopsis,
		'save_book_image' : image,
		'save_update_time': update_time,
		'save_time' : save_time,
		'this_user' : u
	}
	try:
		UserBook.objects.create(**dic)
	except BaseException as e:
		print(str(e))
		return JsonResponse({"status":2,"message":"add failure"})
	return JsonResponse({"status":0,"message":"add success"})
