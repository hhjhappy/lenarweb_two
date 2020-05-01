from django.db import models
from django.utils import timezone
# Create your models here.
class Ops(models.Model):
    employ_id = models.BigIntegerField('工号')
    name = models.CharField('姓名', max_length=50)

class Visitors(models.Model):
    name = models.CharField('姓名', max_length=50)
    phone = models.CharField('电话', max_length=20, unique=True)
    company = models.CharField('所属公司', max_length=50)

class VisitRecord(models.Model):
    visit_time = models.DateTimeField("进入时间", default=timezone.now)
    leave_time = models.DateTimeField("离开时间", auto_now=True)
    visitors = models.ForeignKey(Visitors, on_delete=models.CASCADE)
    accompany_ops = models.ForeignKey(Ops, on_delete=models.CASCADE)
    reason = models.CharField('事由',max_length=100)
    finish = models.BooleanField('是否结束', default=False)

class Mytable(models.Model):
    tid = models.BigIntegerField()

