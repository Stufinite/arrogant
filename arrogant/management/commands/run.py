from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
import time
class Command(BaseCommand):
    help = 'Convenient Way to insert Intern of Yourator json into arrogant'
    def handle(self, *args, **options):
        while True:
            call_command('jobCrawler')
            call_command('updateIntern', 'intern.json')
            call_command('updateIntern', 'job.json')
            time.sleep(86400)
        self.stdout.write(self.style.SUCCESS('daily update Intern and Job Info success!!!'))