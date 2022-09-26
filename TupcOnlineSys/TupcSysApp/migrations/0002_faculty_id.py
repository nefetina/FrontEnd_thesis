# Generated by Django 4.0.4 on 2022-09-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_ID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ff_name', models.CharField(max_length=50)),
                ('fm_name', models.CharField(max_length=50)),
                ('fl_name', models.CharField(max_length=50)),
                ('f_suffix', models.CharField(max_length=50, null=True)),
                ('f_emp', models.CharField(max_length=100)),
                ('f_datereq', models.DateField()),
                ('f_daterel', models.DateField()),
                ('f_gsis', models.CharField(max_length=100, null=True)),
                ('f_gsisp', models.CharField(max_length=100, null=True)),
                ('f_tin', models.CharField(max_length=100, null=True)),
                ('f_pagibig', models.CharField(max_length=100, null=True)),
                ('f_phil', models.CharField(max_length=100, null=True)),
                ('f_other', models.CharField(max_length=100, null=True)),
                ('f_cp', models.CharField(max_length=100, null=True)),
                ('f_num', models.CharField(max_length=100, null=True)),
                ('f_add', models.CharField(max_length=200, null=True)),
                ('f_signature', models.ImageField(upload_to=None)),
            ],
        ),
    ]
