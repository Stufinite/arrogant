from django.db import models
from django.utils import timezone
from infernoWeb.models import User

# Create your models here.
class CompanyManager(models.Manager):
    def get_by_natural_key(self, brand):
        return self.get(brand=brand)

class Company(models.Model):
	objects = CompanyManager()

	brand = models.CharField(max_length=30, default='')
	banner = models.CharField(max_length=200, default='') # 大頭貼照片
	path = models.CharField(max_length=40, default='')
	area = models.CharField(max_length=10, default='')
	公司規模 = models.CharField(max_length=5, default='')
	地址 = models.CharField(max_length=40, default='')
	資本額 = models.CharField(max_length=10, default='')
	description = models.CharField(max_length=150, default='')
	def __str__(self):
		return self.brand

	def natural_key(self):
	    return {
	    	"brand":self.brand,
	    	"banner":self.banner,
	    	"area":self.area,
	    }

	class Meta:
	    unique_together = ('brand', 'path')
	    
class Job(models.Model):
	"""docstring for Job"""
	company = models.ForeignKey(Company)
	name = models.CharField(max_length=20, default='')
	intern_tf = models.BooleanField(default=False)
	has_salary_info = models.BooleanField(default=False)
	salary = models.CharField(max_length=30, default='')
	path = models.CharField(max_length=40, default='')
	avatar = models.CharField(max_length=200, default='') # 大頭貼照片
	def __str__(self):
		return self.name

class JobTag(models.Model):
	name = models.CharField(max_length=15)
	Job = models.ManyToManyField(Job)
	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=15)
	Job = models.ManyToManyField(Job)
	def __str__(self):
		return self.name


class SkillTag(models.Model):
	name = models.CharField(max_length=15)
	skill_field = models.CharField(max_length=10)
	Job = models.ManyToManyField(Job)
	def __str__(self):
		return self.name + '-' + '-' + self.skill_field



class Comment(models.Model):
	Job = models.ForeignKey(Job)
	author = models.ForeignKey(User, related_name='cmtauthor', default=10)
	create = models.DateTimeField(default=timezone.now)
	raw = models.CharField(max_length=500)
	def __str__(self):
		return self.raw

class LikesFromUser(models.Model):
    author = models.OneToOneField(User, related_name='lfuauthor')
    comment = models.ManyToManyField(Comment)	
    def __str__(self):
        return self.author.name

class PageLog(models.Model):
    user = models.ForeignKey(User, related_name='ploguser')
    Job = models.ForeignKey(Job)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.name + self.Job.name + self.create.date().__str__()