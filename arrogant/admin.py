from django.contrib import admin
from arrogant.models import *
# Register your models here.
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobTag)
admin.site.register(Category)
admin.site.register(SkillTag)
admin.site.register(Comment)
admin.site.register(LikesFromUser)
admin.site.register(PageLog)