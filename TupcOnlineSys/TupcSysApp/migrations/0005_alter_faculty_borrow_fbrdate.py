# Generated by Django 4.1.3 on 2022-12-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0004_alter_inventory_i_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_borrow',
            name='fbrdate',
            field=models.DateField(null=True),
        ),
    ]
