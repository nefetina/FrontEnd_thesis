# Generated by Django 4.1.3 on 2023-01-03 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintain_record',
            name='i_sign',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
