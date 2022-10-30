# Generated by Django 4.1.1 on 2022-10-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TupcSysApp', '0002_passreset_psname_passreset_psstats'),
    ]

    operations = [
        migrations.CreateModel(
            name='UITC_borrow_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('if_name5', models.CharField(max_length=100, null=True)),
                ('i_date5', models.DateField()),
                ('i_time5', models.TimeField()),
                ('ir_borrow5', models.CharField(max_length=100, null=True)),
                ('irf_borrow5', models.CharField(max_length=100, null=True)),
                ('i_sig5', models.ImageField(upload_to=None)),
                ('i_stats5', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]