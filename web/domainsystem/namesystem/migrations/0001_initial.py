# Generated by Django 2.2.7 on 2019-12-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dnspod',
            fields=[
                ('recordid', models.IntegerField(primary_key=True, serialize=False)),
                ('hostrecords', models.CharField(max_length=100)),
                ('recordtype', models.CharField(max_length=10)),
                ('Recordvalue', models.IntegerField()),
                ('TTL', models.CharField(max_length=100)),
                ('Operatingtime', models.DateTimeField()),
                ('operation', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dnspoddomain',
            fields=[
                ('domainid', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20)),
                ('TTL', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='wangsuinfo',
            fields=[
                ('domainname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('servicetype', models.CharField(max_length=20)),
                ('cname', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('cdnservicestatus', models.CharField(max_length=20)),
                ('enable', models.CharField(max_length=10)),
            ],
        ),
    ]
