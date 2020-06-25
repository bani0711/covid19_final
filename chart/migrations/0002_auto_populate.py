# chart/migrations/0002_auto_populate.py
"""
DB 현행화 작업이 실행될 때, csv 파일 자료를 DB에 자동적으로 적재한다.
"""
import csv
import os
import datetime
from django.db import migrations
from django.conf import settings

# csv 파일의 해당 열 번호를 상수로 정의
DATE = 0            # 날짜
COUNTRY = 1         # 국가
CONFIRMED = 2       # 확진자 수
RECOVERED = 3       # 회복자 수
DEATHS = 4          # 사망자 수

def add_status(apps, schema_editor):
    Status = apps.get_model('chart', 'Status')
    csv_file = os.path.join(settings.BASE_DIR, 'covid19.csv')
    with open(csv_file) as dataset:                   # 파일 객체 dataset
        reader = csv.reader(dataset)                    # 파일 객체 dataset에 대한 판독기 획득
        next(reader)  # ignore first row (headers)      # __next__() 호출 때마다 한 라인 판독
        for entry in reader:                            # 판독기에 대하여 반복 처리
            Status.objects.create(                       # DB 행 생성
                date=datetime.datetime.strptime(entry[DATE], '%Y-%m-%d'),
                country=entry[COUNTRY],
                confirmed=int(entry[CONFIRMED]),
                recovered=int(entry[RECOVERED]),
                deaths=int(entry[DEATHS]),
            )

class Migration(migrations.Migration):
    dependencies = [
        ('chart', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_status),
    ]