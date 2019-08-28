from django.db import models


class BookName(models.Model):
    book_name = models.CharField(max_length=255)     # 书名
    book_type = models.CharField(max_length=50)     # 书的类型（玄幻）
    book_author = models.CharField(max_length=50)   # 书的作者
    book_synopsis = models.TextField()              # 书的简介
    book_image = models.CharField(max_length=255)   # 书的封面在本地的url
    update_time = models.CharField(max_length=100)  # 最后更新时间


class Section(models.Model):
    section_tables = models.CharField(max_length=255)      # 章节与章节的标题
    section_content = models.TextField()                    # 章节对应的内容

    # 设置外键，将章节与书名进行绑定
    this_book_name = models.ForeignKey("BookName", on_delete=models.CASCADE)

