# Generated by Django 4.1.1 on 2022-11-23 10:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrow_record',
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
        migrations.CreateModel(
            name='faculty_borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbname', models.CharField(max_length=100)),
                ('fbdate', models.DateField()),
                ('fbtime', models.TimeField()),
                ('fbreq', models.CharField(max_length=100)),
                ('fbreason', models.CharField(max_length=100, null=True)),
                ('fbsign', models.ImageField(upload_to=None)),
                ('fbstat', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculty_ID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('f_signature', models.ImageField(upload_to=None)),
                ('f_stat', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculty_lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('dep', models.CharField(max_length=100, null=True)),
                ('l_date', models.DateField()),
                ('lab_num', models.CharField(max_length=100, null=True)),
                ('crs_sec', models.CharField(max_length=100, null=True)),
                ('s_time', models.TimeField()),
                ('e_time', models.TimeField()),
                ('fl_sig', models.ImageField(upload_to=None)),
                ('l_stat', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculty_passreset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fwname', models.CharField(max_length=100)),
                ('fwempID', models.CharField(max_length=100, null=True)),
                ('fwIDtype', models.CharField(choices=[('GSFE', 'GSFE'), ('TUP EMAIL', 'TUP EMAIL'), ('MS TEAMS', 'MS TEAMS'), ('ERS ACCOUNT', 'ERS ACCOUNT'), ('NAS', 'NAS')], max_length=40)),
                ('fwemail', models.CharField(max_length=100, null=True)),
                ('fwstat', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculty_reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftype', models.CharField(max_length=100)),
                ('fbrand', models.CharField(max_length=100, null=True)),
                ('fserial', models.CharField(max_length=100)),
                ('fspecs', models.CharField(max_length=100, null=True)),
                ('fnature', models.CharField(max_length=100, null=True)),
                ('fname', models.CharField(max_length=100)),
                ('Fposjob', models.CharField(max_length=100)),
                ('fdep', models.CharField(max_length=100, null=True)),
                ('fdate', models.DateField()),
                ('ftime', models.TimeField()),
                ('fsign', models.ImageField(upload_to=None)),
                ('fstat', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculty_wifi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gf_name', models.CharField(max_length=100)),
                ('g_dept', models.CharField(max_length=100, null=True)),
                ('g_des', models.CharField(max_length=100, null=True)),
                ('g_sys', models.CharField(max_length=100, null=True)),
                ('g_mac', models.CharField(max_length=100, null=True)),
                ('g_num', models.CharField(max_length=100, null=True)),
                ('g_email', models.CharField(max_length=100, null=True)),
                ('g_fac', models.CharField(max_length=100, null=True)),
                ('g_sig', models.ImageField(upload_to=None)),
                ('g_datereq', models.DateField()),
                ('g_stat', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_quant', models.CharField(max_length=100, null=True)),
                ('i_equip', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lgsfe', models.CharField(max_length=100)),
                ('lidno', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=100)),
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
                ('i_sig4', models.ImageField(upload_to=None)),
                ('is_date4', models.DateField()),
                ('is_time4', models.TimeField()),
                ('ie_date4', models.DateField()),
                ('ie_time4', models.TimeField()),
                ('is_rec4', models.CharField(max_length=200, null=True)),
                ('ie_user4', models.CharField(max_length=200, null=True)),
                ('i_sig5', models.ImageField(default='', upload_to=None)),
                ('ie_date5', models.DateField()),
                ('i_time2', models.TimeField()),
                ('i_stats', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PassReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psname', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('emp_idno', models.CharField(max_length=50, null=True)),
                ('Account', models.CharField(choices=[('GSFE', 'GSFE'), ('TUP EMAIL', 'TUP EMAIL'), ('MS TEAMS', 'MS TEAMS'), ('ERS ACCOUNT', 'ERS ACCOUNT'), ('NAS', 'NAS')], max_length=100, null=True)),
                ('psstats', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='repmain_rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_type', models.CharField(max_length=100)),
                ('i_brand', models.CharField(max_length=100, null=True)),
                ('is_num', models.DateField()),
                ('i_spec', models.CharField(max_length=100, null=True)),
                ('i_notbd', models.CharField(max_length=100, null=True)),
                ('if_name', models.CharField(max_length=100, null=True)),
                ('i_pos', models.CharField(max_length=100, null=True)),
                ('i_dept', models.ImageField(upload_to=None)),
                ('i_daterec', models.DateField()),
                ('i_time', models.TimeField()),
                ('ii_assess', models.CharField(max_length=100, null=True)),
                ('i_assessby', models.CharField(max_length=100, null=True)),
                ('i_sig', models.ImageField(upload_to=None)),
                ('i_dateass', models.DateField()),
                ('ip_assign', models.CharField(max_length=100, null=True)),
                ('i_quant', models.CharField(max_length=100, null=True)),
                ('i_units', models.CharField(max_length=100, null=True)),
                ('i_partics', models.CharField(max_length=100, null=True)),
                ('i_avail', models.CharField(max_length=100, null=True)),
                ('i_approve', models.CharField(max_length=100, null=True)),
                ('i_note', models.CharField(max_length=100, null=True)),
                ('i_coords', models.CharField(max_length=100, null=True)),
                ('i_sig1', models.ImageField(upload_to=None)),
                ('i_daterec1', models.DateField()),
                ('i_time1', models.TimeField()),
                ('iu_pers', models.CharField(max_length=100, null=True)),
                ('i_sig2', models.ImageField(upload_to=None)),
                ('is_date', models.DateField()),
                ('is_time', models.TimeField()),
                ('is_rec', models.CharField(max_length=200, null=True)),
                ('i_aor', models.CharField(max_length=200, null=True)),
                ('ie_user', models.CharField(max_length=200, null=True)),
                ('i_daterec2', models.DateField()),
                ('i_sig3', models.ImageField(upload_to=None)),
                ('i_time2', models.TimeField()),
                ('i_stats', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sched_rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hf_name', models.CharField(max_length=100)),
                ('h_dept', models.CharField(max_length=100, null=True)),
                ('h_daterec', models.DateField()),
                ('hl_num', models.CharField(max_length=100, null=True)),
                ('h_csec', models.CharField(max_length=100, null=True)),
                ('hs_time', models.TimeField()),
                ('he_time', models.TimeField()),
                ('h_sig', models.ImageField(upload_to=None)),
                ('h_stats', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='student_internet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gf_name2', models.CharField(max_length=100)),
                ('g_csec2', models.CharField(max_length=100, null=True)),
                ('g_snum2', models.CharField(max_length=100, null=True)),
                ('g_sem2', models.CharField(max_length=100, null=True)),
                ('g_or2', models.CharField(max_length=100, null=True)),
                ('g_num2', models.CharField(max_length=100, null=True)),
                ('g_email2', models.CharField(max_length=100, null=True)),
                ('g_add2', models.CharField(max_length=100, null=True)),
                ('gu_name2', models.CharField(max_length=100, null=True)),
                ('g_sig2', models.ImageField(upload_to=None)),
                ('g_daterec2', models.DateField()),
                ('g_stats2', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='student_wifi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gf_name1', models.CharField(max_length=100)),
                ('g_csec1', models.CharField(max_length=100, null=True)),
                ('g_snum1', models.CharField(max_length=100, null=True)),
                ('g_sem1', models.CharField(max_length=100, null=True)),
                ('g_or1', models.CharField(max_length=100, null=True)),
                ('g_sys1', models.CharField(max_length=100, null=True)),
                ('g_mac1', models.CharField(max_length=100, null=True)),
                ('g_num1', models.CharField(max_length=100, null=True)),
                ('g_email1', models.CharField(max_length=100, null=True)),
                ('g_add1', models.CharField(max_length=100, null=True)),
                ('g_sig1', models.ImageField(upload_to=None)),
                ('g_daterec1', models.DateField()),
                ('g_stats1', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='register1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Personal_description', models.CharField(default='', max_length=40, null=True)),
                ('gsfe', models.CharField(default='', max_length=100, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ids', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='idno')),
                ('User_name', models.CharField(max_length=50)),
                ('Password_data', models.CharField(default='', max_length=40, unique=True)),
            ],
        ),
    ]
