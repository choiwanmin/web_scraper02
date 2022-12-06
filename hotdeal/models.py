from django.db import models
from django.utils.timezone import now

# Create your models here.
class Deal(models.Model): # 장고를 통해서 orm을 하기 위해 모델스에 있는 모델을 상속 받아야 한다.
    img_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, primary_key=True)
    reply_count = models.IntegerField()
    up_count = models.IntegerField()
    cdate = models.DateTimeField(default=now)
    
    def __str__(self):
        return f'{self.title}-{self.reply_count}-{self.up_count}--{self.cdate}'