# Generated by Django 4.1.4 on 2023-01-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0004_schedule_lab_delete_schedule_l1_delete_schedule_l2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_lab',
            name='lfri',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schedule_lab',
            name='lmon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schedule_lab',
            name='lthu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schedule_lab',
            name='ltue',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schedule_lab',
            name='lwed',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
