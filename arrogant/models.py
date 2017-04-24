from django.db import models
import datetime
# 要取得會員的model要這樣寫
from userper import Userper
User = Userper('login.stufinite.faith')

# Create your models here.
class Company(models.Model):
	company = models.CharField(max_length=20)
	def __str__(self):
		return self.company

class Job(models.Model):
	"""docstring for Job"""
	avatar = models.ImageField(default='politician.png') # 大頭貼照片
	職務類別 = models.CharField(max_length=20, null=True)
	學歷限制 = models.CharField(max_length=20, null=True)
	job = models.CharField(max_length=20)
	聯絡人員 = models.CharField(max_length=20, null=True)
	需求人數 = models.CharField(max_length=20, null=True)
	工作經驗 = models.CharField(max_length=20, null=True)
	到職日期 = models.CharField(max_length=20, null=True)
	薪資 = models.CharField(max_length=20, null=True)
	地區 = models.CharField(max_length=20, null=True)
	科系限制 = models.CharField(max_length=20, null=True)
	工作時間 = models.CharField(max_length=20, null=True)
	休假制度 = models.CharField(max_length=20, null=True)
	工作地點 = models.CharField(max_length=20, null=True)
	實習時段 = models.CharField(max_length=20, null=True)
	職缺更新 = models.CharField(max_length=20, null=True)
	工作性質 = models.CharField(max_length=20, null=True)
	company = models.ForeignKey(Company)
	url = models.CharField(max_length=100)
	工作說明 = models.CharField(max_length=20, null=True)
	身份類別 = models.CharField(max_length=20, null=True)
	def __str__(self):
		return self.job

class Comment(models.Model):
	Job = models.ForeignKey(Job)
	author = User
	create = models.DateTimeField(default=datetime.datetime.now)
	raw = models.CharField(max_length=500)
	def __str__(self):
		return self.raw
