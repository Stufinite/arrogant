from django.core.management.base import BaseCommand, CommandError
from arrogant.models import *
import json, pyprind

class Command(BaseCommand):
    help = 'Convenient Way to insert Intern of Yourator json into arrogant'
    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('json', type=str)

    def handle(self, *args, **options):
        Job.objects.all().update(available=False)
        file = options['json']
        with open(file, 'r') as f:
            for i in pyprind.prog_bar(json.load(f)):
                company = self.getOrCreateCompany(i)
                category = self.getOrCreateCategory(i['category'])
                job = self.getOrCreateJob(company, category, i)
                tags = self.getOrCreateTag(i['tags'], job)
                SkillTag = self.getOrCreateSkillTag(i['skill_tags'], job)

        self.stdout.write(self.style.SUCCESS('insert Json success!!!'))

    @staticmethod
    def getOrCreateCompany(i):
        try:
            obj, created = Company.objects.update_or_create(
                path=i['company']['path'],
                defaults={
                    "brand":i['company']['brand'],
                    "banner":i['company']['banner'],
                    "地址":i['inside']['地址'],
                    "資本額":i['inside'].get('資本額', "未公開"),
                    "公司規模":i['inside'].get('公司規模', '未公開'),
                    "area":i['company']['area'],
                    "description":i['inside']['description'],                    
                }
            )
        except Exception as e:
            print(i)
            raise e
        if created: print(obj)
        return obj

    @staticmethod
    def getOrCreateJob(company, category, i):
        try:
            obj, created = Job.objects.update_or_create(
                path=i['path'],
                defaults={
                    "name":i['name'],
                    "company":company,
                    "intern_tf":i['intern'],
                    "has_salary_info":i['has_salary_info'],
                    "salary":i.get('salary', "未公開"),
                    "avatar":i['company']['banner'],
                    "category":category,
                    "available":True
                }
            )
        except Exception as e:
            print(i['name'], i['path'])
            raise e
        if created: print(obj)
        return obj

    @staticmethod
    def getOrCreateTag(tags, job):
        result = []
        for i in tags:
            obj, created = JobTag.objects.get_or_create(
                name=i['name'],
            )
            if created: print(obj)            
            obj.Job.add(job)
            result.append(obj)
        return result

    @staticmethod
    def getOrCreateCategory(i):
        obj, created = Category.objects.get_or_create(
            name=i['name'],
        )
        if created: print(obj)
        return obj

    @staticmethod
    def getOrCreateSkillTag(skills, job):
        result = []
        for i in skills:
            obj, created = SkillTag.objects.get_or_create(
                name=i['name'],
                defaults={
                    "skill_field":i['skill_field'],
                }
            )
            if created: print(obj)            
            obj.Job.add(job)
            result.append(obj)
        return result
