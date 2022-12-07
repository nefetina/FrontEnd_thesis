# Generated by Django 4.1.4 on 2022-12-07 07:38

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
                ('f_pic', models.TextField(max_length=10000, null=True)),
                ('email1', models.CharField(max_length=50, null=True)),
                ('ff_name', models.CharField(max_length=50)),
                ('fm_name', models.CharField(max_length=50, null=True)),
                ('fl_name', models.CharField(max_length=50)),
                ('f_suffix', models.CharField(max_length=50, null=True)),
                ('f_emp', models.CharField(max_length=100)),
                ('f_datereq', models.DateField(null=True)),
                ('f_daterel', models.DateField(null=True)),
                ('f_gsis', models.CharField(max_length=100, null=True)),
                ('f_gsisp', models.CharField(max_length=100, null=True)),
                ('f_tin', models.CharField(max_length=100, null=True)),
                ('f_pagibig', models.CharField(max_length=100, null=True)),
                ('f_phil', models.CharField(max_length=100, null=True)),
                ('f_other', models.CharField(max_length=100, null=True)),
                ('f_cp', models.CharField(max_length=100, null=True)),
                ('f_num', models.CharField(max_length=100, null=True)),
                ('f_add', models.CharField(max_length=200, null=True)),
                ('f_signature', models.TextField(max_length=10000, null=True)),
                ('f_stat', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='maintain_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_type4', models.CharField(max_length=100, null=True)),
                ('is_num4', models.CharField(max_length=100, null=True)),
                ('i_datem', models.DateField()),
                ('i_brand4', models.CharField(max_length=100, null=True)),
                ('i_code', models.CharField(max_length=100, null=True)),
                ('ie_name', models.CharField(max_length=100, null=True)),
                ('iup_sstats', models.CharField(max_length=100, null=True)),
                ('i_remarks', models.CharField(max_length=100, null=True)),
                ('i_cobfs', models.CharField(max_length=100, null=True)),
                ('i_remarks2', models.CharField(max_length=100, null=True)),
                ('iup_sstats2', models.CharField(max_length=100, null=True)),
                ('i_remarks3', models.CharField(max_length=100, null=True)),
                ('i_scan', models.CharField(max_length=100, null=True)),
                ('i_remarks4', models.CharField(max_length=100, null=True)),
                ('ia_virus', models.CharField(max_length=100, null=True)),
                ('i_remarks5', models.CharField(max_length=100, null=True)),
                ('im_stats', models.CharField(max_length=100, null=True)),
                ('i_remarks6', models.CharField(max_length=100, null=True)),
                ('ik_stats', models.CharField(max_length=100, null=True)),
                ('i_remarks7', models.CharField(max_length=100, null=True)),
                ('i_dust', models.CharField(max_length=100, null=True)),
                ('i_remarks8', models.CharField(max_length=100, null=True)),
                ('i_organize', models.CharField(max_length=100, null=True)),
                ('i_remarks9', models.CharField(max_length=100, null=True)),
                ('i_wipe', models.CharField(max_length=100, null=True)),
                ('i_remarks10', models.CharField(max_length=100, null=True)),
                ('i_run', models.CharField(max_length=100, null=True)),
                ('i_remarks11', models.CharField(max_length=100, null=True)),
                ('i_defragement', models.CharField(max_length=100, null=True)),
                ('i_remarks12', models.CharField(max_length=100, null=True)),
                ('i_empty', models.CharField(max_length=100, null=True)),
                ('i_remarks13', models.CharField(max_length=100, null=True)),
                ('i_create', models.CharField(max_length=100, null=True)),
                ('i_remarks14', models.CharField(max_length=100, null=True)),
                ('iu_pers4', models.CharField(max_length=100, null=True)),
                ('is_date4', models.DateField()),
                ('is_time4', models.TimeField()),
                ('ie_date4', models.DateField()),
                ('ie_time4', models.TimeField()),
                ('is_rec4', models.CharField(max_length=200, null=True)),
                ('ie_user4', models.CharField(max_length=200, null=True)),
                ('i_sig5', models.TextField(max_length=10000, null=True)),
                ('ie_date5', models.DateField()),
                ('i_time2', models.TimeField()),
                ('i_stats', models.CharField(max_length=100, null=True)),
                ('i_sign', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='borrow_record',
            name='i_sig5',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_borrow',
            name='fbsign',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_lab',
            name='fl_sig',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_reports',
            name='fsign',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_reports',
            name='i_sig',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_reports',
            name='i_sig1',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_reports',
            name='i_sig2',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_reports',
            name='i_sig3',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='faculty_wifi',
            name='g_sig',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='sched_rec',
            name='h_sig',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='student_internet',
            name='g_sig2',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='student_wifi',
            name='g_sig1',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
