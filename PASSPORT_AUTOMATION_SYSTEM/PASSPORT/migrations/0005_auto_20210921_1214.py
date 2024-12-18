# Generated by Django 3.2.7 on 2021-09-21 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PASSPORT', '0004_alter_passportdatabase_dateofbirth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passportdatabase',
            options={'ordering': ('ApplicationNo',)},
        ),
        migrations.AddField(
            model_name='passportdatabase',
            name='Passport_admin_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='passportdatabase',
            name='Police_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='passportdatabase',
            name='R_admin_verified',
            field=models.BooleanField(default=False),
        ),
    ]
