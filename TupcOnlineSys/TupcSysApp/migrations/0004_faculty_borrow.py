# Generated by Django 4.1.1 on 2022-10-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0003_faculty_passreset'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbname', models.CharField(max_length=100)),
                ('fbdate', models.DateField()),
                ('fbtime', models.TimeField()),
                ('fbreq', models.CharField(max_length=100)),
                ('fbreason', models.CharField(max_length=100, null=True)),
                ('fbsign', models.ImageField(upload_to=None)),
                ('fbstat', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
