# Generated by Django 4.1.3 on 2022-12-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0005_alter_faculty_borrow_fbrdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_borrow',
            name='fbmodel',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='faculty_borrow',
            name='fbserial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_borrow',
            name='fbremarks',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
