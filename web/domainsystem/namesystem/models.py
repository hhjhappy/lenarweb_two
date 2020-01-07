from django.db import models
from django.db.models import Model

# Create your models here.

#创建网宿表结构
class wangsuinfo(Model):
    domainname = models.CharField(max_length = 100,primary_key=True);
    servicetype = models.CharField(max_length=20)
    cname = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    cdnservicestatus = models.CharField(max_length=20)
    enable = models.CharField(max_length=10)


#创建dnspod子解析列表
class dnspod(models.Model):
    recordid = models.IntegerField(primary_key=True)
    hostrecords = models.CharField(max_length=100)
    recordtype = models.CharField(max_length=10)
    Recordvalue = models.CharField(max_length=200)
    TTL = models.CharField(max_length=100)
    Operatingtime = models.DateTimeField()
    operation = models.CharField(max_length=10,null=True)
    note = models.CharField(max_length=200,null=True)

#创建dnspod-域名表结构
class dnspoddomain(models.Model):
    domainid = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20)
    TTL = models.IntegerField()
    name = models.CharField(max_length=100)


