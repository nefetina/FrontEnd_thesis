# Generated by Django 4.0.1 on 2023-01-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0009_student_wifi_adm'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_internet',
            name='adm',
            field=models.DateTimeField(null=True),
        ),
    ]