# Generated by Django 4.0.1 on 2023-01-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0012_borrow_record_adm_faculty_passreset_adm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_borrow',
            name='adm',
            field=models.DateTimeField(null=True),
        ),
    ]
