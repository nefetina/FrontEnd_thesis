# Generated by Django 4.1.3 on 2022-12-13 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0006_remove_schedule_l1_l1sat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule_l2',
            name='l2sat',
        ),
    ]
