# Generated by Django 4.1.3 on 2022-12-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0010_faculty_id_f_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_id',
            name='f_sign',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]