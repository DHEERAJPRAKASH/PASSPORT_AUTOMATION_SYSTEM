# Generated by Django 3.2.7 on 2021-09-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PASSPORT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passportdatabase',
            name='ApplicationNo',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='passportdatabase',
            name='PanNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='passportdatabase',
            name='PhoneNumber',
            field=models.IntegerField(),
        ),
    ]
