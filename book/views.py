from django.http import JsonResponse
from .models import *
import json
from django.core import serializers
from django.core.paginator import Paginator


def search(request):
	"""
	多表联查
	"""
	data =request.GET
	bookName = data['name']
	print(bookName)
	try:
		s = BookName.objects.get(book_name=bookName)	
	except BookName.DoesNotExist:
		return JsonResponse({"status":1,"message":"Not find this book"})
	print(s)
	# section  = s.section_set.all()
	# for ss in section:
	#	print(ss.content)
	context = {
		"status": 0,
		"bookname": s.book_name,
		"booktype": s.book_type,
		"book_author": s.book_author,
		"book_synopsis": s.book_synopsis,
		"book_image": s.book_image,
		"update_time": s.update_time, 	
	}
	return JsonResponse(context)


def getChapters(request):
	"""
	观看小说：
		参数:bookName
	"""
	data = request.GET
	bookName = data['bookName']
	print(bookName)
	b = BookName.objects.get(book_name=bookName)
	chapters = b.section_set.all()
	print(type(chapters))
	l = []
	for ss in chapters:
		dic = {}
		dic["id"] = ss.id
		dic["chapter"] = ss.section_tables
		l.append(dic)
	context = {
		"status": 0,
		"chapters": l
	}
	return JsonResponse(context)



def getChapterContent(request):
	'''
	获取章节内容
		参数:章节id
	'''
	data = request.GET
	cid = data['id']
	try:
		c = Section.objects.get(id=cid)
	except Section.DoesNotExist:
		return JsonResponse({"status": 1,"message":"Not find this id"})
	print(c)
	context = {
		"status": 0,
		"title": c.section_tables,
		"content": c.section_content
	}
	return JsonResponse(context)



def getType(request):
	data = request.GET
	t = data['type']
	pa = data['page']
	c = BookName.objects.filter(book_type=t)
	p = Paginator(c,20)
	context = {
		"status": 0,	
		"count": p.num_pages,
		"pages": json.loads(serializers.serialize("json",p.page(pa)))
	}
	return JsonResponse(context)



def bookMall(request):
	l = []
	l1 = ["http://i1.17173cdn.com/9ih5jd/YWxqaGBf/forum/images/2014/08/01/231302zkvvgn1ng0lnglzn.jpg","http://i1.17173cdn.com/9ih5jd/YWxqaGBf/forum/images/2014/08/05/201159yhhz33h3lz5awoww.jpg","http://i1.17173cdn.com/9ih5jd/YWxqaGBf/forum/images/2014/08/05/201152iqo0a52o9wo5m8dy.jpg","http://img4.imgtn.bdimg.com/it/u=360400174,1298800920&fm=15&gp=0.jpg"]
	d = {}
	d["tag"] = 0
	d["imageList"] = l1
	l.append(d)
	d1 = {}
	d1["tag"] = 1
	l2 = []
	for i in range(13883,13891):
		s = BookName.objects.get(id=i)
		dd = {}
		dd["status"] = 0
		dd["bookname"] = s.book_name
		dd["booktype"] = s.book_type
		dd["book_author"] = s.book_author
		dd["book_synopsis"] = s.book_synopsis
		dd["book_image"] = s.book_image
		dd["update_time"] = s.update_time
		l2.append(dd)
	d1["bookList"] = l2
	l.append(d1)
	d2 = {}
	d2["tag"] = 2
	l3 = []
	for i in range(13353,13359):
		s = BookName.objects.get(id=i)
		dd = {}
		dd["status"] = 0
		dd["bookname"] = s.book_name
		dd["booktype"] = s.book_type
		dd["book_author"] = s.book_author
		dd["book_synopsis"] = s.book_synopsis
		dd["book_image"] = s.book_image
		dd["update_time"] = s.update_time
		l3.append(dd)
	d2["bookList"] = l3
	l.append(d2)
	context = {
		"status" : 0,
		"data" : l
	}
	return JsonResponse(context)

