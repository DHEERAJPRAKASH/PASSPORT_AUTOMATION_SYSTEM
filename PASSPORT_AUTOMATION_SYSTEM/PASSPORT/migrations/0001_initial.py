# Generated by Django 3.2.7 on 2021-09-21 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassportDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('FatherName', models.CharField(max_length=50)),
                ('DateOfBirth', models.DateField(default=datetime.date(2021, 9, 21))),
                ('Address', models.CharField(max_length=100)),
                ('PermanentAddress', models.CharField(max_length=100)),
                ('PhoneNumber', models.IntegerField(max_length=10)),
                ('PanNo', models.IntegerField(max_length=10)),
                ('EmailId', models.EmailField(max_length=30)),
                ('ApplicationNo', models.IntegerField(max_length=20, unique=True)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]