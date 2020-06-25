# chart/models.py
from django.db import models

class Status(models.Model):  # 코로나19 현황 모델

    date = models.DateField()                        # 날짜
    country = models.CharField(max_length=100)       # 국가
    confirmed = models.IntegerField()                # 확진자 수
    recovered = models.IntegerField()                # 회복자 수
    deaths = models.IntegerField()                   # 사망자 수

    def __str__(self):
        return self.country