# Generated by Django 3.2.7 on 2021-09-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PASSPORT', '0002_auto_20210921_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passportdatabase',
            name='DateOfBirth',
            field=models.DateField(auto_now_add=True),
        ),
    ]
