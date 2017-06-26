from django.core.management.base import BaseCommand, CommandError
from arrogant.models import *
import json, pyprind

class Command(BaseCommand):
    help = 'Convenient Way to insert Intern of Yourator json into arrogant'
    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('json', type=str)

    def handle(self, *args, **options):
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
        obj, _ = Company.objects.get_or_create(
            brand=i['company']['brand'],
            banner=i['company']['banner'],
            path=i['company']['path'],
            area=i['company']['area'],
            公司規模=i['inside'].get('公司規模', '未公開'),
            地址=i['inside']['地址'],
            資本額=i['inside'].get('資本額', "未公開"),
            description=i['inside']['description']
        )
        return obj

    @staticmethod
    def getOrCreateJob(company, category, i):
        obj, _ = Job.objects.get_or_create(
            name=i['name'],
            intern_tf=i['intern'],
            has_salary_info=i['has_salary_info'],
            salary=i.get('salary', "未公開"),
            path=i['path'],
            avatar=i['company']['banner'],
            company=company,
            category=category
        )
        return obj

    @staticmethod
    def getOrCreateTag(tags, job):
        result = []
        for i in tags:
            obj, _ = JobTag.objects.get_or_create(
                name=i['name'],
            )
            obj.Job.add(job)
            result.append(obj)
        return result

    @staticmethod
    def getOrCreateCategory(i):
        obj, _ = Category.objects.get_or_create(
            name=i['name'],
        )
        return obj

    @staticmethod
    def getOrCreateSkillTag(skills, job):
        result = []
        for i in skills:
            obj, _ = SkillTag.objects.get_or_create(
                name=i['name'],
                skill_field=i['skill_field'],
            )
            obj.Job.add(job)
            result.append(obj)
        return result
