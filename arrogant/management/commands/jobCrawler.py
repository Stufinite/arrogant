#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from arrogant.models import *
import requests, json, pyprind
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Convenient Way to insert Intern of Yourator json into arrogant'
    def handle(self, *args, **options):
        self.getIntern()
        self.getJob()
        self.stdout.write(self.style.SUCCESS('crawl Job Json success!!!'))

    def getIntern(self):
        intern = []
        for i in range(1, 1000):
            if requests.get('https://www.yourator.co/api/v2/jobs?position[]=2&page={}'.format(i)).json()['jobs'] == []:
                break
            intern += requests.get('https://www.yourator.co/api/v2/jobs?position[]=2&page={}'.format(i)).json()['jobs']
        for i in pyprind.prog_bar(intern):
            # print(i)  
            res = requests.get('https://www.yourator.co/'+i['path']).text
            soup = BeautifulSoup(res, "html.parser")
            i['inside'] = {}
            i['inside']['description'] = soup.select('.description')[0].text.strip()
            for j in soup.select('.basic-info'):
                key, value = j.text.strip().replace(' ','').replace('\n','').split('：')
                i['inside'][key] = value

            if i['has_salary_info']:
                for j in soup.select('h2'):
                    if j.text == '薪資範圍':
                        i['salary'] = j.findNext('article').text
        with open('intern.json', 'w') as f:
            json.dump(self.testData(intern), f)

    def getJob(self):
        job = []
        for i in range(1, 1000):
            if requests.get('https://www.yourator.co/api/v2/jobs?page={}'.format(i)).json()['jobs'] == []:
                break
            job += requests.get('https://www.yourator.co/api/v2/jobs?page={}'.format(i)).json()['jobs']

        for i in pyprind.prog_bar(job):
            res = requests.get('https://www.yourator.co/'+i['path']).text
            soup = BeautifulSoup(res, "html.parser")
            i['inside'] = {}
            i['inside']['description'] = soup.select('.description')[0].text.strip() if len(soup.select('.description')) else ''
            for j in soup.select('.basic-info'):
                key, value = j.text.strip().replace(' ','').replace('\n','').split('：')
                i['inside'][key] = value

            if i['has_salary_info']:
                for j in soup.select('h2'):
                    if j.text == '薪資範圍':
                        i['salary'] = j.findNext('article').text
        with open('job.json', 'w') as f:
            json.dump(self.testData(job), f)

    @staticmethod
    def testData(data):
        return list(filter(lambda x:x['inside']['description']!='', data))