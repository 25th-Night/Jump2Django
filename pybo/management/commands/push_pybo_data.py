import datetime

from django.core.management.base import BaseCommand

from pybo.models import Question
from django.utils import timezone

# TODO: 커맨드 활용
# https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/#testing
class Command(BaseCommand):
    help = "Push DATA by loop"

    def handle(self, *args, **options):
        for i in range(300):
            q = Question(subject='테스트 데이터입니다:[%03d]' % i, content='내용무', create_date=timezone.now())
            q.save()
