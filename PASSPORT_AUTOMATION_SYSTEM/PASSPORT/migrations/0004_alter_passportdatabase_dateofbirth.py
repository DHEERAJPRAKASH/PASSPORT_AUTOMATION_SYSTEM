# Generated by Django 3.2.7 on 2021-09-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PASSPORT', '0003_alter_passportdatabase_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passportdatabase',
            name='DateOfBirth',
            field=models.DateField(),
        ),
    ]